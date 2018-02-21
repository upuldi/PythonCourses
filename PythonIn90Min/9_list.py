listVariable = [1,2,3,4,5]
print(listVariable)

#list can have diffrent types
anotherList=[1,1.1,True,"String"]
print(anotherList)

#Joining Lists
joinList = listVariable + anotherList
print(joinList)

#adding another value
print(listVariable + [6])

#accessing the list
firstElementOfThelist = listVariable[0]
secondElementOfTheLlist = listVariable[1]

print(firstElementOfThelist)
print(secondElementOfTheLlist)

#selecting a range 
sublisting = listVariable[2:4]
print(sublisting)

#Reassigning values
listVariable[4] = 500
print(listVariable)

#append is same as joining lists

listVariable.append(100)
print(listVariable)