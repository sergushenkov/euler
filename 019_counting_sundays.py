"""You are given the following information, but you may prefer to do some
research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

"""


def is_leap_year(year):
    """
    >>> is_leap_year(2000)
    1
    >>> is_leap_year(1900)
    0
    >>> is_leap_year(1988)
    1
    >>> is_leap_year(1986)
    0

    """
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return 1
    return 0


months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31,
         9:30, 10:31, 11:30, 12:31}
year = 1900
month = 1
day = 1
day_week = 1

# прогоняю календарь до 1 января 1901 года
while not(day == 1 and month == 1 and year == 1901):
    day_week = (day_week + 1) % 7
    day += 1
    if (month == 2 and is_leap_year(year) and day > 29) or \
       (day > months[month]):
        day -= months[month]
        month += 1
        if month > 12:
            year += 1
            month -= 12
            
# подсчет воскресений 1-го числа месяца
count = 0
while not(day == 31 and month == 12 and year == 2000):
    day_week = (day_week + 1) % 7
    day += 1
    if (month == 2 and is_leap_year(year) and day > 29) or \
       (day > months[month]):
        day -= months[month]
        month += 1
        if month > 12:
            year += 1
            month -= 12
    if day == 1 and day_week == 0:
        count += 1
print(count)



