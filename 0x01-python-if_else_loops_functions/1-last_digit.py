#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = int(str(number)[-1])
if number > 0 and digit == 0:
    print(f"Last digit of {number} is {digit} and is 0")
elif number > 0 and digit > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
elif number > 0 and (digit < 6 and digit > 0):
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
else:
    digit = digit * -1
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
