# 1006 - 1996
# leap year
# 26 monday
# 27?

import datetime
import calendar


leap_years = []
for i in range(1006, 1997,10):
    weekday = datetime.date(i,1,26).isoweekday()
    if calendar.isleap(i) and weekday == 1:
        leap_years.append(i)
print(leap_years[-2])
