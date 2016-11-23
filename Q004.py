# Question 004

#Question:
#Write a program which accepts a sequence of comma-separated numbers from console 
#and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

# Read the list of numbers from the user
print "Enter a list of numbers to create a list and tuple of"
inputString = raw_input()

# Split on the commas
list = inputString.split(',')

# Create the tuple list
tuple = tuple(list)

# Print the results to the user
print "\nThe list is:"
print list
print "The tuple is:"
print tuple