import sqlalchemy
# from psycopg2 import cursor
import pandas as pd

db = 'postgresql://postgres:123@localhost:5432/postgres'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()
# print(engine.table_names())

genre = [{'id': 1, 'name': 'rock'},
         {'id': 2, 'name': 'classical'},
         {'id': 3, 'name': 'industrial'},
         {'id': 4, 'name': 'world_music'},
         {'id': 5, 'name': 'neo_classical'},
         {'id': 6, 'name': 'barocco'},
         {'id': 7, 'name': 'indie'},
         {'id': 8, 'name': 'alternative_rock'},
         {'id': 9, 'name': 'jazz'}]

artist = [
         {'id': 11, 'name': 'Linkin park', 'nick_name': 'null'},
         {'id': 12, 'name': 'Rammstein', 'nick_name': 'null'},
         {'id': 13, 'name': 'Jacub Josef Orlinski', 'nick_name': 'Jacub Orlinski'},
         {'id': 14, 'name': 'Drumspyder', 'nick_name': 'null'},
         {'id': 15, 'name': 'Jay Jon Christopher Smith', 'nick_name': 'Jay Smith'},
         {'id': 16, 'name': 'Radiohead', 'nick_name': 'null'},
         {'id': 17, 'name': 'Joep Beving', 'nick_name': 'null'},
         {'id': 18, 'name': 'Odnono', 'nick_name': 'null'},
         {'id': 19, 'name': 'alt-J', 'nick_name': 'null'},
         {'id': 20, 'name': 'Flёur', 'nick_name': 'null'},
         {'id': 21, 'name': 'Alina Orlovskaja', 'nick_name': 'Alina Orlova'},
         {'id': 22, 'name': 'Kings Of Convenience', 'nick_name': 'null'},
         {'id': 23, 'name': 'Ian Scott Anderson', 'nick_name': 'Ian Anderson'},
         {'id': 24, 'name': 'Mgzavrebi', 'nick_name': 'null'},
         {'id': 25, 'name': 'Алексей Рыбников', 'nick_name': 'null'},
         {'id': 26, 'name': 'Gordon Matthew Thomas Sumner', 'nick_name': 'Sting'},
         {'id': 27, 'name': 'The Doors', 'nick_name': 'null'},
         {'id': 28, 'name': 'Musicaeterna orchestra', 'nick_name': 'null'},
         {'id': 29, 'name': 'Morcheeba', 'nick_name': 'null'},
         {'id': 30, 'name': 'Imagine dragons', 'nick_name': 'null'},
         {'id': 31, 'name': 'Teodor Currentzis', 'nick_name': 'null'},
         {'id': 32, 'name': 'Le Poème Harmonique', 'nick_name': 'null'},
         {'id': 33, 'name': 'L_Arpeggiata', 'nick_name': 'null'},
         {'id': 34, 'name': 'Kristjan Järvi', 'nick_name': 'null'},
         {'id': 35, 'name': 'Ella Fitzgerald', 'nick_name': 'null'}
         ]

