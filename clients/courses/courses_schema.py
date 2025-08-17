from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


# Базовая модель для всех, кто работает с API
class ApiBaseModel(BaseModel):
    """
    Базовая Pydantic-модель для интеграции с API.
    Обеспечивает автоматическое преобразование snake_case ↔ camelCase,
    а также общие настройки валидации и сериализации.
    """
    model_config = ConfigDict(
        populate_by_name=True,           # Позволяет инициализировать модель через snake_case или camelCase
        alias_generator=to_camel,        # Автоматически конвертирует поля в camelCase при сериализации/десериализации
        str_strip_whitespace=True,       # Удаляет лишние пробелы в строках
        validate_default=True,           # Валидирует значения по умолчанию при создании
        validate_assignment=True,        # Валидирует поля при изменении
    )


class CourseSchema(ApiBaseModel):
    """
    Схема данных курса, возвращаемая API.

    Используется в ответах:
    - GET /courses
    - GET /courses/{id}
    - POST /courses
    - PATCH /courses/{id}
    """
    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    preview_file: FileSchema
    estimated_time: str
    created_by_user: UserSchema


class GetCoursesQuerySchema(ApiBaseModel):
    """
    Схема параметров запроса для получения списка курсов.

    Пример запроса:
    GET /courses?userId=abc123
    """
    user_id: str


class GetCoursesResponseSchema(ApiBaseModel):
    """
    Схема ответа на запрос списка курсов.

    Пример тела ответа:
    {
      "courses": [
        { "id": "...", "title": "...", "maxScore": 100, ... }
      ]
    }
    """
    courses: list[CourseSchema]


class CreateCourseRequestSchema(ApiBaseModel):
    """
    Схема тела запроса для создания нового курса.

    Все поля заполняются фейкером по умолчанию для удобства тестирования.
    При вызове можно переопределить любое поле.
    """
    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(default_factory=fake.max_score)
    min_score: int = Field(default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    preview_file_id: str = Field(default_factory=fake.uuid4)
    estimated_time: str = Field(default_factory=fake.estimated_time)
    created_by_user_id: str = Field(default_factory=fake.uuid4)


class CreateCourseResponseSchema(ApiBaseModel):
    """
    Схема ответа при успешном создании курса.

    Пример:
    {
      "course": { "id": "abc123", "title": "...", "maxScore": 100, ... }
    }
    """
    course: CourseSchema


class UpdateCourseRequestSchema(ApiBaseModel):
    """
    Схема тела запроса для частичного обновления курса.

    Все поля опциональны (Optional), так как обновление — частичное (PATCH).
    Значения по умолчанию из фейкера нужны только для удобства тестов.
    """
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score)
    min_score: int | None = Field(default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(default_factory=fake.estimated_time)


class UpdateCourseResponseSchema(ApiBaseModel):
    """
    Схема ответа при успешном обновлении курса.

    Возвращает полные данные обновлённого курса.
    """
    course: CourseSchema