import datetime

# day = datetime.date(2025, 8,3)
# day = datetime.date.today()

today = datetime.date.today()


# print(today.weekday())
# print(today.isoweekday())

tdelta = datetime.timedelta(days=7)

print(today - tdelta)

# bdate = datetime.date(1998,12,19)
# tdy = datetime.date.today()

# till_bday = tdy - bdate

# print(till_bday.total_seconds)

dt_str = 'July 26, 2025'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')

