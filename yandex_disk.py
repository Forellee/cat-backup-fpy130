import requests
import logging

def create_folder(token, folder_name):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {"Authorization": f"OAuth {token}"}
    params = {"path": folder_name}

    response = requests.put(url, headers=headers, params=params)
    if response.status_code == 201:
        logging.info(f"Папка '{folder_name}' создана.")
    elif response.status_code == 409:
        logging.info(f"Папка '{folder_name}' уже существует.")
    else:
        logging.error(f"Ошибка создания папки: {response.text}")
        response.raise_for_status()

def upload_by_url(token, file_url, yandex_path):
    url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    headers = {"Authorization": f"OAuth {token}"}
    params = {"path": yandex_path, "url": file_url}

    response = requests.post(url, headers=headers, params=params)
    if response.status_code in (201, 202):
        logging.info(f"Файл '{yandex_path}' успешно загружен.")
    else:
        logging.error(f"Ошибка загрузки файла: {response.text}")
        response.raise_for_status()
