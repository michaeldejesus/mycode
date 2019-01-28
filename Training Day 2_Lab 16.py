#!/usr/bin/env python3

cels_list=[-2,0,5,10,15,25,32,38,40]
fahr_list=[]

for c in cels_list:
    f_temp=c*1.8+32.0
    fahr_list.append(f_temp)

print("The Celsius list: ",cels_list)
print("The Fahrenheit list: ",fahr_list)
print()

i=cels_list.pop()


print("After popping one item from the pop_list...")
print(i)
print("The Celsius list: ",cels_list)

