#9TH PROGRAM 
# THIS PROGRAM WILL HELP IN ACCESSING DICTIONARY ITEMS AND PERFROM CERTAIN OPERATIONS WITH DICTIONARY

ages = {}  #EMPTY DICTIONARY

ages["Micky"] = 24
ages["Lucky"] = 25

print(ages)

keys = ages.keys # .keys prints all the keys avaialble in Dictionary
print(keys)

values = ages.values # .values prints all the values avaialble in Dictionary
print(values) 

print(sorted(ages))
# NOTE Unable to sort print(sorted(ages.values)) 

print(ages.values) # Prints the values

# NOTE has_key() has been replaced by "in" in Python 3 , You can access like below. 
# Syntax : "Values" in "dict" 
if("Micky" in ages):
    print("Micky is there")
else:
    print("Micky is not there")

print(len(ages)) # Print the length of the dictionary

#Adding new item
# New initialization 
ages = {"Snehasis" : "24" , "Sradhasis" : 25}
print(ages)

# New members

ages["LKP"] = 45 # Here value is saved as int
if("LKP" in ages):
    updatedValue = ages.get("LKP") + 10 
    print("Updated Value = " , updatedValue)
print(ages)


ages["JYOTI"] = "38" # Here value is saved as string
if("JYOTI" in ages):
    updatedValue = ages.get("JYOTI") + " New Age"
    print("Updated Value = " , updatedValue)
print(ages)


