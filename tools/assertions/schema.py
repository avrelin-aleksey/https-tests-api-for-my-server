from typing import Any

from jsonschema import validate
from jsonschema.validators import Draft202012Validator
import allure
from tools.logger import get_logger

logger = get_logger("SCHEMA_ASSERTIONS")


@allure.step("Проверка соответствия JSON-схеме")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Проверяет, соответствует ли JSON-объект (instance) указанной JSON-схеме (schema).

    :param instance: JSON-данные, которые необходимо проверить.
    :param schema: Ожидаемая схема в формате JSON Schema.
    :raises jsonschema.exceptions.ValidationError: Если объект не соответствует схеме.
    """
    logger.info("Проверка соответствия JSON-схеме")

    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )