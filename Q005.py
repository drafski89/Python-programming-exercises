# Question 005

#Question:
#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

# Create a class named StringHandling
class StringHandling(object):
	# The init will initialize a string variable in the class
	def __init__(self):
		self.string = ""
	# getString(self) will read the input from the user
	def getString(self):
		print "Enter a string:"
		self.string = raw_input()
	# printString(self) will print the string in uppercase
	def printString(self):
		print self.string.upper()

# Define a test method that expects a StringHandling class type
def test(testingClass):
	# Call the getString method
	testingClass.getString()
	# Call the printString method
	testingClass.printString()
	
# Create a test object called testObject
testObject = StringHandling()
# Test the testObject with the test method
test(testObject)