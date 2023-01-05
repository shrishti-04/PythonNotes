# Using the "split" string method from the preceding lesson, complete the 
# get_word function to return the {n}th word from a passed sentence. 
# For example, get_word("This is a lesson about lists", 4) should return "lesson", which is the 4th word in this sentence.
# Hint: remember that list indexes start at 0, not 1. 

def get_word(sentence, n):
    	# Only proceed if n is positive 
	sentence = sentence.split(" ")
	if n <= len(sentence) and n > 0:
		# Only proceed if n is not more than the number of words 
		return(sentence[n-1])
	else:
		  return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing


# The skip_elements function returns a list containing every other element 
# from an input list, starting with the first element. 
# Complete this function to do that, using the for loop to iterate through the input list.

def skip_elements(elements):
    	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for n in elements:
		# Does this element belong in the resulting list?
		if i % 2 == 0:
			# Add this element to the resulting list
			new_list.append(n)
		# Increment i
		i += 1

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []