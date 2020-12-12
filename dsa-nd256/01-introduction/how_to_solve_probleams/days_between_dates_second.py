# Days Between Dates
# Given your birthday and the current date, calculate your age in days.

# 1. Understanding a computational problem
# Input: your birthday and the current date [Possible inputs (set)]
# Output: your age in days(desired)
# Solution: Input => [Procedure (relationship between inputs to outputs)] => Output

# The first rule: What are the inputs?
# Inputs: two dates
# What is the set of valid inputs: 
# (1)second date must not be before first date(Defensive Programming -> check this in our code)
# (2) Gregorian calendar (15 Oct 1582)
# How are inputs represented? => def daysBetweenDates(year1, month1, day1, year2, month2, day2)