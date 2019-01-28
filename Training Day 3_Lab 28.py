#!/usr/bin/env python3

s1 = "Donald, Victoria, Andrew, Sarah"
s2 = "Donald  Victoria  Andrew  Sarah"
s3 = "Donald@Victoria@Andrew@Sarah"

print("s1: ", s1)
print("s2: ", s2)
print("s3: ", s3)

list1 = s1.split(',')
print("list1: ", list1)

list2 = s2.split()
print("list2: ", list2)

list3 = s3.split('@')
print("list3: ", list3)
ope