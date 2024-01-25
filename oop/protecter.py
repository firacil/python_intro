#!/usr/bin/python3
class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

        @property
        def height(self):
            print("retriveing the height")

            return slef.__height

        @height.setter
        def height(self, value):
            if value.isdigit():
                self.__height = value
            else:
                print("only numbers")

        @property
        def width(self):
            print("Retriving the width")

            return self.__width

        @width.setter
        def width(self, value):

            if value.isdigit():
                self.__width = value
            else:
                print("only numbers for width")

        def getArea(self):
            return int(self.__width) * int(self.__height)



def main():
    asq = Square()

    height = input("Enter Height : ")
    width = input("Enter Width : ")

    asq.height = height
    asq.width = width

    print("Height :", asq.height)
    print("Width :", asq.width)

    print("The Area is :", asq.getArea())

main()
