#8TH PROGRAM
#THIS PROGRAM SHOWS THE MORE DETAILED USAGE OF VARIABLES IN FORM OF LISTS , DICTIONARY & TUPLES
# NOTE LISTS : Lists - exactly what they say they are. Lists of values. Each one has a number, in ascending order and beginning from zero. Value can be removed and new ones added in when needed.
# NOTE TUPLES : Tuples - similar to lists but the values cannot be changed. Make sure you give them the right value first time around because you are stuck with it.  Each value is numbered, beginning at zero.
# NOTE DICTIONARY : Dictionaries – quite similar to what you would expect them to be – a dictionary. This includes an index of all the words and a definition of each one. In the Python language, words are called “keys” and the definitions are called “values”. Values are not numbered in dictionaries ad they are not in any particular order. Keys can be added, removed or changed in a dictionary.
# NOTE List is a collection which is ordered and changeable. Allows duplicate members.
# NOTE Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# NOTE Set is a collection which is unordered and unindexed. No duplicate members.
# NOTE Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


# EXAMPLE OF TUPLES : Denoted by Paranthesis
months = ('January','February','March','April','May','June', \
'July','August','September','October','November',' December')
print(months)
#TODO LINE CONTINUATION CHARACTER "\" isn't working , kindly check

#EXAMPLE OF LIST : Denoted by Square brackets
cats = ['Smokey', 'Josie', 'Jemima', 'Suzy', 'Tom']
print(cats)
print(cats[2])





#To add items to list : Syntax used : listname.append()
cats.append("Sukey")
print(cats)
#To remove items from list : Syntax Used : del(listname[index])
del(cats[1])
print(cats)

# TODO EXAMPLE OF DICTIONARY : DENOTED BY CURLY BRACES

# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 

# Creating a Dictionary 
# with Integer Keys 
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 

# Creating a Dictionary 
# with Mixed keys 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 

# Creating a Dictionary 
# with dict() method 
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 

# Creating a Dictionary 
# with each item as a Pair 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 


