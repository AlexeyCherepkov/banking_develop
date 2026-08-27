import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(data_list) -> None:
    """Проверка корректной работы filter_by_state"""
    assert filter_by_state(data_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_another_key(data_list) -> None:
    """Проверка работы filter_by_state с другим ключем"""
    assert filter_by_state(data_list, key="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_empty_list() -> None:
    """Проверка работы filter_by_state с пустым списком"""
    assert filter_by_state([]) == []


@pytest.mark.parametrize(
    "key, count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 2),
    ],
)
def test_filter_by_state_parametrize(data_list, key, count) -> None:
    assert len(filter_by_state(data_list, key)) == count


def test_sort_by_date(data_list) -> None:
    """Проверка корректной работы sort_by_date"""
    assert sort_by_date(data_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_same_date(data_list_same_data) -> None:
    """Проверка sort_by_date с одинаковыми датами"""
    assert sort_by_date(data_list_same_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sort_by_date_wrong_date(data_list_wrong_data) -> None:
    """Проверка sort_by_date с неверной датой"""
    with pytest.raises(ValueError):
        assert sort_by_date(data_list_wrong_data)
