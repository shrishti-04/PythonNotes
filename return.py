# Q1.) You have two areas of triangles add them together by returning the values.

def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,7)
area_b = area_triangle(4,8)

result = area_a + area_b
print("Therefore the total area of the triangle is: " + str(result))

# OUTPUT: Therefore the total area of the triangle is: 33.5

# Q2.) Use the get_seconds function to work out the amount
# of seconds in 2 hours and 30 minutes, then add this number to the amount of seconds
# in 45 minutes and 15 seconds. Then print the result.

def get_seconds(hours, minutes, seconds):
      return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)

# OUTPUT: 11715

# Q3. Functions also reduces the amount of code. For example:

# june_days = 30
# print("June has " + str(june_days) + " days")
# july_days = 30
# print("July has " + str(july_days) + " days")

# OUTPUT

# June has 30 days
# July has 31 days

def month_days(month, days):
    print(str(month) + " has " + str(days) + " days")

month_days("July", 30)
month_days("July", 31)

# OUTPUT

# June has 30 days
# July has 31 days