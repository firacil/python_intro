#!/usr/bin/python3
""" usage of *args"""

def testit(formal_arg, *argv):
    print("first normal arg:", formal_arg)
    for arg in argv:
        print("another arg through *argv :", arg)

testit('firaol', 'mk', 'python', 'testing', 'argv')
