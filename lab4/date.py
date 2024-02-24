#ex1
from datetime import datetime, timedelta
currentDate= datetime.now()
fiveDaysAgo= currentDate- timedelta(days=5)
print('today:' ,currentDate.strftime('%d.%m.%y'))
print('five days ago: ', fiveDaysAgo.strftime('%d.%m.%y'))

#ex2
from datetime import datetime, timedelta
today= datetime.now()
yesterday= today- timedelta(days=1)
tomorrow= today+timedelta(days=1)
print('Yesterday: ', yesterday.strftime('%d.%m.%y') )
print('Today: ',today.strftime('%d.%m.%y'))
print('Tomorrow: ', tomorrow.strftime('%d.%m.%y'))

#ex3
from datetime import datetime
today= datetime.now()
todayWithoutMicroseconds= today.replace(microsecond=0)
print('original time: ', today )
print('without microseconds: ',todayWithoutMicroseconds )

#ex4
def DateDifferenceSeconds(y1, month1, d1, h1, min1, sec1, y2, month2, d2, h2, min2, sec2):
    total_seconds1 = sec1 + min1 * 60 + h1 * 3600 + d1 * 86400 + month1 * 2592000 + y1 * 31536000
    total_seconds2 = sec2 + min2 * 60 + h2 * 3600 + d2 * 86400 + month2 * 2592000 + y2 * 31536000
    difference = abs(total_seconds2 - total_seconds1)
    return difference
if __name__ == "__main__":
    year1 = int(input("year first date: "))
    month1 = int(input(" month first date: "))
    day1 = int(input("day first date: "))
    hour1 = int(input("hour first date: "))
    minute1 = int(input("minute first date: "))
    second1 = int(input("second first date: "))
    year2 = int(input("year second date: "))
    month2 = int(input(" month second date: "))
    day2 = int(input(" day second date: "))
    hour2 = int(input("hour second date: "))
    minute2 = int(input("minute second date: "))
    second2 = int(input("second second date: "))
    difference_seconds = DateDifferenceSeconds(year1, month1, day1, hour1, minute1, second1, year2, month2, day2, hour2, minute2, second2)
    print("Difference:", difference_seconds)
