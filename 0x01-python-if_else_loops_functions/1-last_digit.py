#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    pos = number * -1
    ld = pos % 10
    ld = ld * -1
else:
    ld = number * 10
    print("Last digit of " + str(number) + " is " + str(ld), end="")
if ld > 5:
    print(" and is greater than 5")
elif ld == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