album = [
        {'id': 101, 'name': 'Arvo Pärt: Passacaglia', 'year_of_release': '2015'},
        {'id': 102, 'name': 'Iasamani', 'year_of_release': '2018'},
        {'id': 103, 'name': 'Meteora', 'year_of_release': '2003'},
        {'id': 104, 'name': 'Rammstein', 'year_of_release': '2019'},
        {'id': 105, 'name': 'Vedrò con mio diletto (Vivaldi)', 'year_of_release': '2018'},
        {'id': 106, 'name': 'The Mother Rune', 'year_of_release': '2018'},
        {'id': 107, 'name': 'OK Computer OKNOTOK 1997', 'year_of_release': '2017'},
        {'id': 108, 'name': 'Solipsism', 'year_of_release': '2015'},
        {'id': 109, 'name': 'Зерна', 'year_of_release': '2016'},
        {'id': 110, 'name': 'An Awesome Wave', 'year_of_release': '2012'},
        {'id': 111, 'name': 'Волшебство', 'year_of_release': '2003'},
        {'id': 112, 'name': 'Дикая собака Динго', 'year_of_release': '2008'},
        {'id': 113, 'name': 'Declaration Of Dependence', 'year_of_release': '2009'},
        {'id': 114, 'name': 'Rupis Dance', 'year_of_release': '2009'},
        {'id': 115, 'name': 'Музыка кино', 'year_of_release': '2004'},
        {'id': 116, 'name': 'Together As One', 'year_of_release': '2007'},
        {'id': 117, 'name': 'The Soft Parade', 'year_of_release': '1969'},
        {'id': 118, 'name': 'Mozart: Requiem', 'year_of_release': '2011'},
        {'id': 119, 'name': 'Dive Deep', 'year_of_release': '2008'},
        {'id': 120, 'name': 'Night Visions', 'year_of_release': '2013'},
        {'id': 121, 'name': 'Purcell Dido & Aeneas', 'year_of_release': '2008'},
        {'id': 122, 'name': 'Ostinato', 'year_of_release': '2012'},
        {'id': 123, 'name': 'Music for a While - Improvisations on Purcell', 'year_of_release': '2014'}
        ]

track = [
    {'id': '151', 'name': 'Credo', 'duration': '13 minutes 41 second', 'album_id': 101},
    {'id': '152', 'name': 'Iavnana', 'duration': '3 minute 23 second', 'album_id': 102},
    {'id': '153', 'name': 'Breaking the habbit', 'duration': '3 minute 16 second', 'album_id': 103},
    {'id': '154', 'name': 'Auslander', 'duration': '3 minute 50 second', 'album_id': 104},
    {'id': '155', 'name': 'My funny Valentine', 'duration': '3 minute 54 second', 'album_id': 'null'},
    {'id': '156', 'name': 'Vivaldi: Il Giustino, RV 717, Act 1: "Vedrò con mio diletto" (Anastasio)',
     'duration': '5 minute 37 second', 'album_id': 105},
    {'id': '157', 'name': 'The Mother Rune', 'duration': '5 minute 28 second', 'album_id': 106},
    {'id': '158', 'name': 'Black Jesus', 'duration': '4 minute 17 second', 'album_id': 'null'},
    {'id': '159', 'name': 'Karma Police', 'duration': '4 minute 21 second', 'album_id': 107},
    {'id': '160', 'name': 'The Light She Brings', 'duration': '2 minute 53 second', 'album_id': 108},
    {'id': '161', 'name': 'Решай сам', 'duration': '4 minute 12 second', 'album_id': 109},
    {'id': '162', 'name': 'Taro', 'duration': '5 minute 05 second', 'album_id': 110},
    {'id': '163', 'name': 'Формалин', 'duration': '4 minute 03 second', 'album_id': 111},
    {'id': '164', 'name': 'Menulis', 'duration': '1 minute 36 second', 'album_id': 112},
    {'id': '165', 'name': 'Riot On An Empty Street', 'duration': '4 minute 05 second', 'album_id': 113},
    {'id': '166', 'name': 'Old Black Cat', 'duration': '3 minute 41 second', 'album_id': 114},
    {'id': '167', 'name': 'Гроза', 'duration': '1 minute 11 second', 'album_id': 115},
    {'id': '168', 'name': 'Lullaby to an Anxious Child ', 'duration': '4 minute 10 second', 'album_id': 116},
    {'id': '169', 'name': 'Wild Child', 'duration': '2 minute 35 second', 'album_id': 117},
    {'id': '170', 'name': 'Requiem in D Minor, K. 626 III Sequenz Lacrimosa', 'duration': '3 minute 47 second', 'album_id': 118},
    {'id': '171', 'name': 'Enjoy the Ride ', 'duration': '4 minute 02 second', 'album_id': 119},
    {'id': '172', 'name': 'Radioactive', 'duration': '3 minute 07 second', 'album_id': 120},
    {'id': '173', 'name': 'Dido & Aeneas Act I, Z 626 Ah Belinda', 'duration': '4 minute 48 second', 'album_id': 121},
    {'id': '174', 'name': 'Lamento della ninfa', 'duration': '3 minute 45 second', 'album_id': 122},
    {'id': '175', 'name': 'Oedipus, King of Thebes, Music for a while', 'duration': '5 minute 54 second', 'album_id': 123}
    ]

