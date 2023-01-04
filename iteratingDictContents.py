file_counts = {'jpg': 12, 'txt': 15, 'csv': 23, 'py': 30}
for extension in file_counts:
    print(extension)
    
# OUTPUT
# jpg
# txt
# csv
# py

for ext, value in file_counts.items():
    print('There are {} files with extension {}'.format(value, ext))
    
# OUTPUT
# There are 12 files with extension jpg
# There are 15 files with extension txt
# There are 23 files with extension csv
# There are 30 files with extension py

# Extract keys from dictionary
print(file_counts.keys())
# OUTPUT
# dict_keys(['jpg', 'txt', 'csv', 'py'])

# # Extract values from dictionary
print(file_counts.values())
# OUTPUT
# dict_values([12, 15, 23, 30])

# Complete the code to iterate through the keys and values of the cool_beasts 
# dictionary. Remember that the items method returns a tuple of key, 
# value for each element in the dictionary.

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for mammal, parts in cool_beasts.items():
    print("{} have {}".format(mammal, parts))
    
# OUTPUT
# octopuses have tentacles
# dolphins have fins
# rhinos have horns

def lettercount(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
        
    return result

print(lettercount('aaaaaa'))
print(lettercount('aaabbbccc'))
print(lettercount('I love to eat chicken a lot very much'))

# OUTPUT
# {'a': 6}
# {'a': 3, 'b': 3, 'c': 3}
# {'I': 1, ' ': 8, 'l': 2, 'o': 3, 'v': 2, 'e': 4, 't': 3, 'a': 2, 'c': 3, 'h': 2, 'i': 1, 'k': 1, 'n': 1, 'r': 1, 'y': 1, 'm': 1, 'u': 1}