import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


def test_filter_by_currency(
    transactions_data, correct_filter_by_currency_1, correct_filter_by_currency_2
) -> None:
    """Тест работы filter_by_currency"""
    generator_filter_by_currency = filter_by_currency(transactions_data)
    assert next(generator_filter_by_currency) == correct_filter_by_currency_1
    assert next(generator_filter_by_currency) == correct_filter_by_currency_2


@pytest.mark.parametrize(
    "key, count",
    [
        ("USD", 3),
        ("EUR", 0),
    ],
)
def test_filter_by_currency_rather_currency(transactions_data, key, count):
    """Тест filter_by_currency по валютам USD и EUR(Отсутвующий ключ)"""
    generator = filter_by_currency(transactions_data, key)
    assert len(list(generator)) == count


def test_filter_by_currency_empty_data() -> None:
    """Тест filter_by_currency с отсутствующими данными"""
    generator = list(filter_by_currency([]))
    assert generator == []


def test_transaction_descriptions(transactions_data) -> None:
    """Тест работы transaction_description"""
    generator = transaction_descriptions(transactions_data)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"


def test_transaction_description_empty_data() -> None:
    """Тест работы transaction_descriptions с пустыми вводными данными"""
    generator = transaction_descriptions([])
    assert len(list(generator)) == 0


def test_card_number_generator() -> None:
    """Тест работы card_number_generator"""
    generator = card_number_generator(0, 5)
    assert next(generator) == "0000 0000 0000 0000"
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"


@pytest.mark.parametrize(
    "min_number, max_number, total",
    [(0, 1999, 2000), (9999999999999000, 9999999999999999, 1000)],
)
def test_card_number_generator_parametrize(min_number, max_number, total) -> None:
    """Тест работы card_number_generator"""
    generator = card_number_generator(min_number, max_number)
    assert len(list(generator)) == total
