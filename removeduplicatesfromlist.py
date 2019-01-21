#23RD PROGRAM
# NOTE : This program remove duplicates from a list

myList = ['a','b','c','e','e','f']
#Inorder to remove duplicates we have to change the list to dictionary as "Dictionary" can't have duplicate members

myList = list(dict.fromkeys(myList))
print(myList)
myDict = dict(dict.fromkeys(myList))
for index,values in enumerate(myDict ,0):
    myDict[values] = values + str(index)
    #myDict[values] = values,index
print(myDict)