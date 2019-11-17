days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def next_day(year, month, day):
    if day < days_in_month(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

def is_date_before(year1, month1, day1, year2, month2, day2):
    if (year1, month1, day1) < (year2, month2, day2):
        return True
    return False

def days_in_month(year, month):
    for m, days in enumerate(days_of_month):
        if m + 1 == month:
            if month == 2:
                if is_leap_year(year):
                    days = 29
                else:
                    days = 28
            return days

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
def days_between_dates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    assert not is_date_before(year2, month2, day2, year1, month1, day1), "Invalid dates, the second date should not be before first"
    days = 0
    while is_date_before(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = next_day(year1, month1, day1)
        days += 1
    return days

def test_days_between_dates():
    
    # test same day
    assert(days_between_dates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(days_between_dates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(days_between_dates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test leap month
    assert(days_between_dates(2012, 2, 28,
                              2012, 3, 1)  == 2)
    
    # test february for non-leap year
    assert(days_between_dates(2013, 2, 28,
                              2013, 3, 1)  == 1)
    
    # test full year difference
    assert(days_between_dates(2012, 6, 28,
                              2013, 6, 28)  == 365)
    
    print("Congratulations! Your days_between_dates")
    print("function is working correctly!")
    
test_days_between_dates()
