#!/usr/bin/python3
from  datetime import datetime
from  datetime import timedelta
d = datetime(1980, 1, 21)
day_number = d.weekday()
import calendar
days_text = list(calendar.day_name)
print()
print(list(calendar.day_name))
print(day_number)
print(days_text[day_number])
print()
print(timedelta(days=67))
print()
d2 = d + timedelta(days=67)
print("67 jours plus loin")
print(d2)
print(d2.weekday())
print(days_text[d2.weekday()])
print("mon age en jours")
print(datetime.today() - d)
print(type(datetime.today() - d))
timedeltajour = datetime.today() - d
agejour = timedeltajour.days
print(agejour)
print(agejour * 8 / 24) #nombre d'heure que j'ai dormi
