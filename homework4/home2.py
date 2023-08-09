import os.path
import argparse
import requests
from multiprocessing import Process
import os
import time

URL_list = ["https://static.gismeteo.st/assets/maps/n_prc.png",
            "https://shop.mts.ru/upload/rk/987/Desktop-952kh476-.jpg",
            "https://mtscdn.ru/upload/rk/cc4/perehod.png0",
            "https://media.komus.ru/medias/sys_master/root/h63/h6a/11848288043038/-.jpg",
            "https://faberlic.com/images/flippingbook/2023/Florange_RU_2023/cat-001.jpg",
            "https://faberlic.com/images/flippingbook/2023/Catalog_11/RU/cat-001.jpg",
            "https://faberlic.com/images/flippingbook/2023/Russia_Wallness_23/cat-001.jpg",
            "https://images.faberlic.com/images/fl/TflGoods/sm/1001347679976_16869259282.jpg",
            "https://images.faberlic.com/images/fl/TflGoods/sm/1001347679972_16893426293.jpg"]


def download(url_img, dir_name='download'):
    start_time = time.time()
    response = requests.get(url_img)
    *_, name_files, = url_img.split("/")
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    path_folder = os.path.join(dir_name, name_files)
    with open(path_folder, "wb") as f:
        f.write(response.content)
    print(f"{name_files} скачано за {time.time() - start_time} секунд")


def pars_path():
    """
    sample input url for terminal
    python home.py -p https://images.faberlic.com/images/fl/TflGoods/sm/1001347679976_16869259282.jpg
    """
    parser = argparse.ArgumentParser(prog="download image from urls")
    parser.add_argument('-p', metavar='p')
    args = parser.parse_args()
    return download(f'{args.p}')


def proc_download():
    processes = []
    for url in URL_list:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()


if __name__ == "__main__":

    start_time = time.time()
    proc_download()
    print(f"Всего за {time.time() - start_time} секунд")