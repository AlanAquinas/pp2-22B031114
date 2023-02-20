#---------------------------------------------------- 1
from datetime import date, timedelta

new_date = date.today() - timedelta(5)
print(new_date)
#---------------------------------------------------- 2
tup = ("yesterday", "today", "tomorrow")
a = iter(tup)
while True:
    try:
        print(next(a))
    except StopIteration:
        break
#---------------------------------------------------- 3
import datetime
date = datetime.datetime.today().replace(microsecond=0)
print(date)
#---------------------------------------------------- 4
from datetime import datetime

def dif_time(dt2,dt1):

    delta_time = dt2 - dt1

    return delta_time.days * 24 * 3600 + delta_time.seconds


data1 = datetime.strptime('2023-02-20 14:16:20','%Y-%m-%d %H:%M:%S')

data2 = datetime.now()

print(dif_time(data2,data1))