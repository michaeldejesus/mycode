#!/usr/bin/env python3

def get_user_age():
    prompt_age_msg = "Please enter your age: "
    user_str=input(prompt_age_msg)
    if(user_str.isdigit()):
        user_age=int(user_str)
    else:
        user_age=0
    return user_age


def print_age_output(myage):
    if myage < 13:
        print("WOW! You can still buy a kids meal!")
    elif myage >= 13 and myage < 20:
        print("WOW! You are a teenager. Enjoy those French fries now!")
    elif myage >= 20 and myage < 24:
        print("Welcome to the wonderful adult world. Get a job!")
    elif myage > 64:
        print("Congradulation! You are eligible for retirement!")
    else:
        # Calculate how many years the user has to work!
        i = 65 - myage
        print("Sorry! You have to work", i, "more years before retiring.")


def get_user_name():
    prompt_name_msg = "Please enter your name. Enter Q to quit: "
    user_name = input(prompt_name_msg)
    while (user_name.upper() != "Q"):
        if user_name.isnumeric():
            user_name = input(prompt_name_msg)
        elif user_name.count('-'):
            user_name = input(prompt_name_msg)
        elif user_name.upper() == "":
            user_name = input(prompt_name_msg)
        else:
            print("Now processing user name...", user_name)
            myage = get_user_age()
            while (myage <= 0):
                myage = get_user_age()

            print_age_output(myage)
            print()

            user_name = input(prompt_name_msg)
            print()

my_user_name = get_user_name()
