#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
last_digit = number % 10 if number > 10 else number % -10
print(f"Last digit of {number} is {last_digit} and is ", end="")
if last_digit == 0:
    print("0")
elif last_digit < 6:
    print("less than 6 and not 0")
elif last_digit > 5:
    print("greater than 5")
