from datetime import datetime
from typing import Any


def filter_by_state(data_list: list[dict[str, Any]], key="EXECUTED") -> list:
    """
    Исключает из списка по ключу state
    """
    result = []
    for i in data_list:
        if i["state"] == key:
            result.append(i)
    return result


def sort_by_date(
    data_list: list[dict[str, Any]], sort_parameter=True
) -> list[dict[str, Any]] | None:
    """
    Сортирует список по ключу date
    """
    for i in data_list:
        try:
            datetime.fromisoformat(i["date"])
            result = sorted(data_list, key=lambda x: x["date"], reverse=sort_parameter)
            return result
        except ValueError:
            raise ValueError("Неверная дата")
    return None
