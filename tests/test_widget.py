import pytest

from src.widget import get_date, mask_account_card


def test_get_date(date_iso) -> None:
    assert get_date(date_iso) == "21.06.2026"


def test_mask_account_card() -> None:
    """Проверяет корректность работы mask_account_card"""
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert (
        mask_account_card("Visa Platinum 8990922113665229")
        == "Visa Platinum 8990 92** **** 5229"
    )


def test_mask_account_card_with_mistakes() -> None:
    """Проверяет mask_account_card на ошибку"""
    with pytest.raises(ValueError):
        assert mask_account_card("")


@pytest.mark.parametrize(
    "wrong_date",
    [
        "",
        "25.12.2024",
        "2024-13-01",
        "2024-02-30",
        "привет мир",
    ],
)
def test_get_date_errors(wrong_date) -> None:
    with pytest.raises(ValueError):
        assert get_date(wrong_date)
