#!/usr/bin/python3
letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters)
print(letters[0])

# let's remove some value.

letters[1:5] = []
print(letters)

# replace all

letters[:] = []
print(letters)
