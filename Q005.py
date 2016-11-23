# Question 005

#Question:
#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class StringHandling(object):
	def __init__(self):
		self.string = ""
	def getString(self):
		print "Enter a string:"
		self.string = raw_input()
	def printString(self):
		print self.string.upper()

def test(StringHandling):
	testingClass = StringHandling
	testingClass.getString()
	testingClass.printString()
	
testObject = StringHandling()
test(testObject)