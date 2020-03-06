import sqlite3
from remote import *
import dataBase as db
conn = sqlite3.connect("temp_data_full.db")
cursor = conn.cursor()

def instalInfo():
    db.connect("temp_data_full.db")
    for city_null in get_cities():
        city_id = city_null['city_id']
        city = get_city_data(city_id)

        db.add_city(city_id, city)

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