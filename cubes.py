#!/usr/bin/python3
cubes = [1, 8, 27, 65, 125]
4 ** 3 # the cube root of 4 is 64, not 65! so we will replace it.

cubes[3] = 64 # replaced
print(cubes)
''' let's append a value to cubes
    we will do for bothe cube of 6 and 7'''

cubes.append(6 ** 3)
cubes.append(7 ** 3)

# let's print after appending value

print(cubes)
