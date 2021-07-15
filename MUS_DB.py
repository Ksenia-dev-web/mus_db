import sqlalchemy
import psycopg2


db = 'postgresql://postgres:123@localhost:5432/postgres'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

genre = [{'id': '1', 'name': 'rock'},
         {'id': '2', 'name': 'classical'},
         {'id': '3', 'name': 'industrial'},
         {'id': '4', 'name': 'world_music'},
         {'id': '5', 'name': 'neo_classical'},
         {'id': '6', 'name': 'barocco'},
         {'id': '7', 'name': 'indie'},
         {'id': '8', 'name': 'alternative_rock'}]

artist = [
         {'id': '11', 'name': 'Linkin park', 'nick_name': 'null'},
         {'id': '12', 'name': 'Rammstein', 'nick_name': 'null'},
         {'id': '13', 'name': 'Jacub Josef Orlinski', 'nick_name': 'Jacub Orlinski'},
         {'id': '14', 'name': 'Drumspyder', 'nick_name': 'null'},
         {'id': '15', 'name': 'Jay Jon Christopher Smith', 'nick_name': 'Jay Smith'},
         {'id': '16', 'name': 'Radiohead', 'nick_name': 'null'},
         {'id': '17', 'name': 'Joep Beving', 'nick_name': 'null'},
         {'id': '18', 'name': 'Odnono', 'nick_name': 'null'},
         {'id': '19', 'name': 'alt-J', 'nick_name': 'null'},
         {'id': '20', 'name': 'Flёur', 'nick_name': 'null'},
         {'id': '21', 'name': 'Alina Orlovskaja', 'nick_name': 'Alina Orlova'},
         {'id': '22', 'name': 'Kings Of Convenience', 'nick_name': 'null'},
         {'id': '23', 'name': 'Ian Scott Anderson', 'nick_name': 'Ian Anderson'},
         {'id': '24', 'name': 'Mgzavrebi', 'nick_name': 'null'},
         {'id': '25', 'name': 'Алексей Рыбников', 'nick_name': 'null'},
         {'id': '26', 'name': 'Gordon Matthew Thomas Sumner', 'nick_name': 'Sting'},
         {'id': '27', 'name': 'The Doors', 'nick_name': 'null'},
         {'id': '28', 'name': 'Musicaeterna orchestra', 'nick_name': 'null'},
         {'id': '29', 'name': 'Morcheeba', 'nick_name': 'null'},
         {'id': '30', 'name': 'Imagine dragons', 'nick_name': 'null'},
         {'id': '31', 'name': 'Teodor Currentzis', 'nick_name': 'null'},
         {'id': '32', 'name': 'Le Poème Harmonique', 'nick_name': 'null'},
         {'id': '33', 'name': 'L_Arpeggiata', 'nick_name': 'null'},
         {'id': '34', 'name': 'Kristjan Järvi', 'nick_name': 'null'}]

album = [
        {'id': '101', 'name': 'Arvo Pärt: Passacaglia', 'year_of_release': '2015'},
        {'id': '102', 'name': 'Iasamani', 'year_of_release': '2018'},
        {'id': '103', 'name': 'Meteora', 'year_of_release': '2003'},
        {'id': '104', 'name': 'Rammstein', 'year_of_release': '2019'},
        {'id': '105', 'name': 'Vedrò con mio diletto (Vivaldi)', 'year_of_release': '2018'},
        {'id': '106', 'name': 'The Mother Rune', 'year_of_release': '2018'},
        {'id': '107', 'name': 'OK Computer OKNOTOK 1997', 'year_of_release': '2017'},
        {'id': '108', 'name': 'Solipsism', 'year_of_release': '2015'},
        {'id': '109', 'name': 'Зерна', 'year_of_release': '2016'},
        {'id': '110', 'name': 'An Awesome Wave', 'year_of_release': '2012'},
        {'id': '111', 'name': 'Волшебство', 'year_of_release': '2003'},
        {'id': '112', 'name': 'Дикая собака Динго', 'year_of_release': '2008'},
        {'id': '113', 'name': 'Declaration Of Dependence', 'year_of_release': '2009'},
        {'id': '114', 'name': 'Rupis Dance', 'year_of_release': '2009'},
        {'id': '115', 'name': 'Музыка кино', 'year_of_release': '2004'},
        {'id': '116', 'name': 'Together As One', 'year_of_release': '2007'},
        {'id': '117', 'name': 'The Soft Parade', 'year_of_release': '1969'},
        {'id': '118', 'name': 'Mozart: Requiem', 'year_of_release': '2011'},
        {'id': '119', 'name': 'Dive Deep', 'year_of_release': '2008'},
        {'id': '120', 'name': 'Night Visions', 'year_of_release': '2013'},
        {'id': '121', 'name': 'Purcell Dido & Aeneas', 'year_of_release': '2008'},
        {'id': '122', 'name': 'Ostinato', 'year_of_release': '2012'},
        {'id': '123', 'name': 'Music for a While - Improvisations on Purcell', 'year_of_release': '2014'}
         ]



