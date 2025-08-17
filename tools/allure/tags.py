from enum import Enum


class AllureTag(str, Enum):
    USERS = "Пользователи"
    FILES = "Файлы"
    COURSES = "Курсы"
    EXERCISES = "Задания"
    REGRESSION = "Регрессия"
    AUTHENTICATION = "Аутентификация"

    GET_ENTITY = "Получение сущности"
    GET_ENTITIES = "Получение списка сущностей"
    CREATE_ENTITY = "Создание сущности"
    UPDATE_ENTITY = "Обновление сущности"
    DELETE_ENTITY = "Удаление сущности"
    VALIDATE_ENTITY = "Валидация сущности"
