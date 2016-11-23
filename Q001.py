# Question 001

#Question:
#Write a program which will find all such numbers which are divisible by 7
#but are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

testNumber = 2000
finalAnswerSet = ""

for testNumber in range(2000,3200,1):
	if (testNumber % 7 == 0 and testNumber % 5 != 0):
		finalAnswerSet = finalAnswerSet + ",{}".format(testNumber)
print finalAnswerSet