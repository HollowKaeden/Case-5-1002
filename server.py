from schedule import *
from time import *
from remote import *
import datetime as dt
import dataBase as db
conn = None
cursor = None
db.connect()
time = 0
city_id = 11


def job():
    global time
    time += 1
    print('Начал работать в:', datetime.datetime.now())
    # второе задание работает
    db.add_temperature_city(time, city_id, get_city_temperature(city_id))

    # третье задание работает
    for house in db.get_houses_city(city_id):
        temp = []
        for apt in get_apartments_temperature(house[1], house[2], house[3]):
            temp += [apt]
        db.add_temperature_apartments(time, temp, house[0])

    # четвертое задание работает
    for app in db.get_apartments_number1():
        if city_id == app[0]:
            continue
        db.add_temperature_citys_oneApp(app[4], time, get_apartment_temperature(app[0], app[1], app[2], app[3]))
    print('Закончил работать в:', datetime.datetime.now())

every(8).minutes.do(job)
while time != 180:
    run_pending()
