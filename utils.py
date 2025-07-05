import requests
import json

def get_file_size(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        return int(response.headers.get("Content-Length", 0))
    except requests.RequestException as e:
        print(f"Ошибка при получении размера: {e}")
        return 0


def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
