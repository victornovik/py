import time
from datetime import datetime, timedelta


def get_weekday():
    return datetime.date.today().strftime("%A %d %B %Y")


today = datetime.now()
print("Str():", str(today))
print("Repr():", repr(today))

# d = date(2024, 3, 15)
# print(d.isocalendar())
#
# t = time(16, 9, 28)
# print(t.isoformat())

# print(datetime.now())
#
# dt = datetime(2024, 3, 15, 16, 9, 28)
# print(dt.isoformat())
#
# print(dt.strftime("%d-%b-%Y %H:%M:%S"))
#
s = "15-Mar-2024 16:09:28"
dt2 = datetime.strptime(s, "%d-%b-%Y %H:%M:%S")
print(dt2)

print(dt2 + timedelta(days=100, minutes=3))

print(time.time())
print(time.ctime(1710681674))

# start = time.time()
# time.sleep(1.0)
# print(time.time() - start)
