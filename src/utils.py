import json
import os

BASE_DIR = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "data", "operations.json")


def get_data(track="") -> list[dict]:
    """
    Считывает файл 'operation.json' из папки 'data' и десериализирует его
    """
    with open(track, "r", encoding="utf-8") as file:
        return json.load(file)
