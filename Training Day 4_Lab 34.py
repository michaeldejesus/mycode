#!/usr/bin/env python3

def trad_fib(n):
    a=1
    b=1

    while b<n:
        print(a, end=" ")
        old_b=b
        b=a+b
        a=old_b
    print(a, end=" ")
    print()
    return a

x=trad_fib(400)
print("The Fibonacci number that is less than 400...", x)
print()

x=trad_fib(2000)
print("The Fibonacci number that is less than 2000...", x)
