# Lesson 1: Write a program to find all numbers divisible by 7 but not multiples of 5,
# within the range 2000 and 2300 (including 2000 and 2300). 
# The resulting numbers will be printed as a string on one line, using comma.

# Solution
x=[] # Create an empty list to save the results
for i in range(2000, 2300): # Go through all the numbers in the range from 2000 to 2300
    if (i%7==0) and (i%5!=0): # Check if number i is divisible by 7 and not a multiple of 5
        x.append(str(i)) # If true, then add number i to the result list
print (','.join(x)) # Print the result list to the screen, elements separated by commas