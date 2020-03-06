import sqlite3
from remote import *
conn = sqlite3.connect("temp_data_full.db")
cursor = conn.cursor()

def clearDtBs():
    cursor.execute('DELETE FROM APARTMENTS')
    cursor.execute('DELETE FROM HOUSES')
    cursor.execute('DELETE FROM CITIES')

def instalInfo():
    for city_null in get_cities():
        city_id = city_null['city_id']
        city = get_city_data(city_id)
        # name, area_count, house_count, apartment_count
        cursor.execute('INSERT INTO CITIES VALUES (?,?,?,?,?)',(city_id,
                       city['city_name'], city['area_count'],
                       city['house_count'], city['apartment_count']))

        for area_id in range(1, city['area_count'] + 1):
            # [{'house_id': 1, 'apartment_count': 56}...]
            area = get_area_data(city_id, area_id)
            for house in area:
                # city_id, area_id, house_number, apartment_count
                cursor.execute('''INSERT INTO HOUSES (city_id, area_id, house_number, apartment_count) 
                               VALUES (?,?,?,?)''',
                               (city_id, area_id, house['house_id'],
                               house['apartment_count']))
                for apartment_number in range(1, house['apartment_count'] + 1):
                    cursor.execute('''INSERT INTO APARTMENTS (apartment_number, house_id) 
                                    VALUES (?,?)''',
                                   (apartment_number, house['house_id']))
conn.commit()