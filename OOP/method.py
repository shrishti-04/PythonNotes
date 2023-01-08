# Write a code of Piglet which introduces itself adding method to class.

class Piglet:
    name = "Piglet"
    def speak(self):
        print('Oink Oink!! I am {} Oink Oink!!'.format(self.name))
    
    age = 0    
    def pig_years(years):
        return years.age*18
        
        
hamlet = Piglet()
hamlet.name = 'Hamlet'
hamlet.speak()
hamlet.age = 2
print(hamlet.pig_years())

petunia = Piglet()
petunia.name = 'Petunia'
petunia.speak()
petunia.age = 1.5
print(int(petunia.pig_years()))

# OUTPUT
# Oink Oink!! I am Hamlet Oink Oink!!
# 36
# Oink Oink!! I am Petunia Oink Oink!!
# 27



