from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Функция маскирует номер счета или карты
    """
    number = ""
    account_card_data = ""

    for i in data:
        if i.isdigit():
            number += i
        else:
            account_card_data += i

    if len(number) == 16:
        masked_number = get_mask_card_number(number)
    else:
        masked_number = get_mask_account(number)

    return account_card_data + masked_number


def get_date(str_date: str) -> str:
    """
    Функция возвращает дату в формате ДД.ММ.ГГГГ
    """
    date_format = datetime.fromisoformat(str_date)
    return date_format.strftime("%d.%m.%Y")
