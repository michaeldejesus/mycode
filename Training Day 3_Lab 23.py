#!/usr/bin/env python3

age=40
print('Age = '+str(age)+"...")
if age > 21 and age <100:
    print('WOW! You are old.')

print()
age=18
print('Age = '+str(age)+"...")
if age <=21:
    years=21 - age
    print('Sorry! You have to wait '+str(years)+' years to rent a car')

print()
age=22
print('Age = ' +str(age)+"...")
if age<12:
    print("You can still buy a kids meal")
else:
    print("Sorry! You cant buy a kids meal anymore!")
