# Days Between Dates
# Given your birthday and the current date, calculate your age in days.

# 1. Understanding a computational problem
# Input: your birthday and the current date [Possible inputs (set)]
# Output: your age in days(desired)
# Solution: Input => [Procedure (relationship between inputs to outputs)] => Output

# The 0 rule: Do not panic!

# The first rule: What are the inputs?
# Inputs: two dates
# What is the set of valid inputs: 
# (1)second date must not be before first date(Defensive Programming -> check this in our code)
# (2) Gregorian calendar (15 Oct 1582)
# How are inputs represented? => def daysBetweenDates(year1, month1, day1, year2, month2, day2)

# The second rule: What are the outputs?
# Outputs: Calculate your age in days
# How should we specify the output? => Return a number giving the numbers of days
# between the first date and the second date.

# Problem Statement:
# Define a procedure, daysBetweenDates, that takes two dates as inputs and returns
# the number of days between the first date and second date. Each date is passed in 
# as three numbers giving a valid year, month, and day in the Gregorian calendar.
# The second date must not be before the first.

# Solving the Problem
# Understand the Inputs, Understand the Outputs 
# and Understand the Relationship - some examples => Consider systematically how a human solves the problem

# The third rule: Work through some examples by hand
# human algorithm pseudocode
#[days = #of days in month1 - day1
# month1 += 1
# while month1 < month2:
#     days += #of days in month1
#     month1 += 1
# days += day2
# while year1 < year2:
#     days += days in year1        ]
# !!!! We should try to find a simple way !!!! Human is lazy to repeat but computer like mechnical alorithm.

# The fourth rule: Simple mechanical solution => Do not optimize prematurely! Simple and correct.
# Simple mechanical algorithm pseudocode
#[days = 0
# while date1 is before date2:
#     date1 = day after date1
#     days += 1
# return days                  ]

# Real world problem => Think best strategy
# The fifth rule: Develop incrementally and test as we go.

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1 and 
    year2/month2/day2. Assumes inputs are valid dates in Gergorian 
    calendar, and the first date is not after the second."""
    assert dateIsBefore(year1, month1, day1, year2, month2, day2)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
      return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def nextDay(year, month, day):
    """Waring: this version incorrectly
       assumes all months have 30 days!"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

def daysInMonth(year, month):
    daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year):
        daysOfMonths[1] = 29
    return daysOfMonths[month - 1]

def isLeapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def test():
    assert nextDay(2011, 11, 10)
    assert nextDay(2011, 11, 30)
    assert nextDay(2011, 12, 30)
    assert dateIsBefore(2011, 10, 2, 2011, 10, 3)
    assert dateIsBefore(2011, 9, 2, 2011, 10, 2)
    assert dateIsBefore(2010, 9, 2, 2011, 8, 2)
    assert nextDay(2011, 12, 30) == (2011, 12, 31)
    assert nextDay(2011, 2, 28) == (2011, 3, 1)
    assert daysInMonth(2011, 2) == 28
    assert daysInMonth(2012, 2) == 29
    assert daysInMonth(2000, 2) == 29
    assert daysInMonth(2000, 1) == 31
    assert daysInMonth(2000, 4) == 30
    assert daysBetweenDates(2011, 10, 2, 2011, 10, 3) == 1
    assert daysBetweenDates(2011, 9, 2, 2011, 10, 2) == 30
    assert daysBetweenDates(2010, 9, 2, 2011, 8, 2) == 334
    assert isLeapYear(2004)
    assert isLeapYear(2000)
    assert isLeapYear(2005) == False
    assert isLeapYear(1900) == False
    assert daysBetweenDates(2012, 2, 2, 2012, 3, 2) == 29
    assert daysBetweenDates(2012, 2, 2, 2013, 2, 2) == 366
    print("All pass!")
    
test()