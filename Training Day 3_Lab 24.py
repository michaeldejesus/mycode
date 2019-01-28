#!/usr/bin/env python3

myage=int(input('Enter you age: '))

if myage<13:
    print("WOW! You can still buy a kids meal!")
elif myage>=13 and myage<20:
    print("WOW! You are a teenager. Enjoy those French fries now!")
elif myage>=20 and myage<24:
    print("Welcome to the wonderful adult world. Get a job!")
elif myage>64:
    print("Congradulation! You are eligible for retirement!")
else:
    #Calculate how many years the user has to work!
    i = 65-myage
    print("Sorry! You have to work", i, "more years before retiring.")