collection = [
         {'id': 211, 'name': 'Essential Bands', 'year_of_release': 2006},
         {'id': 212, 'name': 'Idol Box', 'year_of_release': 2011},
         {'id': 213, 'name': 'Nyårsfest', 'year_of_release': 2020},
         {'id': 214, 'name': 'Claudio Monteverdi: Madrigali Guerrieri Et Amorosi', 'year_of_release': 2009},
         {'id': 215, 'name': 'Дискография', 'year_of_release': 2016},
         {'id': 216, 'name': 'The Singles', 'year_of_release': 2017},
         {'id': 217, 'name': 'Музыка из фильмов', 'year_of_release': 1975},
         {'id': 218, 'name': 'Thick As A Brick - Live In Iceland', 'year_of_release': 2014},
         {'id': 219, 'name': 'Ella 100', 'year_of_release': 2012}
         ]

genre_artist = [
         {'id': 311, 'artist_id': 11, 'genre_id': 8},
         {'id': 312, 'artist_id': 12, 'genre_id': 3},
         {'id': 313, 'artist_id': 13, 'genre_id': 6},
         {'id': 314, 'artist_id': 14, 'genre_id': 4},
         {'id': 315, 'artist_id': 15, 'genre_id': 1},
         {'id': 316, 'artist_id': 16, 'genre_id': 8},
         {'id': 317, 'artist_id': 17, 'genre_id': 5},
         {'id': 318, 'artist_id': 18, 'genre_id': 4},
         {'id': 319, 'artist_id': 19, 'genre_id': 8},
         {'id': 320, 'artist_id': 20, 'genre_id': 1},
         {'id': 321, 'artist_id': 21, 'genre_id': 7},
         {'id': 322, 'artist_id': 22, 'genre_id': 7},
         {'id': 323, 'artist_id': 23, 'genre_id': 8},
         {'id': 324, 'artist_id': 24, 'genre_id': 4},
         {'id': 325, 'artist_id': 25, 'genre_id': 5},
         {'id': 326, 'artist_id': 26, 'genre_id': 4},
         {'id': 327, 'artist_id': 27, 'genre_id': 1},
         {'id': 328, 'artist_id': 28, 'genre_id': 2},
         {'id': 329, 'artist_id': 29, 'genre_id': 1},
         {'id': 330, 'artist_id': 30, 'genre_id': 1},
         {'id': 331, 'artist_id': 31, 'genre_id': 2},
         {'id': 332, 'artist_id': 32, 'genre_id': 6},
         {'id': 333, 'artist_id': 33, 'genre_id': 6},
         {'id': 334, 'artist_id': 34, 'genre_id': 6},
         {'id': 335, 'artist_id': 35, 'genre_id': 9}
        ]

album_artist = [
         {'id': 411, 'artist_id': 11, 'album_id': 103},
         {'id': 412, 'artist_id': 12, 'album_id': 104},
         {'id': 413, 'artist_id': 13, 'album_id': 105},
         {'id': 414, 'artist_id': 14, 'album_id': 106},
         {'id': 415, 'artist_id': 15, 'album_id': 'null'},
         {'id': 416, 'artist_id': 16, 'album_id': 107},
         {'id': 417, 'artist_id': 17, 'album_id': 108},
         {'id': 418, 'artist_id': 18, 'album_id': 109},
         {'id': 419, 'artist_id': 19, 'album_id': 110},
         {'id': 420, 'artist_id': 20, 'album_id': 111},
         {'id': 421, 'artist_id': 21, 'album_id': 112},
         {'id': 422, 'artist_id': 22, 'album_id': 113},
         {'id': 423, 'artist_id': 23, 'album_id': 114},
         {'id': 424, 'artist_id': 24, 'album_id': 102},
         {'id': 425, 'artist_id': 25, 'album_id': 115},
         {'id': 426, 'artist_id': 26, 'album_id': 116},
         {'id': 427, 'artist_id': 27, 'album_id': 117},
         {'id': 428, 'artist_id': 28, 'album_id': 118},
         {'id': 429, 'artist_id': 29, 'album_id': 119},
         {'id': 430, 'artist_id': 30, 'album_id': 120},
         {'id': 431, 'artist_id': 31, 'album_id': 121},
         {'id': 432, 'artist_id': 32, 'album_id': 122},
         {'id': 433, 'artist_id': 33, 'album_id': 123},
         {'id': 434, 'artist_id': 34, 'album_id': 101},
         {'id': 435, 'artist_id': 35, 'album_id': 'null'}
         ]

