import datetime

t = datetime.time(22, 20, 1)
print(t)
print('t.hour : ', t.hour)
print('t.minute : ', t.minute)
print('t.second : ',t.second)
print('t.microsecond', t.microsecond)
print('t.tzinfo', t.tzinfo)
print('t.max', t.max)
print('t.min', t.min)
print('t.resolution : ', t.resolution)

d = datetime.date.today()
print(d)
print('d.year ', d.year)
print('d.month ', d.month)
print('d.day ', d.day)