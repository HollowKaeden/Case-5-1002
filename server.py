from schedule import *
from time import *
import remote
import datetime as dt
import dataBase as db
conn = None
cursor = None
db.connect()
time = 0


def job():
    global time
    time += 1
    db.add_temperature_citys(time)
    db.add_temperature_apartments(time)


every(8).minutes.do(job)
while time != 180:
    run_pending()

