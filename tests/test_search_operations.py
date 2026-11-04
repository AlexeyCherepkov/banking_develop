import pytest

from src.search_operations import process_bank_operations, process_bank_search


@pytest.fixture
def operations():
    return [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод со счета на счет"},
        {"id": 3, "description": "Перевод с карты на карту"},
        {"id": 4, "description": "Открытие вклада"},
    ]


def test_counts_categories(operations):
    result = process_bank_operations(operations, ["Перевод", "Открытие вклада"])
    assert result == {"Перевод": 3, "Открытие вклада": 1}


def test_category_not_found(operations):
    assert process_bank_operations(operations, ["Кредит"]) == {"Кредит": 0}


def test_empty_data():
    assert process_bank_operations([], ["Перевод"]) == {"Перевод": 0}


def test_empty_categories(operations):
    assert process_bank_operations(operations, []) == {}


@pytest.fixture
def operations_search():
    return [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод со счета на счет"},
        {"id": 3, "description": "Перевод с карты на карту"},
        {"id": 4, "description": "Открытие вклада"},
    ]


def test_finds_matching_operations(operations_search):
    result = process_bank_search(operations_search, "Перевод")
    assert [op["id"] for op in result] == [1, 2, 3]


def test_returns_original_dicts(operations_search):
    result = process_bank_search(operations_search, "вклада")
    assert result == [operations_search[3]]
    assert result[0] is operations_search[3]


def test_no_matches(operations_search):
    assert process_bank_search(operations_search, "Кредит") == []


def test_empty_data_search():
    assert process_bank_search([], "Перевод") == []
