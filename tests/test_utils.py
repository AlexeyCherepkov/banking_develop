import json
from unittest.mock import mock_open, patch

from src.utils import get_data


def test_get_data_success():
    data = [{"id": 1}]
    with patch("builtins.open", mock_open(read_data=json.dumps(data))):
        assert get_data("fake.json") == data


def test_get_data_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        assert get_data("missing.json") == []
