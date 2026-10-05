import json
import logging
import os

BASE_DIR = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "data", "operations.json")
LOG_PATH = os.path.join(BASE_DIR, "logs", "utils.log")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s",
    filename=LOG_PATH,
    filemode="w",
)
logger = logging.getLogger(__name__)


def get_data(track=DATA_PATH) -> list[dict]:
    """
    Считывает файл 'operation.json' из папки 'data' и десериализирует его
    """
    logger.info("Start")
    try:
        with open(track, "r", encoding="utf-8") as file:
            data = json.load(file)
        logger.info("Load completed")
        return data

    except FileNotFoundError:
        logger.error("File not found")
        return []

    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in {e}")
        return []

    finally:
        logger.info("End")
