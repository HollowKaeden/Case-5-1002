from schedule import *
from time import *
import remote
import dataBase as db
conn = None
cursor = None
db.connect()
time = 0


def job():
    global time
    time += 1
    for city in db.get_cities():
        temp = remote.get_city_temperature(city.id)
        db.add_temperature_city(time, temp, city)

    for house in db.get_houses_apartment_count():
        city_id, area_id, house_id = house[1], house[2], house[3]
        for apartment_id in range(1, house[-1] + 1):
            db.add_temperature_apartment(time, apartment_id, db.get_apartment_temperature(city_id, area_id, house_id, apartment_id))


every(8).minutes.do(job)


while time != 180:
    run_pending()
