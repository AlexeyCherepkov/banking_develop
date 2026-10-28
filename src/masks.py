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
    """
    Функция маскирует номер карты и разбивает ее на блоки по 4 символа
    принимает значение из 16 символов
    """
    logger.info("Start")
    try:
        str_card_number = str(card_number)

        if not str_card_number.isdigit():
            logger.error("Card number contains non-digit characters")
            raise ValueError("Неверно введены данные карты")

        if len(str_card_number) != 16:
            logger.error(f"Wrong card number length: {len(str_card_number)}")
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
    """
    Функция маскирует номер аккаунта и возвращает последние 4 символа
    принимает значение из 20 символов
    """
    logger.info("Start")
    try:
        str_account_number = str(account_number)

        if not str_account_number.isdigit():
            logger.error("Account number contains non-digit characters")
            raise ValueError("Неверно введены данные аккаунта")

        if len(str_account_number) != 20:
            logger.error(f"Wrong account number length: {len(str_account_number)}")
            raise ValueError("Неверно введены данные аккаунта")

        masked_number = f"**{str_account_number[-4:]}"
        logger.info("Account number has been masked")
        return masked_number
    finally:
        logger.info("End")
