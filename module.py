# import functions
from functions import sum
# import sys
# sys.path.append('C:\Users\Zamlyy\Desktop\Zamly Python\New folder')
from functions import sum

num1 = 20
num2 = 30

# print(functions.sum(num1, num2))
print(sum(num1, num2))

name = "zamly"

# print(hello_func(name))

# print(functions.hello_func(name))

# print(sys.path)
import random

course = ['Histry', 'Tamil', 'sinhala']

print(random.choices(course))

import math

rads = math.radians(90)

print(rads)

print(math.sin(rads))

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

import os

print(os.getcwd())
print(os.__file__)
