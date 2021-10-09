def intro(a):
    print("My name is " + a)
intro("Shrishti")

# Output: My name is Shrishti

# If there are two parameters

def info(name, address):
    print("Hello guys!! My name is " + name)
    print("I stay in " + address)

info("Shrishti", "Mumbai")

# Output: Hello guys!! My name is Shrishti
#         I stay in Mumbai

# Let's try one question

# Flesh out the body of the print_seconds function so that it
# prints the total amount of seconds given the hours, minutes, and seconds function parameters.
# Remember that there are 3600 seconds in an hour and 60 seconds in a minute.

# Solution:

def print_seconds(hours, minutes, seconds):
    print(hours*3600 + minutes*60 + seconds)

print_seconds(1,2,3)