#!/usr/bin/env python3

list1 = ['ZZ', 'YY', 'XX', 'WW', 'VV']
print("list1: ", list1)

sep_string = " , "
s1 = sep_string.join(list1)
print("s1: ", s1)

sep_string = "  "
s2 = sep_string.join(list1)
print("s2: ", s2)

sep_string = " - "
s3 = sep_string.join(list1)
print("s3: ", s3)

