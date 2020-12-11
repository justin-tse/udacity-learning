def daysBetweenDates(year1, month1, day1, year2, month2, day2):
  assert dateIsBefore(year1, month1, day1, year2, month2, day2)
  dayCount = 0
  while dateIsBefore(year1, month1, day1, year2, month2, day2):
      year1, month1, day1 = nextDay(year1, month1, day1)
      dayCount += 1
  return dayCount

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year2 > year1:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    if day < daysInMonth(year, month):
        return year, month, day + 1
    elif month < 12:
        return year, month + 1, 1
    else:
        return year + 1, 1, 1

def isLeapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def daysInMonth(year, month):
  assert month > 0 and month <= 12
  daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  if isLeapYear(year):
      daysOfMonths[1] = 29

  return daysOfMonths[month - 1]

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

def my_test(): 
    assert daysBetweenDates(2020, 12, 10, 2020, 12, 11) == 1
    assert daysBetweenDates(2020, 11, 10, 2020, 12, 10) == 30
    assert daysBetweenDates(2020, 2, 20, 2020, 3, 20) == 29
    assert daysBetweenDates(2020, 11, 10, 2020, 12, 10) == 30
    assert daysInMonth(2019, 2) == 28
    assert isLeapYear(2012)
    
    print("all pass")
            

            
my_test()  