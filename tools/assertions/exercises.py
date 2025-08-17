from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    ExerciseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, GetExercisesResponseSchema, \
    UpdateExerciseResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response
import allure
from tools.logger import get_logger

logger = get_logger("EXERCISES_ASSERTIONS")


@allure.step("Проверить задание")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные задания соответствуют ожидаемым.

    :param actual: Фактические данные задания.
    :param expected: Ожидаемые данные задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Проверка задания")

    assert_equal(actual.id, expected.id, "exercise_id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


@allure.step("Проверить ответ на создание задания")
def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        response: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на создание задания соответствует отправленному запросу.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API с данными о созданном задании.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Проверка ответа на создание задания")

    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")


@allure.step("Проверить ответ на получение задания")
def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение задания идентичен ответу при его создании.

    :param get_exercise_response: Ответ API при запросе данных задания.
    :param create_exercise_response: Ответ API при создании задания.
    :raises AssertionError: Если данные задания не совпадают.
    """
    logger.info("Проверка ответа на получение задания")

    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)


@allure.step("Проверить ответ на обновление задания")
def assert_update_exercise_response(
        request: UpdateExerciseRequestSchema,
        response: UpdateExerciseResponseSchema
):
    """
    Проверяет, что ответ на обновление задания соответствует данным из запроса.

    :param request: Исходный запрос на обновление задания.
    :param response: Ответ API с обновлёнными данными задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    logger.info("Проверка ответа на обновление задания")

    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")


@allure.step("Проверить ответ: задание не найдено")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Проверяет, что ответ API соответствует ошибке «Задание не найдено».

    :param actual: Фактический ответ от сервера.
    :raises AssertionError: Если ответ не соответствует ошибке "Exercise not found".
    """
    logger.info("Проверка ответа: задание не найдено")

    expected = InternalErrorResponseSchema(detail="Exercise not found")
    assert_internal_error_response(actual, expected)


@allure.step("Проверить ответ на получение списка заданий")
def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_responses: list[CreateExerciseResponseSchema]
):
    """
    Проверяет, что ответ на получение списка заданий содержит те же данные, что и при их создании.

    :param get_exercises_response: Ответ API при запросе списка заданий.
    :param create_exercise_responses: Список ответов от API при создании заданий.
    :raises AssertionError: Если количество или данные заданий не совпадают.
    """
    logger.info("Проверка ответа на получение списка заданий")

    assert_length(get_exercises_response.exercises, create_exercise_responses, "exercises")

    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)