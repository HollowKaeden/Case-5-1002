from remote import *
import dataBase as db
conn = None
cursor = None
db.connect()


def instalInfo():
    for city_null in get_cities():
        city_id = city_null['city_id']
        city = get_city_data(city_id)
        db.add_city(city_id, city)

        add_city_houses(city_id)
    db.add_apartments()


def add_city_houses(city_id):
    city = db.get_city(city_id)
    for area_id in range(1, city.area_count + 1):
        area = get_area_data(city_id, area_id)
        for house in area:
            db.add_house(city_id, area_id, house)
