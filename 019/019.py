
days_per_month = {
    1: 31,  # jan
    2: 28,  # feb
    3: 31,  # mar
    4: 30,  # apr
    5: 31,  # may
    6: 30,  # jun
    7: 31,  # jul
    8: 31,  # aug
    9: 30,  # sept
    10: 31,  # oct
    11: 30,  # nov
    12: 31,  # dec
}


def to_day(day):
    return {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
    }[day]


# leap years
# feb has 29 days on leap years
# leap year occurs on any year divisible by 4
# but not on a century unless it is divisible by 400
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:  # a centry
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False


# let sunday be the 0th day of the week, monday the 1st, etc..
start_day = 1  # monday
start = (1900, 1, 1)
end = (2000, 12, 31)

sundays = 0
while start < end:
    year, month, day = start

    # increment to next month
    start_day = (start_day + days_per_month[month]) % 7
    if month == 2:
        if is_leap_year(year):
            start_day = (start_day + 1) % 7
        month += 1
    elif month < 12:
        month += 1
    else:
        month = 1
        year += 1
    start = (year, month, day)

    # calculate sundays
    if start_day == 0 and year != 1900:
        print(year, month, day)
        sundays += 1

print(sundays)
