#!/usr/bin/python3
# fibonacci series:
# sum of two elements defines the next

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