track = [
    {'id': '151', 'name': 'Credo', 'duration': '13:41', 'album_id': '101'},
    {'id': '152', 'name': 'Iavnana', 'duration': '3:23', 'album_id': '102'},
    {'id': '153', 'name': 'Breaking the habbit', 'duration': '3:16', 'album_id': '103'},
    {'id': '154', 'name': 'Auslander', 'duration': '3:50', 'album_id': '104'},
    {'id': '155', 'name': 'Auslander', 'duration': '3:16', 'album_id': '103'},
    {'id': '156', 'name': 'Vivaldi: Il Giustino, RV 717, Act 1: "Vedrò con mio diletto" (Anastasio)', 'duration': '5:37', 'album_id': '105'},
    {'id': '157', 'name': 'The Mother Rune', 'duration': '5:28', 'album_id': '106'},
    {'id': '158', 'name': 'Black Jesus', 'duration': '4:17', 'album_id': 'null'},
         # нет альбома есть сборник
    {'id': '159', 'name': 'Karma Police', 'duration': '4:21', 'album_id': '107'},
    {'id': '160', 'name': 'The Light She Brings', 'duration': '2:53', 'album_id': '108'},
    {'id': '161', 'name': 'Решай сам', 'duration': '4:12', 'album_id': '109'},
    {'id': '162', 'name': 'Taro', 'duration': '5:05', 'album_id': '110'},
    {'id': '163', 'name': 'Формалин', 'duration': '4:03', 'album_id': '111'},
    {'id': '164', 'name': 'Menulis', 'duration': '1:36', 'album_id': '112'},
    {'id': '165', 'name': 'Riot On An Empty Street', 'duration': '4:05', 'album_id': '113'},
    {'id': '166', 'name': 'Old Black Cat', 'duration': '3:41', 'album_id': '114'},
    {'id': '167', 'name': 'Гроза', 'duration': '1:11', 'album_id': '115'},
    {'id': '168', 'name': 'Lullaby to an Anxious Child ', 'duration': '4:10', 'album_id': '116'},
    {'id': '169', 'name': 'Wild Child', 'duration': '2:35', 'album_id': '117'},
    {'id': '170', 'name': 'Requiem in D Minor, K. 626 III Sequenz Lacrimosa', 'duration': '3:47', 'album_id': '118'},
    {'id': '171', 'name': 'Enjoy the Ride ', 'duration': '4:02', 'album_id': '119'},
    {'id': '172', 'name': 'Radioactive', 'duration': '3:07', 'album_id': '120'},
    {'id': '173', 'name': 'Dido & Aeneas Act I, Z 626 Ah Belinda', 'duration': '4:48', 'album_id': '121'},
    {'id': '174', 'name': 'Lamento della ninfa', 'duration': '3:45', 'album_id': '122'},
    {'id': '175', 'name': 'Oedipus, King of Thebes, Music for a while', 'duration': '5:54', 'album_id': '123'}
    ]

