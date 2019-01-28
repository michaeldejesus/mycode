#!/usr/bin/env python3

import os

file_name=input("Please enter a file name to read from:")

while not os.path.exists(file_name):
    print("The Following file does not exist:", file_name)
    file_name=input("Please enter a file name to read from: ")

print("This input file exists: ", file_name)

in_file = open(file_name, 'r')

line_count=0

for a_line in in_file:
    print(a_line, end='')
    line_count+=1

in_file.close()
