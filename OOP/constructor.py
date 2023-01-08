# In this code, there's a Person class that has an attribute name, which gets set when constructing the object.
# 1) when an instance of the class is created, the attribute gets set correctly, and 
# 2) when the greeting() method is called, the greeting states the assigned name.

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return print('Hello!! my name is {}'.format(self.name))
    
some_person = Person('Shrishti')
print(some_person.greeting())

# OUTPUT
# Hello!! my name is Shrishti


# Use of string constructor
class Apple:
    def __init__(self, color, flavour):
        Apple.color = color
        Apple.flavour = flavour
        
    def __str__(self):
        return 'This is {} color Apple and its flavour is {}'.format(self.color, self.flavour)
    
Jonagold = Apple('red', 'sweet')
print(Jonagold)

# OUTPUT
# This is red color Apple and its flavour is sweet