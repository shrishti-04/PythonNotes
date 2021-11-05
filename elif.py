# Q1.The number_group function should return "Positive" if the number received is positive,
# "Negative" if it's negative, and "Zero" if it's 0.

def number_group(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(number_group(5))
print(number_group(0))
print(number_group(-4))

# OUTPUT: Positive
#         Zero 
#         Negative

# Q2. A company wants you to create a username for employers and that username length should be more then three and less than 15. You
# If it is more than 15 and less than 3 then it should return invalid username or else it will be a valid username.

def create_username(username):
    if len(username) < 3:
        return "Invalid Username"
    elif len(username) > 15:
        return "Invalid Username"
    else:
        return "Valid Username"

print(create_username("st"))
print(create_username("Shrishti"))
print(create_username("Shrishti Ashok Tiwari"))

# OUTPUT: Invalid Username
#         Valid Username
#         Invalid Username

    
