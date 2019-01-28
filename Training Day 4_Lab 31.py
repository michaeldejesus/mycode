#!/usr/bin/env python3

in_file = open('infile_001.txt', 'r')
line_count=0

for a_line in in_file:
    print(a_line, end='')
    line_count+=1

in_file.close()

print()
print("The number of lines contained in this file were: ", line_count)
print()

tmp_lc=line_count
tmp_lc=tmp_lc + 1
print("The value of the variable tmp_lc: ", tmp_lc)
