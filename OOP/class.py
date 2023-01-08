class Apple:
    pass

class Apple:
    color = ''
    flavor = ''
    
jonagold = Apple()
jonagold.color = 'red'
jonagold.flavor = 'sweet'

print(jonagold.color)
print(jonagold.flavor)

# OUTPUT
# red
# sweet

golden = Apple()
golden.color = 'yellow'
golden.flavor = 'soft'

print(golden.color)
print(golden.flavor)

# OUTPUT
# yellow
# soft

# Write a code to make it print a poem.

class Flower:
    color = 'unknown'

rose = Flower()
rose.color = 'red'

violet = Flower()
violet.color = 'blue'

this_pun_is_for_you = 'Sugar is sweet and so you are..'

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you)

# OUTPUT
# Roses are red,
# violets are blue,
# Sugar is sweet and so you are..


# We have two pieces of furniture: a brown wood table and a red leather couch. 
# The creation of each Furniture class instance, so that the describe_furniture function 
# can format a sentence that describes these pieces as follows: "This piece of furniture is made of {color} {material}"

class Furniture:
    color = ""
    material = ""
    	

table = Furniture()
table.color = 'brown'
table.material = 'wood'

couch = Furniture()
couch.color = 'red'
couch.material = 'leather'

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"