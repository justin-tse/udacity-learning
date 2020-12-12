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
# days = #of days in month1 - day1
# month1 += 1
# while month1 < month2:
#     days += #of days in month1
#     month1 += 1
# days += day2
# while year1 < year2:
#     days += days in year1
# !!!! We should try to find a simple way !!!! Human is lazy to repeat but computer like mechnical alorithm.