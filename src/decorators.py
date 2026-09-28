from functools import wraps
from time import time


def log(filename="log.txt"):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            def write_log(message):
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(message)

            write_log(f'"{func.__name__}" запущена')

            try:
                start_time = time()
                result = func(*args, **kwargs)
                end_time = time()
                total_time = end_time - start_time
            except Exception as error:
                write_log(
                    f'"{func.__name__}" не выполнена.\n'
                    f"Ошибка: {error}.\n"
                    f"Inputs: {args}, {kwargs}\n"
                )
                raise
            else:
                write_log(
                    f'"{func.__name__}" выполнена.\n'
                    f"Результат: {result}\n"
                    f"Время на выполнение: {round(total_time, 2)}\n"
                )
                return result

        return wrapper

    return decorator
