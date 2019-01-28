#!/usr/bin/env python3

#import os

in_file = open('infile_002', 'r')
line_count = 0
total_glucose = 0
total_insulin_dose = 0

sugar_levels_list = in_file.readlines()

print("***SUGAR LEVEL LIST BELOW***")
print(sugar_levels_list)
print()

print('###First Element in the Sugar Levels List###')
print()

for a_line in sugar_levels_list:
    print(a_line, end='')
    tmp_list = a_line.split(',')
    glucose_value = tmp_list[2]
    insulin_dose = tmp_list[3]
    total_glucose += int(glucose_value)
    total_insulin_dose += int(insulin_dose)
    line_count += 1
    print()
    print("Glucose Value=", glucose_value)
    print()

print()
print("Total Glucose = ", total_glucose)
print("Total Count = ", line_count)
print("Average Glucose = ", total_glucose/line_count)
print("Average Insulin Dose = ", total_insulin_dose/line_count)
print()
print("*DONE READING THE FILE*")
in_file.close()
