class Person:
    # class is a blueprint for create object
    
    def __init__(self, name, age):
        self.name = name # attribute is variables that store data for an object
        self.age = age
        
    # Method: describe behaviour of an object
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Create an object(instance) of person class
person1 = Person("Firaol", 22)


# let's access attribute and call methods
print(person1.name) # output: Firaol
print(person1.greet()) # output: will be return of method    
    