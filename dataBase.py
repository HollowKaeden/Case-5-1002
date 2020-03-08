# Андрей
import sqlite3


class City:
    def __init__(self, id, name, area_count, house_count, apartment_count):
        self.id = id
        self.name = name
        self.area_count = area_count
        self.house_count = house_count
        self.apartment_count = apartment_count


cursor = None
conn = None

def connect(db_name):
    global cursor, conn
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def clearDtBs():
    cursor.execute('DELETE FROM APARTMENTS')
    cursor.execute('DELETE FROM HOUSES')
    cursor.execute('DELETE FROM CITIES')


def add_city(city_id, city):
    # name, area_count, house_count, apartment_count
    cursor.execute('INSERT INTO CITIES VALUES (?,?,?,?,?)', (city_id,
                                                             city['city_name'], city['area_count'],
                                                             city['house_count'], city['apartment_count']))
    conn.commit()


def get_cities():
    return list(map(lambda x: City(x[0], x[1], x[2], x[3], x[4]),
                    cursor.execute("SELECT * FROM CITIES").fetchall()))


def get_city(id) -> City:
    result = cursor.execute("SELECT * FROM CITIES WHERE id=?", (id, )).fetchone()
    return City(result[0], result[1], result[2], result[3], result[4])


def get_city_id(cityName):
    return cursor.execute('SELECT * FROM CITIES WHERE name=?', (cityName, )).fetchone()[0]


def get_city_area_count(city_id):
    return cursor.execute('SELECT area_count FROM CITIES WHERE id=?', (city_id, )).fetchone()[0]


def get_area_house_count(city_id, area_id):
    return cursor.execute('SELECT house_number FROM HOUSES WHERE city_id=? and area_id=?',
                          (city_id, area_id, )).fetchall()[-1][0]


def get_house_apartment_count(city_id, area_id, house_id):
    return cursor.execute('SELECT apartment_count FROM HOUSES WHERE city_\
id=? and area_id=? and house_number=?',
                          (city_id, area_id, house_id, )).fetchone()[0]
