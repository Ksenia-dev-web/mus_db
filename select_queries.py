# название и год выхода альбомов, вышедших в 2018 году; - ok
# название и продолжительность самого длительного трека; - wrong output 13 min
# название треков, продолжительность которых не менее 3,5 минуты; - ok
# названия сборников, вышедших в период с 2018 по 2020 год включительно; - ok
# исполнители, чье имя состоит из 1 слова; - ok
# название треков, которые содержат слово "мой"/"my". - ok

import sqlalchemy
# from psycopg2 import cursor
import pandas as pd

db = 'postgresql://postgres:123@localhost:5432/postgres'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

album_year = connection.execute("""SELECT name, year_of_release FROM album
WHERE year_of_release = '2018';""").fetchall()
print(album_year)

longest_track = connection.execute("""SELECT name, duration FROM track
ORDER by duration DESC;""").fetchone()
print(longest_track)

track_more_3_5 = connection.execute("""SELECT name, duration FROM track
WHERE duration >= '3 minute 30 second';""").fetchall()
print(track_more_3_5)

collections_2018_2020 = connection.execute("""SELECT name FROM collection
WHERE year_of_release BETWEEN 2018 and 2020;""").fetchmany(10)
print(collections_2018_2020)

one_word_artist = connection.execute("""SELECT name FROM artist
WHERE (LENGTH(name) - LENGTH(replace(name, ' ', ''))) = 0;""").fetchall()
print(one_word_artist)

my_included_track = connection.execute("""SELECT name FROM track
WHERE name LIKE '%%My%%' or name LIKE '%%my%%' or name LIKE '%%мой%%' or name LIKE '%%Мой%%';""").fetchall()
print(my_included_track)