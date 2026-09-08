from typing import Any, Generator


def filter_by_currency(data: list[dict], key: str = "USD") -> Generator[dict[str, Any]]:
    """Генератор, фильтрующий данные по валюте"""
    for item in data:
        if item["operationAmount"]["currency"]["code"] == key:
            yield item


def transaction_descriptions(data: list[dict]):
    """Генератор, выдающий описание транзакции"""
    for item in data:
        description = item.get("description")
        yield description


def card_number_generator(start_num: int | str, end_num: int | str) -> Generator[str]:
    """Генерирует номера карт в определённом диапазоне"""
    if len(str(end_num)) > 16:
        raise (ValueError("Конечный предел диапазона превышает длинну карты (16 цифр)"))
    elif int(start_num) >= int(end_num):
        raise (ValueError("Стартовый диапазон меньше конечного"))
    else:
        for num in range(int(start_num), int(end_num) + 1):
            str_num = str(num)
            while len(str_num) < 16:
                str_num = "0" + str_num
            yield str_num[:4] + " " + str_num[4:8] + " " + str_num[
                8:12
            ] + " " + str_num[12:]
