# Lesson 2: Write a program that can calculate the factorial of a given number.
# The result is printed as a string on one line, separated by commas.
# For example, given number is 8 then the output should be 40320.

x = 8
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
print (fact(x))