#  Example1: print_prime_factors function print all the prime factors of a number. A prime factor is a number that is prime and divides another without a remainder.
def print_prime_factors(number):
      # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)

# Output:
# 2
# 2
# 5
# 5

# Example2: The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5.
# An additional requirement is that the result is not to exceed 25, which is done with the break statement.
# Fill in the blanks to complete the function to satisfy these conditions.

def multiplication_table(number):
    	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number * multiplier 
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24