from enum import Enum


class AllureEpic(str, Enum):
    LMS = "Сервис LMS"
    STUDENT = "Сервис студента"
    ADMINISTRATION = "Сервис администратора"
