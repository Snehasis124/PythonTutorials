#19TH PROGRAM  - Regrex.py

import re

#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#RegEx can be used to check if a string contains the specified search pattern#

#FIND ALL FUNCTION
str = "The rain in Spain"
x = re.findall("ai", str)
print(x)
#If a search is found , it returns a list else it returns an empty list

#SEARCH FUNCTION
y = re.search("rain", str )
print(y.start())
#For NONE output , you cannot use the start() function

#SPLIT FUNCTION
z = re.split("\s", str)
a = re.split("\s",str,1)
print(z)
print (a)

# #SUB FUNCTION : THE SUBSTITUTE FUNCTION
# b = re.sub("\s" , "9" , str)
# print(b)

# NO OF REPITIONS
c = re.findall(r"ain\b" , str)
if (c!= None):
    print("No of repitions",len(c))


# Where is "a" in the string

d = re.findall( "rain" , str)
print(d)

e = re.findall("^T.*n" , str)
print("printing characters", e)



#To search the number of occurences of words starting with t and ending with n

str1 = "Hello we have an meeting at 8pm on 68 oct"
g = re.findall("[0-9][0-9]",str1)
print("Time is ", g)


#Figuring out the date and time from String
from datetime import datetime as dt
str2 = "Meet us at 080912"
d = re.findall("[0-9][0-9]" , str2)
e = dt.strptime(''.join(d) , "%H%M%S" ).time()
print(d)
print(e)