collection_track = [
         {'id': 511, 'collection_id': 211, 'track_id': 159},
         {'id': 512, 'collection_id': 212, 'track_id': 158},
         {'id': 513, 'collection_id': 213, 'track_id': 172},
         {'id': 514, 'collection_id': 214, 'track_id': 174},
         {'id': 515, 'collection_id': 215, 'track_id': 163},
         {'id': 516, 'collection_id': 216, 'track_id': 169},
         {'id': 517, 'collection_id': 217, 'track_id': 167},
         {'id': 518, 'collection_id': 218, 'track_id': 166},
         {'id': 519, 'collection_id': 219, 'track_id': 155}
         ]

# DOESN'T WORK BECAUSE OF CONSTRAINTS!!! correct order of db download
# genre_massive = pd.DataFrame(genre)
# print(genre_massive)
# genre_massive.to_sql('genre', connection, if_exists='replace', index=True)
#
# artist_massive = pd.DataFrame(artist)
# print(artist_massive)
# artist_massive.to_sql('artist', connection, if_exists='replace', index=True)
#
# album_massive = pd.DataFrame(album)
# print(album_massive)
# album_massive.to_sql('album', connection, if_exists='replace', index=True)
#
# track_massive = pd.DataFrame(track)
# print(track_massive)
# track_massive.to_sql('track', connection, if_exists='replace', index=True)
#
# collection_massive = pd.DataFrame(collection)
# print(collection_massive)
# collection_massive.to_sql('collection', connection, if_exists='replace', index=True)
#
# genre_artist_massive = pd.DataFrame(genre_artist)
# print(genre_artist_massive)
# genre_artist_massive.to_sql('genre_artist', connection, if_exists='replace', index=True)
#
# album_artist_massive = pd.DataFrame(album_artist)
# print(album_artist_massive)
# album_artist_massive.to_sql('album_artist', connection, if_exists='replace', index=True)
#
# collection_track_massive = pd.DataFrame(collection_track)
# print(collection_track_massive)
# collection_track_massive.to_sql('collection_track', connection, if_exists='replace', index=True)

# res = connection.execute("""SELECT id, name FROM genre;""").fetchall()
# print('res=', res)
#
# res1 = connection.execute("""SELECT id, name FROM artist;""").fetchall()
# print('res1=', res1)
#
# res2 = connection.execute("""SELECT id, name FROM album;""").fetchall()
# print('res2=', res2)
#
# res3 = connection.execute("""SELECT id, name FROM collection;""").fetchall()
# print('res3=', res3)
#
# res4 = connection.execute("""SELECT id, genre_id FROM genre_artist;""").fetchall()
# print('res4=', res4)
#
# res5 = connection.execute("""SELECT id, album_id FROM album_artist;""").fetchall()
# print('res5=', res5)
#
# res6 = connection.execute("""SELECT id, collection_id FROM collection_track;""").fetchall()
# print('res6=', res6)
#
# res7 = connection.execute("""SELECT id, name FROM track;""").fetchall()
# print('res7=', res7)

# название и год выхода альбомов, вышедших в 2018 году; - ok
# название и продолжительность самого длительного трека; - wrong output 13 min
# название треков, продолжительность которых не менее 3,5 минуты; - ok
# названия сборников, вышедших в период с 2018 по 2020 год включительно; - ok
# исполнители, чье имя состоит из 1 слова; - ok
# название треков, которые содержат слово "мой"/"my". - ok

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

