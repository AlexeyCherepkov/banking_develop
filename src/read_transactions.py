import os

import pandas as pd

BASE_DIR = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH_CSV = os.path.join(BASE_DIR, "data", "transactions.csv")
DATA_PATH_EXCEL = os.path.join(BASE_DIR, "data", "transactions_excel.xlsx")


def get_csv_data(track: str = DATA_PATH_CSV) -> list[dict]:
    """
    Считывает данные из файла transactions.csv
    """
    csv_data = pd.read_csv(track, encoding="utf-8", sep=';')
    result = csv_data.to_dict(orient="records")
    return result


def get_excel_data(track: str = DATA_PATH_EXCEL) -> list[dict]:
    """
    Считывает данные из файла transactions_excel.xlsx
    """
    excel_data = pd.read_excel(track)
    result = excel_data.to_dict(orient="records")
    return result
