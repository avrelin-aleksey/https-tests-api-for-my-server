import allure
from clients.users.users_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetUserResponseSchema,
    UserSchema
)
from tools.assertions.base import assert_equal
from tools.logger import get_logger

logger = get_logger("USERS_ASSERTIONS")


def assert_create_user_response(
        request: CreateUserRequestSchema,
        response: CreateUserResponseSchema
) -> None:
    """
    Проверяет соответствие ответа о создании пользователя исходному запросу.

    Args:
        request: Запрос на создание пользователя
        response: Ответ API с данными созданного пользователя

    Raises:
        AssertionError: Если данные не соответствуют запросу
    """
    with allure.step("Проверить ответ на создание пользователя"):
        logger.info("Проверяем ответ на создание пользователя")

        assert_equal(response.user.email, request.email, "Email пользователя")
        assert_equal(response.user.last_name, request.last_name, "Фамилия")
        assert_equal(response.user.first_name, request.first_name, "Имя")
        assert_equal(response.user.middle_name, request.middle_name, "Отчество")


def assert_user(
        actual: UserSchema,
        expected: UserSchema
) -> None:
    """
    Проверяет соответствие данных пользователя ожидаемым значениям.

    Args:
        actual: Фактические данные пользователя
        expected: Ожидаемые данные пользователя

    Raises:
        AssertionError: Если данные не совпадают
    """
    with allure.step("Проверить данные пользователя"):
        logger.info("Проверяем данные пользователя")

        assert_equal(actual.id, expected.id, "ID пользователя")
        assert_equal(actual.email, expected.email, "Email")
        assert_equal(actual.last_name, expected.last_name, "Фамилия")
        assert_equal(actual.first_name, expected.first_name, "Имя")
        assert_equal(actual.middle_name, expected.middle_name, "Отчество")


def assert_get_user_response(
        get_user_response: GetUserResponseSchema,
        create_user_response: CreateUserResponseSchema
) -> None:
    """
    Проверяет соответствие полученных данных пользователя данным его создания.

    Args:
        get_user_response: Ответ с данными пользователя
        create_user_response: Данные создания пользователя

    Raises:
        AssertionError: Если данные не совпадают
    """
    with allure.step("Проверить полученные данные пользователя"):
        logger.info("Проверяем полученные данные пользователя")
        assert_user(get_user_response.user, create_user_response.user)
