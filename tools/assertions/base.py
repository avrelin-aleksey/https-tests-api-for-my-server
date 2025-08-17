from typing import Any, Sized

import allure

from tools.logger import get_logger

logger = get_logger("BASE_ASSERTIONS")


def assert_status_code(actual: int, expected: int):
    """
    Проверяет, что фактический статус-код ответа соответствует ожидаемому.

    :param actual: Фактический статус-код ответа.
    :param expected: Ожидаемый статус-код.
    :raises AssertionError: Если статус-коды не совпадают.
    """
    with allure.step(f"Проверить, что статус код ответа равен {expected}"):
        logger.info(f"Проверяем, что статус код ответа равен {expected}")

        assert actual == expected, (
            'Неверный статус код ответа. '
            f'Ожидалось: {expected}. '
            f'Фактически: {actual}'
        )



def assert_equal(actual: Any, expected: Any, name: str):
    """
    Проверяет, что фактическое значение равно ожидаемому.

    :param actual: Фактическое значение.
    :param expected: Ожидаемое значение.
    :param name: Название поля для отображения в отчёте (например, 'id', 'url').
    :raises AssertionError: Если значения не совпадают.
    """
    with allure.step(f"Проверить, что '{name}' равно {expected}"):
        logger.info(f'Проверяем, что "{name}" равно {expected}')

        assert actual == expected, (
            f'Неверное значение параметра: "{name}". '
            f'Ожидалось: {expected}. '
            f'Фактически: {actual}'
        )


def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    with allure.step(f"Проверить, что '{name}' равно True"):
        logger.info(f'Проверяем, что "{name}" равно True')

        assert actual, (
            f'Неверное значение параметра: "{name}". '
            f'Ожидалось True, но получено: {actual}'
        )


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """

    with allure.step(f"Проверить, что длина '{name}' равна {len(expected)}"):
        logger.info(f'Проверяем, что длина "{name}" равна {len(expected)}')

        assert len(actual) == len(expected), (
            f'Неверная длина объекта: "{name}". '
            f'Ожидалась: {len(expected)}. '
            f'Фактически: {len(actual)}'
        )
