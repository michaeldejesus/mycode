#!/usr/bin/env python3
prompt_name_msg="Please enter you full name:"
user_name = input(prompt_name_msg)
while(user_name==''):
    user_name=input(prompt_name_msg)
print()
print("Welcome to the wonderful world of Python,", user_name)
print()
