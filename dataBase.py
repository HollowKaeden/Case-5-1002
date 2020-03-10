# Андрей
import sqlite3
import remote


class City:
    def __init__(self, id, name, area_count, house_count, apartment_count):
        self.id = id
        self.name = name
        self.area_count = area_count
        self.house_count = house_count
        self.apartment_count = apartment_count


cursor = None
conn = None


def connect():
    global cursor, conn
    conn = sqlite3.connect("temp_data_full.db")
    cursor = conn.cursor()


def clearDtBs():
    cursor.execute('DELETE FROM APARTMENTS')
    cursor.execute('DELETE FROM HOUSES')
    cursor.execute('DELETE FROM CITIES')

    conn.commit()


def clearDtBs_temperature():
    cursor.execute('DELETE FROM APARTMENT_TEMPERATURE')
    cursor.execute('DELETE FROM CITIES_TEMPERATURE')


def add_city(city_id, city):
    # name, area_count, house_count, apartment_count
    cursor.execute('INSERT INTO CITIES VALUES (?,?,?,?,?)', (city_id,
                                                             city['city_name'], city['area_count'],
                                                             city['house_count'], city['apartment_count']))
    conn.commit()


def add_house(city_id, area_id, house):
    cursor.execute('''INSERT INTO HOUSES (city_id, area_id, house_number, apartment_count) 
                                   VALUES (?,?,?,?)''',
                                   (city_id, area_id, house['house_id'],
                                   house['apartment_count']))


def add_apartment(apartment_number, house):
    cursor.execute('''INSERT INTO APARTMENTS (apartment_number, house_id) 
                                        VALUES (?,?)''',
                   (apartment_number, house['house_id']))


def get_cities():
    return list(map(lambda x: City(x[0], x[1], x[2], x[3], x[4]),
                    cursor.execute("SELECT * FROM CITIES").fetchall()))


def get_houses():
    return list(cursor.execute('SELECT * from HOUSES'))


def add_apartments():
    for house in get_houses():
        apartment_count, house_id = house[-1], house[0]
        for apartment_number in range(1, apartment_count + 1):
            cursor.execute('''INSERT INTO APARTMENTS (apartment_number, house_id) 
                                                    VALUES (?,?)''',
                           (apartment_number, house_id))
    conn.commit()


def get_cities():
    return list(map(lambda x: City(x[0], x[1], x[2], x[3], x[4]),
                    cursor.execute("SELECT * FROM CITIES").fetchall()))


def get_city(id) -> City:
    result = cursor.execute("SELECT * FROM CITIES WHERE id=?", (id, )).fetchone()
    return City(result[0], result[1], result[2], result[3], result[4])


def get_temperature_City_year():
    cursor.execute('SELECT APARTMENTS (apartment_number, house_id')


def get_names_citys():
    return [i[0] for i in cursor.execute('SELECT name FROM CITIES')]


def get_houses_city(city_id):
    return cursor.execute('SELECT * FROM HOUSES WHERE city_id=?', (city_id, )).fetchall()

def get_id_apartment(house_id, apartment_number):
    return cursor.execute('''SELECT a.id FROM APARTMENTS a INNER JOIN HOUSES h ON a.house_id = h.id
    WHERE h.id=? and a.apartment_number=?''', (house_id, apartment_number)).fetchone()[0]

def get_apartments_number1():
    return cursor.execute('''SELECT h.city_id, h.area_id, h.house_number, a.apartment_number, a.id
    FROM APARTMENTS a INNER JOIN HOUSES h ON a.house_id = h.id 
    WHERE h.house_number=? AND a.apartment_number=? and h.area_id=?
    ''', (1, 1, 1)).fetchall()


def add_temperature_city(time_id, city_id, temp):
    cursor.execute('INSERT INTO CITIES_TEMPERATURE (city_id, time_id, temperature) VALUES (?, ?, ?)',
                        (city_id, time_id, float(temp)))



def add_temperature_apartment(time_id, apartment_id, temperature):
    cursor.execute('INSERT INTO APARTMENT_TEMPERATURE (apartment_id, time_id, temperature) VALUES (?, ?, ?)',
                   (apartment_id, time_id, float(temperature)))



def add_temperature_citys_oneApp(apartment_id, time_id, temperature):
    cursor.execute('INSERT INTO APARTMENT_TEMPERATURE (apartment_id, time_id, temperature) VALUES (?, ?, ?)',
                   (apartment_id, time_id, float(temperature)))



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


def get_cities_temperature_half_year(city_id):
    return cursor.execute('SELECT temperature FROM CITIES_TEMPERATURE WHERE time_id <= 180 and id=?', (city_id, )).fetchall()


def get_apartments_temperature_from_one_city(city_id):
    return cursor.execute('SELECT a.apartment_number, at.temperature FROM HOUSES \
h INNER JOIN APARTMENTS a on h.id = a.house_id INNER JOIN APARTMENT_TEMPERATURE at \
on a.id = at.apartment_id WHERE h.city_id=?', (city_id, )).fetchall()



def do_all_requests(time, city_id):
    # второе задание работает
    add_temperature_city(time, city_id, remote.get_city_temperature(city_id))

    # третье задание работает
    for house in get_houses_city(city_id):
        for apt in remote.get_apartments_temperature(house[1], house[2], house[3]):
            add_temperature_apartment(time, get_id_apartment(house[0], apt['apartment_id']), apt['temperature'])

    # четвертое задание работает
    for app in get_apartments_number1():
        if city_id == app[0]:
            continue
        add_temperature_citys_oneApp(app[4], time, remote.get_apartment_temperature(app[0], app[1], app[2], app[3]))
    conn.commit()
