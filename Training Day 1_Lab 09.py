#!usr/bin/env python3
print("The ORD function...")
for myChar in 'abcdefgh':
    myNum= ord(myChar)
    print(myChar, myNum)

    print()
    print("The CHR function...")
for i in range(65,75):
        myChar=chr(i)
        print(i, myChar)

print()
print("The HEX function...")
for j in range(1,17):
    myHexValue=hex(j)
    print(j, myHexValue)

