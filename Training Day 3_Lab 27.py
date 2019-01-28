#!/usr/bin/env python3

s1 = "%to,two,too!"

s2 = s1.strip('%!')
s3 = s1.strip(",")

print("s1: ", s1)
print("s2: ", s2)
print("s3: ", s3)

s4 = ",,anotherstring,,"
s5 = s4.strip(',')
print("s4: ", s4)
print("s5: ", s5)

s6 = ''
s7 = s6.strip(' ')
print("s6: ", s6)
print("s7: ", s7)