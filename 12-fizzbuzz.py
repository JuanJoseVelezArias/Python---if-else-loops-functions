#!/usr/bin/python3 
def fizzbuzz():
    for i in range (100):
        i += 1
        if i % 3 == 0:
            print("Fizz", end = " ")
        elif i % 5 == 0:
            print("Buzz", end = " ")
        elif i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz", end = " ")
        else:
            print(i, end = " ")
    print()
          
            
        