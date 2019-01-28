#!usr/bin/env python3

global prompt_age_msg
prompt_age_msg= "Please enter your age: "

def get_user_age():
    user_str=input(prompt_age_msg)
    if(user_str.isdigit()):
        user_age=int(user_str)
    else:
        user_age=0
    return user_age

my_user_age=get_user_age()
while(my_user_age<=0):
    prompt_age_msg= "Wrong format entered. Enter an integer value for your age."
    my_user_age=get_user_age()

print()
print("Your age is:",my_user_age,"year old.")
print()
