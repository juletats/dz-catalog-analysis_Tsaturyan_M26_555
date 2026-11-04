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


def print_non_comedy_movies(movies):
    """
       Этап 3. С помощью for и continue выведите на экран (print) названия
        всех фильмов, которые НЕ относятся к жанру "comedy".
       """
    for movie in movies:
        if "comedy" not in movie['genres']:
            print(movie['title'])
        else:
            continue


def find_first_masterpiece(movies):
    """
        Этап 3. С помощью while и break найдите первый по порядку в списке фильм
        с рейтингом выше 9.0; если такого фильма нет, цикл должен
        завершиться веткой else с сообщением "Шедевров не найдено".
        """
    i = 0
    while i < len(movies):
        if movies[i]['rating'] > 9.0:
            print("Первый шедевр:", movies[i]['title'])
            break  # нашли -- прерываемся, ветка else не выполнится
        i += 1
    else:
        # сработает только если цикл завершился без break
        print("Шедевров не найдено")
        return None
    return movies[i]


def count_long_movies(movies, threshold=120):
    """
        Этап 3. Функция count_long_movies(movies, threshold=120), которая через for с
        накопительной переменной считает количество фильмов длиннее threshold минут.
        """
    result = 0
    for movie in movies:
        if movie['duration_min'] > threshold:
            result += 1
    return result


def normalize_title(title):
    """
        Этап 4. Функция normalize_title(title), которая приводит строку к формату
        Title Case (каждое слово с заглавной буквы) без использования str.title()
        напрямую: разбейте строку по пробелам и соберите заново вручную,
        меняя первуюбукву каждого слова
        через срез (word[0].upper() + word[1:]).
        """
    words = title.split()
    result = []
    for word in words:
        if word:
            result.append(word[0].upper() + word[1:])
    return " ".join(result)


def make_slug(title):
    """
        Этап 4. Функция make_slug(title), которая превращает нормализованное
         название в «слаг» вида the-quiet-algorithm.
        """
    normalized = normalize_title(title)
    return normalized.replace(" ", "-").lower()


def format_report_line(movie):
    """
        Этап 4. Функция format_report_line(movie), возвращающую единую строку
        с описанием фильма:
        "The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi
        """
    title = normalize_title(movie['title'])
    year = movie['year']
    rating = str(movie['rating']) + '/10'
    duration = duration_in_hours(movie['duration_min'])
    genres = ", ".join(sorted(movie["genres"]))
    return f'"{title}" ({year}) — {rating}, {duration}, жанры: {genres}'


def titles_sorted_by_rating(movies):
    """
        Этап 5. Функция titles_sorted_by_rating(movies), возвращающую список
        названий фильмов, отсортированных по убыванию рейтинга.
        """
    sorted_movies = sorted(movies, key=lambda movie: movie['rating'], reverse=True)
    return [movie['title'] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    """
        Этап 5. Функция top_n_by_rating(movies, n=3), возвращающую список из n кортежей
         (title, rating) — топ по рейтингу.
        [("The Quiet Algorithm", 9.2), ("midnight in oslo", 8.9),
         ("The Dune Chronicles", 8.6)]
        """
    sorted_movies = sorted(movies, key=lambda movie: movie['rating'], reverse=True)
    return [(movie['title'], movie['rating']) for movie in sorted_movies[:n]]


def count_by_genre(movies):
    """
        Этап 6. Функция count_by_genre(movies), возвращающую словарь
        {жанр: количество фильмов}, построенный вручную
        через цикл и метод dict.get() (без Counter).
        """
    result = {}
    for movie in movies:
        for genre in movie['genres']:
            result[genre] = result.get(genre, 0) + 1
    return result


def actor_filmography(movies):
    """
        Этап 6. Функция  actor_filmography(movies),
        возвращающую словарь {актер: [список названий фильмов]}.
        """
    result = {}
    for movie in movies:
        for actor in movie['actors']:
            result.setdefault(actor, []).append(movie['title'])
    return result


def above_average_rating(movies):
    """
        Этап 6. С помощью генератора словаря (dict comprehension)
        постройте словарь {title: rating} только для фильмов с рейтингом
        выше среднего (используйте average_rating из этапа 1).
        """
    return {movie["title"]: movie["rating"]
            for movie in movies if movie["rating"] > average_rating(movies)}


def all_genres(movies):
    """
        Этап 7. Функция all_genres(movies), возвращающую
        множество всех уникальных жанров каталога
        """
    genres = set()
    for movie in movies:
        genres |= movie["genres"]
    return genres


def common_actors(movie1, movie2):
    """
        Этап 7. Функция common_actors(movie1, movie2),
         возвращающую множество актеров, снимавшихся в обоих фильмах.
        """
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    """
        Этап 7. Функция genres_only_in_one(movies_a, movies_b),
        которая возвращает жанры, встречающиеся в movies_a,
        но не встречающиеся в movies_b.
        """
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movies, min_rating=8.0):
    """
        Этап 8. Функция-генератор iter_high_rated(movies, min_rating=8.0),
        которая через yield лениво отдает фильмы с рейтингом не ниже min_rating
        """
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def duration_above_threshold_sum(movies, threshold=7.0):
    """
        Этап 8. Генераторное выражение, которое считает суммарную
        длительность всех фильмов с рейтингом выше 7 в минутах, и передает его в sum()
    """
    return sum(movie["duration_min"] for movie in movies if movie["rating"] > threshold)


def build_report(movies):
    """
        Этап 9. Функция build_report(movies), которая объединяет результаты всех
        предыдущих этапов в единый консольный отчет: общую статистику, топ-3 фильма,
        количество фильмов по каждому жанру и полный список уникальных жанров каталога.
    """
    print("ОТЧЕТ ПО КАТАЛОГУ")
    average_age = catalog_age_stats(movies)[2]
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {average_age} лет")
    print()

    by_title = {movie["title"]: movie for movie in movies}
    print("Топ-3 фильма:")
    for title, rating in top_n_by_rating(movies, 3):
        print("  " + format_report_line(by_title[title]))
    print()

    print("Фильмов по жанрам:")
    counts = count_by_genre(movies)
    sorted_genres = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    for genre, number in sorted_genres:
        print(f" {genre} — {number}")
    print()

    genre_line = ", ".join(sorted(all_genres(movies)))
    print(f"Все жанры каталога: {genre_line}")


if __name__ == '__main__':
    # Этап 1
    print("Средний рейтинг:", average_rating(movies))
    print("Средний возраст фильмов: " + str(catalog_age_stats(movies)[2]) + " лет")
    print("134 мин = " + duration_in_hours(134))
    # Этап 2
    print("Рейтинг 8.6: " + rating_tier(8.6))
    print("Фильмы 2018 года " + decade_label(2018))
    # Этап 3
    print("Количество фильмов длинее 120 минут: ", count_long_movies(movies))
    # Этап 4
    # case = "silent hours"
    # print(normalize_title(case))
    # print(make_slug(case))
    print(format_report_line(movies[7]))
    # Этап 5
    print(titles_sorted_by_rating(movies))
    print(top_n_by_rating(movies))
    # Этап 6
    print(count_by_genre(movies))
    print(actor_filmography(movies))
    print("Фильмы с рейтингом выше среднего: ", above_average_rating(movies))
    # Этап 7
    print(all_genres(movies))
    print(common_actors(movies[0], movies[3]))
    print(genres_only_in_one(movies[5:6], movies[:5]))
    # Этап 8
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
    print(duration_above_threshold_sum(movies))
    print()
    # Этап 9
    build_report(movies)
