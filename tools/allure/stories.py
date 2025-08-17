from enum import Enum


class AllureStory(str, Enum):
    LOGIN = "Авторизация"

    GET_ENTITY = "Получение сущности"
    GET_ENTITIES = "Получение списка сущностей"
    CREATE_ENTITY = "Создание сущности"
    UPDATE_ENTITY = "Обновление сущности"
    DELETE_ENTITY = "Удаление сущности"
    VALIDATE_ENTITY = "Валидация сущности"