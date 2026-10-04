import logging
import os

BASE_DIR = str(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOG_PATH = os.path.join(BASE_DIR, "logs", "masks.log")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s %(funcName)s %(levelname)s: %(message)s",
    filename=LOG_PATH,
    filemode="w",
)
logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: int | str) -> str:
    logger.info("Start")
    """
    Функция маскирует номер карты и разбивает ее на блоки по 4 символа
    принимает значение из 16 символов
    """
    try:
        str_card_number = str(card_number)
        if len(str_card_number) != 16 or not str_card_number.isdigit():
            logger.error("Wrong card number")
            raise ValueError("Неверно введены данные карты")

        masked_number = (
            f"{str_card_number[:4]} "
            f"{str_card_number[4:6]}** **** "
            f"{str_card_number[12:]}"
        )
        logger.info("Card number has been masked")
        return masked_number
    finally:
        logger.info("End")


def get_mask_account(account_number: int | str) -> str:
    logger.info("Start")
    """
    Функция маскирует номер аккаунта и возвращает последние 4 символа
    принимает значение из 20 символов
    """
    try:
        str_account_number = str(account_number)
        if len(str_account_number) >= 4:
            masked_number = f"**{str_account_number[-4:]}"
            logger.info("Account number has been masked")
            return masked_number
        else:
            logger.error("Wrong account number")
            raise ValueError("Неверно введены данные аккаунта")
    finally:
        logger.info("End")
