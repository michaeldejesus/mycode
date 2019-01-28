#!/usr/bin/env python3

a_list=[1,2,3,4]

print("The original list...")
print(a_list)
print()

for i, item in enumerate(a_list):
    a_list[i]=100

print(a_list)
