from datetime import datetime
import os
from random import randrange
from datetime import timedelta

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

years = os.popen("date +%Y")
years = (years.read())[:4]

month = os.popen("date +%m")
month = (month.read())[:2]

day = os.popen("date +%d")
day = (day.read())[:2]

hour = os.popen("date +%H")
hour = hour.read()[:2]

minute = os.popen("date +%M")
minute = minute.read()[:2]

print(minute+"test")

d1 = datetime.strptime(f'{month}/{day}/{years} 23:59', '%m/%d/%Y %H:%M')
d2 = datetime.strptime(f'{month}/{day}/{str(int(years)+1)} 01:00', '%m/%d/%Y %H:%M')

result = random_date(d1, d2)

print(result)
print(f"{result.year}{result.month}{result.day}{result.hour}{result.minute}")

years = str(int(years))
month = str(int(month))
day = str(int(day))
hour = str(int(hour))
minute = str(int(minute))


print(f"{years}{month}{day}{hour}{minute}")
