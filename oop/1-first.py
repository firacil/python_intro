#!/usr/bin/python3
class Cat:

    def __init__(self, name="", height=0):
        self.name = name
        self.height = height

    def miaw(self):
        print("{} that is cat".format(self.name))
    def drinks(self):
        print("{} the cat drinks".format(self.name))

def main():
    obje = Cat("baby", 23)
    obje.miaw()

    dum = Cat()
    dum.drinks()


main()
