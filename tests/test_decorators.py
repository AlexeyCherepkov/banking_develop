import pytest

from src.decorators import log


def test_log():
    @log(filename=None)
    def add(a, b):
        return a + b

    result = add(1, 2)
    assert result == 3


def test_log_error() -> None:
    @log(filename=None)
    def division_zero():
        return 1 / 0

    with pytest.raises(ZeroDivisionError):
        assert division_zero()


def test_log_without_file(capsys) -> None:
    @log(filename=None)
    def add(a, b):
        return a + b

    result = add(1, 2)
    captured = capsys.readouterr()

    assert result == 3
    assert '"add" запущена' in captured.out
    assert '"add" выполнена.' in captured.out
    assert "Результат: 3" in captured.out
