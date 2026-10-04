import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = str(os.getenv("API_KEY"))


def currency_conversion(transaction: dict) -> int | float:
    """
    Обращаясь к Exchange Rates Data API, переводит сумму транзакции в рубли
    """
    try:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            return transaction["operationAmount"]["amount"]
        else:
            currency = transaction["operationAmount"]["currency"]["code"]
            amount = transaction["operationAmount"]["amount"]
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

            headers = {"apikey": API_KEY}

            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                raise ValueError("Convert failed")
            data = response.json()
            return float(data["result"])
    except KeyError:
        raise KeyError("Missing key")
