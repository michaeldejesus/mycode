#!/usr/bin/env python3

def fib(n):
    a,b=0,1
    while b<n:
        print(b, end=" ")
        a, b=b, a+b

    print()
    return a

x=fib(100)
print("The Fibonacci number that is less that 100...", x)
print()

x=fib(500)
print("The Fibonacci number that is less that 500...", x)
print()

x=fib(2000)
print("The Fibonacci number that is less that 2000...", x)
print()
