testVariable = 100


def valueTest(testVariable):
	if testVariable < 1000:
		print('testVariable is less than 1000')
	else:
		print('testVariable is greater than 1000')




valueTest(testVariable)

testVariable = 5000
valueTest(testVariable)


#else if is represented by elif

def whereTheIntStands(val):

	if val > 10:
		print('greater than 10')
	elif val == 10:
		print('equal to 10')
	else:
		print('less than 10') 


whereTheIntStands(11)
whereTheIntStands(10)
whereTheIntStands(9)


