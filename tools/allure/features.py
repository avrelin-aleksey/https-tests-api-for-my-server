from enum import Enum


class AllureFeature(str, Enum):
    USERS = "Пользователи"
    FILES = "Файлы"
    COURSES = "Курсы"
    EXERCISES = "Задания"
    AUTHENTICATION = "Аутентификация"