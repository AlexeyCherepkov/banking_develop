import re
from typing import Any


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Поиск всех операций по определенной транзакции
    """
    pattern = re.compile(search, re.IGNORECASE)
    result = []
    for operation in data:
        if operation:
            description = operation.get("description")
            if isinstance(description, str) and pattern.search(description):
                result.append(operation)
    return result


def process_bank_operations(
    data: list[dict[str, Any]], categories: list[str]
) -> dict[str, int]:
    """
    Количество определенных категорий в операциях
    """
    result = {}
    for category in categories:
        pattern = re.compile(category)
        result[category] = 0
        for operation in data:
            if operation:
                description = operation.get("description")
                if isinstance(description, str) and pattern.search(description):
                    result[category] += 1
    return result
