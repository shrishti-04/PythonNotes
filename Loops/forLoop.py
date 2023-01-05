# Example1: Sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x (not included).
# Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285

# Example2: In math, the factorial of a number is defined as the product of an integer and all the integers below it.
# For example, the factorial of four (4!) is equal to 1*2*3*4=24.

def factorial(n):
    result = 1
    for i in range(n):
        result = n*factorial(n-1)
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

# print the first 10 factorials (from 0 to 9) with the corresponding number. 
# Remember that the factorial of a number is defined as the product of an integer and all integers before it.
# For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.

def factorial(n):
    result = 1
    for x in range(1, n+1):
        result = result * x
    return result

for n in range(0, 10):
    print(n, factorial(n))