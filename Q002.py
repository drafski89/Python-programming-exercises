# Question 002

#Question:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

# This will do the factorial, but is not written as a method
inputNumber = 8
outputNumber = 1

while (inputNumber > 1):
	outputNumber = outputNumber * inputNumber
	inputNumber -= 1

print outputNumber

# Writing the factorial method
def factorial(inputNumber):
	outputNumber = 1
	while (inputNumber > 1):
		outputNumber = outputNumber * inputNumber
		inputNumber -= 1
	return outputNumber

# Implementing the factorial method
print "Enter a number to compute the factorial of: "
inputFromUser = int(raw_input())
print factorial(inputFromUser)