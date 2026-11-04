from datetime import datetime
from typing import Any


def filter_by_state(data_list: list[dict[str, Any]], key="EXECUTED") -> list:
    """
    Исключает из списка по ключу state
    """
    result = []
    for operation in data_list:
        if operation:
            state = operation.get("state")
            if isinstance(state, str) and state == key:
                result.append(operation)
    return result


def sort_by_date(
    data_list: list[dict[str, Any]], sort_parameter: bool = True
) -> list[dict[str, Any]]:
    """
    Сортирует список по ключу date
    """
    for item in data_list:
        try:
            datetime.fromisoformat(item["date"])
        except ValueError:
            raise ValueError("Неверная дата")

    return sorted(data_list, key=lambda x: x["date"], reverse=sort_parameter)
