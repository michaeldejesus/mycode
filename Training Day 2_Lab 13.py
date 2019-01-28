#!/usr/bin/env python3

a_list=[1,2,3,4]
print("This original list...")
print(a_list)
print()

print("Item 1 in the list is: ", a_list[0])
print("Item 2 in the list is: ", a_list[1])
print("Item 3 in the list is: ", a_list[2])
print("Item 4 in the list is: ", a_list[3])
print()

reversed_list=a_list[-1::-1]
print("The reversed list...")
print(reversed_list)
print()

print("Now using the FOR loop to maneuver the entire list")
for x in reversed_list:
    print(x," ",end="")

