import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson",
                                                    "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies):
    """
    Этап 1. Функция average_rating(movies) возвращает среднюю
    оценку по каталогу, округленную до одного знака (round).
    """
    ratings_sum = sum(movie['rating'] for movie in movies)
    return round(ratings_sum / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """
    Этап 1. Функция catalog_age_stats(movies, current_year=2026) возвращает
    кортеж (самый старый фильм в годах, самый новый фильм в годах, среднее),
    где среднее округлено вверх до целого с помощью math.ceil.
    """
    ages = [current_year - movie['year'] for movie in movies]
    return min(ages), max(ages), math.ceil(sum(ages) / len(ages))


def duration_in_hours(minutes):
    """
    Этап 1. Функция duration_in_hours(minutes) переводит минуты в формат "2ч 35м",
    используя целочисленное деление и остаток от деления.
    """
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours}ч {minutes}м"


def rating_tier(rating):
    """
    Этап 2. Функция rating_tier(rating), которая по оценке возвращает категорию:
    "шедевр" (≥9), "хорошо" (7–8.9), "средне" (5–6.9), "слабо" (<5).
    """
    if rating >= 9:
        return "шедевр"
    elif 7 <= rating <= 8.9:
        return "хорошо"
    return "слабо" if rating < 5 else "средне"


def decade_label(year):
    """
    Этап 2. Функция decade_label(year), которая через оператор match возвращает
    метку "новые" (после 2020), "недавние" (2015–2020) или "старые" (раньше 2015).
    """
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


if __name__ == '__main__':
    # Этап 1
    print("Средний рейтинг:", average_rating(movies))
    print("Средний возраст фильмов: " + str(catalog_age_stats(movies)[2]) + " лет")
    print("134 мин = " + duration_in_hours(134))
    # Этап 2
    print("Рейтинг 8.6: " + rating_tier(8.6))
    print("Рейтинг 5.6: " + rating_tier(5.6))
    print("Рейтинг 3.6: " + rating_tier(3.6))
    print("Рейтинг 9.6: " + rating_tier(9.6))
    print("Фильмы 2018 года " + decade_label(2018))
    print("Фильмы 1998 года " + decade_label(1998))
    print("Фильмы 2022 года " + decade_label(2022))
