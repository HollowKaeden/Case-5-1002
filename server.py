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
    db.do_all_requests(time, city_id)
    print('Закончил работать в:', datetime.datetime.now())

every(8).minutes.do(job)
while time != 180:
    run_pending()

