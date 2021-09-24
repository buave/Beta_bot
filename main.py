from datetime import datetime
import os
from random import randrange
from datetime import timedelta
import random
import sqlite3
import time

today = False

years = os.popen("date +%Y")
years = (years.read())[:4]

month = os.popen("date +%m")
month = (month.read())[:2]

day = os.popen("date +%d")
day = (day.read())[:2]

years = str(int(years))
month = str(int(month))
day = str(int(day))
date = int(years+month+day)

conn = sqlite3.connect("data.db")
date_db = conn.execute("SELECT DATE FROM SAVE")
for row in date_db:
    if row[0] == date:
        today = True
        print("yes")

if today == True:
    finish = False
    date_db = conn.execute("select HOUR FROM SAVE")
    for row in date_db:
        hour_db = row[0]
    while finish == False:
        hour = os.popen("date +%H")
        hour = hour.read()[:2]

        minute = os.popen("date +%M")
        minute = minute.read()[:2]

        hour = str(int(hour))
        minute = str(int(minute))

        time_h = int(hour + minute)

        if time_h == hour_db:


            #Do what you want


            def random_date(start, end):
                delta = end - start
                int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
                random_second = randrange(int_delta)
                return start + timedelta(seconds=random_second)

            d1 = datetime.strptime(f'{month}/{day}/{years}', '%m/%d/%Y')
            d2 = datetime.strptime(f'{month}/{day}/{str(int(years)+1)}', '%m/%d/%Y')

            hour_rand = random.randint(6, 23)
            minute_rand = random.randint(1,59)

            result = random_date(d1, d2)

            print(f"{result.year}{result.month}{result.day}")
            print(f"{hour_rand}{minute_rand}")

            date = int(str(result.year)+str(result.month)+str(result.day))
            time_d = int(str(hour_rand)+str(minute_rand))

            conn.execute("DELETE FROM SAVE WHERE HOUR")
            conn.commit()
            conn.execute("INSERT INTO SAVE (DATE, HOUR) VALUES (?, ?)", (date, time_d))
            conn.commit()
            finish = True


        time.sleep(30)

conn.close()
