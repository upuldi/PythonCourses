emptyTuble = ()
print(emptyTuble)

tupleOfSizeOne = ('a',)
tupleOfSizeTwo = ('a',100)
anotherTuple = (10,400)

print(tupleOfSizeOne)
print(tupleOfSizeTwo)

#we can add tuples
bothTuples = tupleOfSizeOne + tupleOfSizeTwo
print(bothTuples)

#accessing values from a tuple
print(tupleOfSizeTwo[0])
print(tupleOfSizeTwo[0:])

#In tuples you can not change the values once they are assigned
