import pytest


@pytest.fixture
def wrong_card_number() -> int:
    """Возвращает неверный номер карты"""
    return 1


@pytest.fixture
def wrong_account_number() -> int:
    """Возвращается неверный номер аккаунта"""
    return 1


@pytest.fixture
def date_iso() -> str:
    return "2026-06-21"


@pytest.fixture
def data_list() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def data_list_same_data() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def data_list_wrong_data() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "гггг-мм-дд"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
