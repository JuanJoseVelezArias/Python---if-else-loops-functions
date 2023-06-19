#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = int(str(number)[-1])
if number < 0:
    ld = -ld
elif ld < 6 and ld != 0:
    print ("Last digit of", number, "is", ld, "and is less than 6 and not 0")
elif ld > 5 and ld != 0:
    print ("Last digit of", number, "is", ld, "and is greater than 5")
elif ld == 0:
    print ("Last digit of", number, "is", ld, "and is 0")