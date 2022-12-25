import random
import faker
import json

import conf


def main() -> None:
    """
    Основная функция, формирует файл json.
    :return: None
    """
    gen_dict = gen_func()
    book_list = [next(gen_dict) for _ in range(10)]
    with open("books.json", "w", encoding="utf-8") as f_json:
        json.dump(book_list, f_json, ensure_ascii=False, indent=4)


def random_year() -> int:
    """
    Возвращает случайный год издания книги с 1900 до 2022. Используется модуль random.
    :return: год в виде целого цисла
    """
    return random.randint(1900, 2022)


def random_pages() -> int:
    """
    Возвращает случайное количество страниц книги от 10 до 500. Используется модуль random.
    :return: количество страниц в виде целого числа
    """
    return random.randint(10, 500)


def random_isbn13() -> str:
    """
    Возвращает случайный международный стандартный книжный номер isbn13. Используется модуль faker.
    :return: международный стандартный книжный номер в виде строки
    """
    fake = faker.Faker("ru")
    return fake.isbn13()


def random_rating() -> float:
    """
    Возвращает случайное значение рейтинга книги от 0 до 5. Используется модуль random.
    :return: значение рейтинга в виде числа с плавающей запятой
    """
    rand = random.uniform(0.00, 5.01)
    return round(rand, 2)


def random_price() -> float:
    """
    Возвращает случайное значение цены книги от 1 до 100. Используется модуль random.
    :return: значение цены в виде числа с плавающей запятой
    """
    rand = random.uniform(1.00, 100.01)
    return round(rand, 2)


def random_author() -> list:
    """
    Возвращает список случайных авторов книги (от 1 до 3). Используется модуль faker.
    :return: список случайных авторов книги
    """
    fake = faker.Faker("ru")
    quantity = random.randint(1, 3)
    author_list = []
    for _ in range(quantity):
        gender = random.choice(['m', 'f'])
        if gender == 'm':
            author_list.append(" ".join([fake.first_name_male(), fake.last_name_male()]))
        else:
            author_list.append(" ".join([fake.first_name_female(), fake.last_name_female()]))
    return author_list


def gen_func(start: int = 1) -> dict:
    """
    Функция-генератор для формирования словарей с информацией по книгам.
    :param data:
    :param start: начальное значение для счетчика
    :return: None
    """
    pk = start
    with open("books.txt", "r", encoding="utf-8") as f_txt:
        data = f_txt.readlines()
    while True:
        book_dict = {"model": conf.MODEL, "pk": pk, "fields": {"title": data[random.randint(0, 4)].rstrip(),
                                                                "year": random_year(),
                                                                "pages": random_pages(),
                                                                "isbn13": random_isbn13(),
                                                                "rating": random_rating(),
                                                                "price": random_price(),
                                                                "author": random_author()}}

        yield book_dict
        pk += 1


if __name__ == "__main__":
    main()
