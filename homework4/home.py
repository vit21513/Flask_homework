# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле,
# название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и
# общем времени выполнения программы.
import os.path
import time
import threading
import requests
import argparse

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
    print(f" {name_files} скачано за {time.time() - start_time} секунд")


def pars_path():
    """
    sample input url for terminal
    python home.py -p https://images.faberlic.com/images/fl/TflGoods/sm/1001347679976_16869259282.jpg
    """
    parser = argparse.ArgumentParser(prog="download image from urls")
    parser.add_argument('-p', metavar='p')
    args = parser.parse_args()
    return download(f'{args.p}')


def tread_download():
    threads = []
    for url in URL_list:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start_time = time.time()
    tread_download()
    print(f"общее время выполнения {time.time() - start_time} секунд")
