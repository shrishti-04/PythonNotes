# 1.
multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
    
print(multiples)

# Another form
multiples = [ x*7  for x in range(1, 11)]
print(multiples)

# OUTPUT
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# 2. Find the length of each element of given list
languages = ['Java', 'Python', 'JavaScript', 'Perl', 'Ruby', 'Go', 'C']
lengths = [ len(language)   for language in languages ]
print(lengths)

# 3. Take out the multiples of 3 from the range of 1 to 100
n = [x  for x in range(1, 101)   if x % 3 == 0]
print(n)

# OUTPUT
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

# 4. The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. 
# Fill in the blanks in the function, using list comprehension

def odd_numbers(elements):
    elements = [x   for x in range(0, elements + 1)   if x%2 != 0]
    return elements

print(odd_numbers(10))
print(odd_numbers(5))
print(odd_numbers(1))
print(odd_numbers(-1))

# OUTPUT
# [1, 3, 5, 7, 9]
# [1, 3, 5]
# [1]
# []