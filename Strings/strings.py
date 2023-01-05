a = "Shrishti"
b = "ice cream"
print(a + " loves " + b)

# OUTPUT
# Shrishti loves ice cream

# Modify the double_word function so that it returns the same word repeated twice, 
# followed by the length of the new doubled word. For example, double_word("hello") should return hellohello10.

def double_word(word):
    words = word*2
    length = len(words)
    return words+str(length)

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

# Be my guest! Modify the first_and_last function so that it returns True 
# if the first letter of the string is the same as the last letter of the string, False if they’re different. 
# Remember that you can access characters using message[0] or message[-1].
# Be careful how you handle the empty string, which should return True since nothing is equal to nothing

def first_and_last(message):
    if message == "" or message[0] == message[-1]:
        return True
    else:
        return False
    
print(first_and_last("else"))  #True
print(first_and_last("tree"))  #False
print(first_and_last(""))      #True

# Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious".

word = "supercalifragilisticexpialidocious"
print(word.index("x"))

# OUTPUT
# 21

# It returns the initials of the words contained in the phrase received, in upper case. 
# For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.

def initials(phrase):
    
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
        
    return result

print(initials('Universal Serial Bus')) #USB
print(initials('Local Area Network')) #LAN
print(initials('Operating System')) #OS


# The format_address function separates out parts of the address string into new strings:
# house_number and street_name, and returns: "house number X on street named Y". 
# The format of the input string is: numeric house number, followed by the street 
# name which may contain numbers, but never by themselves, and could be several words long. 
# For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.

def format_address(address_string):
      # Declare variables
  house_number = ''
  street_name = ""
  # Separate the address string into parts
  x = address_string.split()
  # Traverse through the address parts
  for y in x:
    # Determine if the address part is the
    # house number or part of the street name
    if (y.isdigit()):
      house_number += y
    else:
      street_name += y
      street_name += " "
  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"