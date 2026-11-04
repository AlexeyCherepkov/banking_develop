from src.processing import filter_by_state, sort_by_date
from src.read_transactions import get_csv_data, get_excel_data
from src.search_operations import process_bank_search
from src.utils import get_data
from src.widget import get_date, mask_account_card


def choose_file_type() -> list[dict]:
    """
    Выбирает тип данных
    """
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")

    loaders = {
        "1": get_data,
        "2": get_csv_data,
        "3": get_excel_data,
    }

    while True:
        choice = input().strip()
        if choice in loaders:
            return loaders[choice]()
        print("Введена неверная команда. Введите цифру от 1 до 3")


def choose_transaction_status(data: list[dict]) -> list[dict]:
    """
    Выбор по статусу операции
    """
    while True:
        print("""Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        answer = input().strip().upper()
        if answer == "EXECUTED":
            data = filter_by_state(data, answer)
            break

        elif answer == "CANCELED":
            data = filter_by_state(data, answer)
            break

        elif answer == "PENDING":
            data = filter_by_state(data, answer)
            break

        else:
            print(f"Статус операции {answer} недоступен")
    return data


def sort_by_date_main(data: list[dict]) -> list[dict]:
    """
    Сортировка по дате
    возрастание / убывание
    """
    while True:
        print("Отсортировать операции по дате? Да/Нет")
        answer = input().strip().lower()

        if answer == "нет":
            return data

        elif answer == "да":
            break

        else:
            print("Неверная команда")

    while True:
        print("Отсортировать по возрастанию или по убыванию?")
        direction = input().strip().lower()

        if direction == "по возрастанию":
            return sort_by_date(data, False)

        elif direction == "по убыванию":
            return sort_by_date(data, True)

        else:
            print("Неверная команда")


def filter_by_rub_transaction(data: list[dict]) -> list[dict]:
    """
    Фильтр по рублевым транзакциям
    """
    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        answer = input().strip().lower()

        if answer == "да":
            result = []
            for transaction in data:
                currency_path = (
                    transaction.get("operationAmount", {})
                    .get("currency", {})
                    .get("code")
                )
                if currency_path is None:
                    currency_path = transaction.get("currency_code")

                if currency_path == "RUB":
                    result.append(transaction)
            return result

        elif answer == "нет":
            return data

        else:
            print("Неверная команда")


def search_by_description(data: list[dict]) -> list[dict]:
    """
    Фильтр по описанию транзакции
    """
    while True:
        print(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет"
        )
        answer = input().strip().lower()

        if answer == "да":
            answer_word = input("Введите слово\n")
            result = process_bank_search(data, answer_word)
            return result

        elif answer == "нет":
            return data


def final_message(data: list[dict]):
    """
    Итоговый вывод
    """
    if len(data) > 1:
        print("Распечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке: {len(data)}\n")

        for transaction in data:
            """Дата и описание"""
            print(f'{get_date(transaction["date"])} {transaction['description']}')

            """Откуда -> куда"""
            transaction_from = transaction.get("from", "")
            transaction_to = transaction.get("to", "")
            print(
                f"{mask_account_card(transaction_from)} -> {mask_account_card(transaction_to)}"
            )

            def get_amount_and_currency(item: dict) -> str:
                """Получение суммы и валюты"""
                operation_amount = item.get("operationAmount")

                if isinstance(operation_amount, dict):
                    amount = operation_amount.get("amount")
                    currency = operation_amount.get("currency", {}).get("code")

                else:
                    amount = item.get("amount")
                    currency = item.get("currency_code")

                return f"{amount} {currency}"

            """Сумма и валюта"""
            print(f"Сумма: {get_amount_and_currency(transaction)}\n")

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


def main():
    data_result = choose_file_type()
    data_result = choose_transaction_status(data_result)
    data_result = sort_by_date_main(data_result)
    data_result = filter_by_rub_transaction(data_result)
    data_result = search_by_description(data_result)
    final_message(data_result)


if __name__ == "__main__":
    main()
