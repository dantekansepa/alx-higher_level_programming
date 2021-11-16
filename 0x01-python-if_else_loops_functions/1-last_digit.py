#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
print("Last digit of {:d} is {:d}".format(number, last_digit))
