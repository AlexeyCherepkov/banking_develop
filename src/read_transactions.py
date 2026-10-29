import logging
import os

import pandas as pd

BASE_DIR = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH_CSV = os.path.join(BASE_DIR, "data", "transactions.csv")
DATA_PATH_EXCEL = os.path.join(BASE_DIR, "data", "transactions_excel.xlsx")
LOG_PATH = os.path.join(BASE_DIR, "logs", "read_transactions.log")


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s",
    filename=LOG_PATH,
    filemode="w",
)
logger = logging.getLogger(__name__)


def get_csv_data(track: str = DATA_PATH_CSV) -> list[dict]:
    """
    Считывает данные из файла transactions.csv
    """
    logger.info("Start")
    try:
        csv_data = pd.read_csv(track, encoding="utf-8", sep=";")
        result = csv_data.to_dict(orient="records")

    except UnicodeDecodeError:
        logger.error("Not an UTF-8")
        return []

    except FileNotFoundError:
        logger.error("File not found")
        return []

    finally:
        logger.info("End")

    return result


def get_excel_data(track: str = DATA_PATH_EXCEL) -> list[dict]:
    """
    Считывает данные из файла transactions_excel.xlsx
    """
    logger.info("Start")
    try:
        excel_data = pd.read_excel(track)
        result = excel_data.to_dict(orient="records")

    except FileNotFoundError:
        logger.error("File not found")
        return []

    finally:
        logger.info("End")

    return result
