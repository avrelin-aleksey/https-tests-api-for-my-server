from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, CourseSchema, \
    GetCoursesResponseSchema, CreateCourseResponseSchema, CreateCourseRequestSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user
import allure
from tools.logger import get_logger

logger = get_logger("COURSES_ASSERTIONS")


def assert_update_course_response(
        request: UpdateCourseRequestSchema,
        response: UpdateCourseResponseSchema
):
    """
    Проверяет соответствие ответа обновления курса исходному запросу.

    Args:
        request: Запрос на обновление курса
        response: Ответ API с обновленными данными

    Raises:
        AssertionError: Если данные не соответствуют
    """
    with allure.step("Проверить ответ обновления курса"):
        logger.info("Проверяем ответ обновления курса")

        assert_equal(response.course.title, request.title, "Название курса")
        assert_equal(response.course.max_score, request.max_score, "Максимальный балл")
        assert_equal(response.course.min_score, request.min_score, "Минимальный балл")
        assert_equal(response.course.description, request.description, "Описание")
        assert_equal(response.course.estimated_time, request.estimated_time, "Расчетное время")


def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    Проверяет соответствие данных курса ожидаемым значениям.

    Args:
        actual: Фактические данные курса
        expected: Ожидаемые данные курса

    Raises:
        AssertionError: Если данные не совпадают
    """
    with allure.step("Проверить данные курса"):
        logger.info("Проверяем данные курса")

        assert_equal(actual.id, expected.id, "ID курса")
        assert_equal(actual.title, expected.title, "Название")
        assert_equal(actual.max_score, expected.max_score, "Макс. балл")
        assert_equal(actual.min_score, expected.min_score, "Мин. балл")
        assert_equal(actual.description, expected.description, "Описание")
        assert_equal(actual.estimated_time, expected.estimated_time, "Время прохождения")

        with allure.step("Проверить превью курса"):
            assert_file(actual.preview_file, expected.preview_file)

        with allure.step("Проверить создателя курса"):
            assert_user(actual.created_by_user, expected.created_by_user)


def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_responses: list[CreateCourseResponseSchema]
):
    """
    Проверяет соответствие списка курсов данным их создания.

    Args:
        get_courses_response: Ответ со списком курсов
        create_course_responses: Данные создания курсов

    Raises:
        AssertionError: Если списки не соответствуют
    """
    with allure.step("Проверить список курсов"):
        logger.info("Проверяем список курсов")

        assert_length(get_courses_response.courses, create_course_responses, "Количество курсов")

        for index, create_course_response in enumerate(create_course_responses):
            with allure.step(f"Проверить курс #{index + 1}"):
                assert_course(get_courses_response.courses[index], create_course_response.course)


def assert_create_course_response(
        request: CreateCourseRequestSchema,
        response: CreateCourseResponseSchema
):
    """
    Проверяет соответствие созданного курса исходному запросу.

    Args:
        request: Запрос на создание курса
        response: Ответ API с созданным курсом

    Raises:
        AssertionError: Если данные не соответствуют
    """
    with allure.step("Проверить созданный курс"):
        logger.info("Проверяем созданный курс")

        assert_equal(response.course.title, request.title, "Название")
        assert_equal(response.course.max_score, request.max_score, "Макс. балл")
        assert_equal(response.course.min_score, request.min_score, "Мин. балл")
        assert_equal(response.course.description, request.description, "Описание")
        assert_equal(response.course.estimated_time, request.estimated_time, "Время прохождения")

        with allure.step("Проверить превью курса"):
            assert_equal(response.course.preview_file.id, request.preview_file_id, "ID превью")

        with allure.step("Проверить создателя курса"):
            assert_equal(response.course.created_by_user.id, request.created_by_user_id, "ID создателя")