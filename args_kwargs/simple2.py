#!/usr/bin/python3
""" let's check for **kwargs"""

def testkw(**kwargs):
    if kwargs is not None:
        for k, v in kwargs.items():
            print("{} == {}".format(k, v))

testkw(name="Firaol")
