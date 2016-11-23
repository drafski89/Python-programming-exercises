# Question 006

#Question:
#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.
#Example
#Let us assume the following comma separated input sequence is given to the program:
#100,150,180
#The output of the program should be:
#18,22,24

# Import the math library
import math

# Equation: Q = ((2 * C * D)/H) ^ (0.5)
# Constants
c = 50
h = 30

inputString = raw_input()
inputList = [value for value in inputString.split(',')]
outputValues = []

for position in inputList:
	outputValues = ((2 * c * position)/h) ** 0.5

print outputValues
