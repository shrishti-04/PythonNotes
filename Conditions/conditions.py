# Q1.) The is_positive function should print True if the number received 
# is positive, otherwise it prints None.

def is_positive(number):
    if number > 0:
       print("True")
    else:
        print("None")
is_positive(5)

# OUTPUT: True

# Q2  The is_even function should print True if the number received 
# is even, otherwise it prints None.(Without using else statement)

def is_even(numbers):
    if numbers % 2 == 0:
        return True
    return False
print(is_even(7))
