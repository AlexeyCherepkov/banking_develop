import pandas as pd

from src.read_transactions import get_csv_data, get_excel_data


def test_get_csv_data_success(tmp_path):
    """
    Успешная работа функции
    """
    file = tmp_path / "transactions.csv"
    file.write_text(
        "id;описание;сумма\n1;Перевод;100\n2;Оплата;250\n", encoding="utf-8"
    )

    result = get_csv_data(str(file))

    assert result == [
        {"id": 1, "описание": "Перевод", "сумма": 100},
        {"id": 2, "описание": "Оплата", "сумма": 250},
    ]


def test_get_csv_data_file_not_found(tmp_path):
    """
    Файл не найден
    """
    assert get_csv_data(str(tmp_path / "missing.csv")) == []


def test_get_csv_data_wrong_encoding(tmp_path):
    """
    Неправильная кодировка
    """
    file = tmp_path / "cp1251.csv"
    file.write_bytes("id;описание\n1;Перевод\n".encode("cp1251"))

    assert get_csv_data(str(file)) == []


def test_get_excel_data_success(tmp_path):
    """
    Успешная работа функции
    """
    file = tmp_path / "transactions_excel.xlsx"
    pd.DataFrame(
        [
            {"id": 1, "описание": "Перевод", "сумма": 100},
            {"id": 2, "описание": "Оплата", "сумма": 250},
        ]
    ).to_excel(file, index=False)

    result = get_excel_data(str(file))

    assert result == [
        {"id": 1, "описание": "Перевод", "сумма": 100},
        {"id": 2, "описание": "Оплата", "сумма": 250},
    ]


def test_get_excel_data_file_not_found(tmp_path):
    """
    Файл не найден
    """
    assert get_excel_data(str(tmp_path / "missing.xlsx")) == []
