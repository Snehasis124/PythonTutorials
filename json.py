import json

# If you have a JSON String , you can parse it using json.loads() function
# Convert JSON to Python -> Result will be a python dictionary

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}' 

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


#You can convert Python objects of the following types, into JSON strings:

# dict :     print(json.dumps({"name": "John", "age": 30}))
# list :     print(json.dumps(["apple", "bananas"]))
# tuple :    print(json.dumps(("apple", "bananas")))
# string :   print(json.dumps("hello"))
# int :      print(json.dumps(42))
# float :    print(json.dumps(31.76))
# True :     print(json.dumps(True))
# False :    print(json.dumps(False))
# None   :   print(json.dumps(None))


