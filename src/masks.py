def get_mask_card_number(card_number: int | str) -> str:
    """
    Функция маскирует номер карты и разбивает ее на блоки по 4 символа
    принимает значение из 16 символов
    """
    str_card_number = str(card_number)
    if len(str_card_number) == 16:
        masked_number = (
            str_card_number[:4]
            + " "
            + str_card_number[4:6]
            + "** **** "
            + str_card_number[12:]
        )
        return masked_number
    else:
        raise ValueError("Неверно введены данные карты")


def get_mask_account(account_number: int | str) -> str:
    """
    Функция маскирует номер аккаунта и возвращает последние 4 символа
    принимает значение из 20 символов
    """
    str_account_number = str(account_number)
    if len(str_account_number) >= 4:
        masked_number = "**" + str_account_number[-4:]
        return masked_number
    else:
        raise ValueError("Неверно введены данные аккаунта")
