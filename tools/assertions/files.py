import allure

from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema, InternalErrorResponseSchema
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema, \
    GetFileResponseSchema
from config import settings
from tools.assertions.base import assert_equal
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response
from tools.logger import get_logger

logger = get_logger("FILES_ASSERTIONS")


@allure.step("Проверить ответ на создание файла")
def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на создание файла соответствует отправленному запросу.

    :param request: Исходный запрос на создание файла.
    :param response: Ответ API с данными о созданном файле.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Проверка ответа на создание файла")

    expected_url = f"{settings.http_client.client_url}static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")


@allure.step("Проверить файл")
def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Проверяет, что фактические данные файла совпадают с ожидаемыми.

    :param actual: Фактические данные файла.
    :param expected: Ожидаемые данные файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Проверка файла")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")


@allure.step("Проверить ответ на получение файла")
def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    """
    Проверяет, что ответ на получение файла идентичен ответу при его создании.

    :param get_file_response: Ответ API при запросе данных файла.
    :param create_file_response: Ответ API при создании файла.
    :raises AssertionError: Если данные файла не совпадают.
    """
    logger.info("Проверка ответа на получение файла")

    assert_file(get_file_response.file, create_file_response.file)


@allure.step("Проверить ответ при создании файла с пустым именем")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на попытку создания файла с пустым именем соответствует ожидаемой ошибке валидации.

    :param actual: Ответ от API с ошибкой валидации.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Проверка ответа при создании файла с пустым именем")

    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "filename"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)


@allure.step("Проверить ответ при создании файла с пустой директорией")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на попытку создания файла с пустой директорией соответствует ожидаемой ошибке валидации.

    :param actual: Ответ от API с ошибкой валидации.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Проверка ответа при создании файла с пустой директорией")

    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "directory"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)


@allure.step("Проверить ответ: файл не найден")
def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    Проверяет, что ответ API соответствует ошибке «Файл не найден».

    :param actual: Фактический ответ от сервера.
    :raises AssertionError: Если ответ не соответствует ошибке «File not found».
    """
    logger.info("Проверка ответа: файл не найден")

    expected = InternalErrorResponseSchema(
        details="File not found"  # ← реальное имя поля
    )
    assert_internal_error_response(actual, expected)


@allure.step("Проверить ответ при запросе файла с некорректным ID")
def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на запрос файла с некорректным UUID соответствует ожидаемой ошибке валидации.

    :param actual: Ответ от API с ошибкой валидации.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    logger.info("Проверка ответа при запросе файла с некорректным ID")

    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="uuid_parsing",
                input="incorrect-file-id",
                context={
                    "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
                },
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                location=["path", "file_id"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)