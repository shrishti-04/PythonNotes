# 1. Find the number of characters in given tuple and find the average of the length of the given tuple

animals = ['lion', 'tiger', 'deer', 'bear', 'snake']
chars = 0
for animal in animals:
    chars += len(animal)

print('Total characters = {}, Average length = {}'.format(chars, chars/len(animals)))

# OUTPUT
# Total characters = 22, Average length = 4.4

# 2. Denote the index of the given array using the enumerate function instead of range function.

winners = ['Shrishti', 'Ronaldo', 'Messi', 'Austin']
for index, winner in enumerate(winners):
    print('{} - {}'.format(index + 1, winner))

# OUTPUT
# 1 - Shrishti
# 2 - Ronaldo
# 3 - Messi
# 4 - Austin

# 3. In a tuple you have given name as well as email, so therefore write it in the format Shrishti <Shrishti@gmail.com>

def full_name_emails(people):
    result = []
    for email, person in people:
        result.append('{} <{}>'.format(person, email))
    return result

print(full_name_emails( [('Shrishti@gmail.com', 'shrishti'),
                         ('Steve@gmail.com', 'steve'),
                         ('Nancy@gmail.com', 'Nancy'),] ))

# OUTPUT
# ['shrishti <Shrishti@gmail.com>', 'steve <Steve@gmail.com>', 'Nancy <Nancy@gmail.com>']

# 4. Try out the enumerate function for yourself in this quick exercise. 
# Complete the skip_elements function to return every other element from the list, 
# this time using the enumerate function to check if an element is in an even position or an odd position.

def skip_elements(elements):
    	# code goes here
	result = []
	for i, element in enumerate(elements):
		if (i % 2 == 0):
			result.append(element)
	return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# OUTPUT
# ['a', 'c', 'e', 'g']
# ['Orange', 'Strawberry', 'Peach']