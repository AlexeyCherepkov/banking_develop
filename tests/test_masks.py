import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_card_number() -> None:
    """Тестирует корректность работы get_mask_card_number"""
    assert get_mask_card_number(1234123412341234) == "1234 12** **** 1234"
    assert get_mask_card_number("1234123412341234") == "1234 12** **** 1234"


def test_wrong_card_numbers(wrong_card_number) -> None:
    """Тестирует работу с неправильными данными get_mask_card_number"""
    with pytest.raises(ValueError):
        assert get_mask_card_number(wrong_card_number)


def test_account_number() -> None:
    """Тестирует корректность работы get_mask_account"""
    assert get_mask_account(12345678901234567890) == "**7890"
    assert get_mask_account("12345678901234567890") == "**7890"


def test_wrong_account_numbers(wrong_account_number) -> None:
    """Тестирует работы с неправильными данными get_mask_account"""
    with pytest.raises(ValueError):
        assert get_mask_account(wrong_account_number)
