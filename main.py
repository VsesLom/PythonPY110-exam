import random
import faker
import json

import conf


def main() -> None:
    a = gen_func()
    book_list = [next(a) for _ in range(100)]
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump(book_list, f, ensure_ascii=False, indent=4)


def gen_func(start: int=1) -> dict:
    def random_year() -> int:
        return random.randint(1980, 2022)

    def random_pages() -> int:
        return random.randint(100, 500)

    def random_isbn13() -> str:
        fake = faker.Faker("ru")
        return fake.isbn13()

    def random_rating() -> float:
        rand = random.uniform(0.00, 5.01)
        return round(rand, 2)

    def random_price() -> float:
        return random.uniform(0, 100)

    def random_author() -> list:
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

    pk = start
    with open("books.txt", "r", encoding="utf-8") as f:
        data = f.readlines()
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
