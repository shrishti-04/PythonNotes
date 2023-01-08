class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    
class Apple(Fruit):
    pass

class Mango(Fruit):
    pass

granny_smith = Apple('Green', 'tard')
carnelia = Mango('Red', 'sweet')

print('Granny Smith bought Apples which were in {} color and were {} in flavor'.format(granny_smith.color, granny_smith.flavor))
print('Whereas her grand daughter bought Mangoes which were in {} color and were {} in flavor'.format(carnelia.color, carnelia.flavor))

# OUTPUT
# Granny Smith bought Apples which were in Green color and were tard in flavor
# Whereas her grand daughter bought Mangoes which were in Red color and were sweet in flavor

# Write a code which makes animals sound.

class Animal:
    sound = ''
    def __init__(self, name):
        self.name = name
    def speak(self):
        print('{sound} I am {name}!! {sound}'.format(name = self.name, sound = self.sound))
        
class Pigglet(Animal):
    sound = 'Oink'
    
hamlet = Pigglet('Hamlet')
hamlet.speak()

class Dog(Animal):
    sound = 'Bow'
    
tommy = Dog('Tommy')
tommy.speak() 

# OUTPUT
# Oink I am Hamlet!! Oink
# Bow I am Tommy!! Bow


# Below we have a base class called Clothing. Together, let’s create a second class, called Shirt, 
# that inherits methods from the Clothing class. 

class Clothing:
    material = ''
    def __init__(self, name):
        self.name = name
    def check_material(self):
        print('This {} is made up of {}'.format(self.name, self.material))
        
class Shirt(Clothing):
    material = 'Cotton'
        
polo = Shirt('Polo')
polo.check_material()

# OUTPUT
# This Polo is made up of Cotton