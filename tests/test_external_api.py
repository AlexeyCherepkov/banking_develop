from unittest.mock import patch

import pytest

from src.external_api import currency_conversion

transaction = {
    "id": 179194306,
    "state": "EXECUTED",
    "date": "2019-05-19T12:51:49.023880",
    "operationAmount": {
        "amount": "6381.58",
        "currency": {"name": "USD", "code": "USD"},
    },
    "description": "Перевод организации",
    "from": "МИР 5211277418228469",
    "to": "Счет 58518872592028002662",
}


@patch("requests.get")
def test_conversion_from_usd(mock_get):
    """Тест запроса API"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 100.0}
    result = currency_conversion(transaction)
    assert result == 100.0


@patch("requests.get")
def test_conversion_rub(mock_get):
    """Тест без запроса API"""
    transaction_rub = {"operationAmount": {"amount": 100, "currency": {"code": "RUB"}}}
    assert currency_conversion(transaction_rub) == 100
    mock_get.assert_not_called()


@patch("requests.get")
def test_conversion_api_error(mock_get):
    """Если API не отвечает кодом 200"""
    mock_get.return_value.status_code = 500
    with pytest.raises(ValueError, match="Convert failed"):
        currency_conversion(transaction)
