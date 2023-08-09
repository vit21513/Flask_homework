import argparse
import asyncio

import aiofiles
# асинхронный модуль для получения информации из сети интернет (асинхронный аналог requests
import aiohttp
import time
import os
import os
import time

URL_list = ["https://static.gismeteo.st/assets/maps/n_prc.png",
            "https://faberlic.com/images/flippingbook/2023/Catalog_11/RU/cat-001.jpg",
            "https://faberlic.com/images/flippingbook/2023/Russia_Wallness_23/cat-001.jpg",
            "https://images.faberlic.com/images/fl/TflGoods/sm/1001347679976_16869259282.jpg",
            "https://images.faberlic.com/images/fl/TflGoods/sm/1001347679972_16893426293.jpg"]


async def download(url_img, dir_name='download'):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url_img) as response:
            if response.status == 200:
                content = await response.read()
    *_, name_files, = url_img.split("/")
    path_folder = os.path.join(dir_name, name_files)
    async with aiofiles.open(path_folder, 'wb') as f:
        await f.write(content)
    print(f"скачано за {time.time() - start_time} секунд")


def pars_path():
    """
    sample input url for terminal
    python home.py -p https://images.faberlic.com/images/fl/TflGoods/sm/1001347679976_16869259282.jpg
    """
    parser = argparse.ArgumentParser(prog="download image from urls")
    parser.add_argument('-p', metavar='p')
    args = parser.parse_args()
    return download(f'{args.p}')


async def main():
    tasks = []
    for url in URL_list:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f"Всего за {time.time() - start_time} секунд")