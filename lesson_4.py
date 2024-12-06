# lesson 4: Write a program that accepts a string of numbers, separated by commas, from the console, producing a list and a tuple containing every number.

values = "20,17,95,43,18,92"
l = values.split(",")
t = tuple(l)

print ("l = ",l)

print ("t = ", t)