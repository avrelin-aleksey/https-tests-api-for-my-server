from faker import Faker
from typing import Final


class Fake:
    """
    Класс-обертка над Faker для генерации тестовых данных.
    Предоставляет удобные методы для создания различных типов случайных данных.

    Пример использования:
    >>> fake = Fake()
    >>> email = fake.email()
    >>> name = fake.first_name()
    """

    # Диапазоны для генерации баллов
    DEFAULT_MAX_SCORE_RANGE: Final[tuple[int, int]] = (50, 100)
    DEFAULT_MIN_SCORE_RANGE: Final[tuple[int, int]] = (1, 30)
    DEFAULT_ESTIMATED_TIME_RANGE: Final[tuple[int, int]] = (1, 10)

    def __init__(self, faker: Faker = Faker()) -> None:
        """
        Инициализирует генератор тестовых данных.

        Args:
            faker: Экземпляр Faker (по умолчанию создается новый)
        """
        self.faker = faker

    def text(self) -> str:
        """Генерирует случайный текст (1 абзац)."""
        return self.faker.text()

    def uuid4(self) -> str:
        """Генерирует случайный UUID версии 4."""
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        Генерирует случайный email.

        Args:
            domain: Домен для email (если None - используется случайный)

        Returns:
            Строка с email адресом
        """
        return self.faker.email(domain=domain)

    def sentence(self) -> str:
        """Генерирует случайное предложение (5-15 слов)."""
        return self.faker.sentence()

    def password(self) -> str:
        """Генерирует случайный пароль (длиной 8-16 символов)."""
        return self.faker.password()

    def last_name(self) -> str:
        """Генерирует случайную фамилию."""
        return self.faker.last_name()

    def first_name(self) -> str:
        """Генерирует случайное имя."""
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Генерирует случайное отчество.
        Примечание: Faker не поддерживает отчества напрямую,
        поэтому используем first_name как базовую реализацию.
        """
        return self.faker.first_name()

    def estimated_time(self) -> str:
        """Генерирует строку с предполагаемым временем (например, '2 weeks')."""
        weeks = self.integer(*self.DEFAULT_ESTIMATED_TIME_RANGE)
        return f"{weeks} week{'s' if weeks != 1 else ''}"

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Генерирует случайное целое число в заданном диапазоне.

        Args:
            start: Минимальное значение (включительно)
            end: Максимальное значение (включительно)

        Returns:
            Случайное целое число
        """
        return self.faker.random_int(min=start, max=end)

    def max_score(self) -> int:
        """Генерирует случайный максимальный балл (50-100 по умолчанию)."""
        return self.integer(*self.DEFAULT_MAX_SCORE_RANGE)

    def min_score(self) -> int:
        """Генерирует случайный минимальный балл (1-30 по умолчанию)."""
        return self.integer(*self.DEFAULT_MIN_SCORE_RANGE)


# Создаем экземпляр по умолчанию для удобного импорта
fake = Fake()