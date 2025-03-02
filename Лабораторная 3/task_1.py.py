class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга '{self.name}'. Автор {self.author}"

    def __repr__(self):
        # Исправлено на self.__class__.__name__
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages  # Добавлена инициализация _pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise TypeError(f"Количество страниц должно быть типом int и положительным.")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга '{self.name}'. Автор {self.author}. Количество страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration  # Добавлена инициализация _duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (int, float)) or value <= 0:
            raise TypeError(f"Продолжительность должна быть числом с плавающей запятой и положительной.")
        self._duration = float(value)

    def __str__(self):
        return f"Аудиокнига '{self.name}'. Автор {self.author}. Продолжительность: {self.duration:.2f} часов"


# Тестирование
if __name__ == "__main__":
    paper_book = PaperBook("Клинок, рассекающий демонов", "Коёхару Готогоэ", 1500)
    audio_book = AudioBook("Оно", "Стивен Кинг", 55.5)

    print(paper_book)
    print(audio_book)
