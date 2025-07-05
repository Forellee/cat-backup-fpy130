from cataas_api import get_cat_image_url
from yandex_disk import create_folder, upload_by_url
from utils import save_json, get_file_size
import logging

logging.basicConfig(level=logging.INFO)


def main():
    group_name = "FPY-130"
    text = input("Введите текст для картинки: ").strip()
    token = input("Введите токен Яндекс.Диска: ").strip()

    logging.info("Получение URL картинки с сайта cataas.com...")
    image_url = get_cat_image_url(text)

    create_folder(token, group_name)
    filename = f"{text}.jpg"
    yandex_path = f"{group_name}/{filename}"

    logging.info(f"Загрузка {filename} на Яндекс.Диск...")
    upload_by_url(token, image_url, yandex_path)

    size = get_file_size(image_url)
    save_json({"filename": filename, "size_bytes": size}, "result.json")
    logging.info("Файл успешно загружен и информация сохранена в result.json.")


if __name__ == "__main__":
    main()
    