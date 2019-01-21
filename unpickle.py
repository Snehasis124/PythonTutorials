#16TH PROGRAM : UNPICKLE OBJECT

import pickle
unpicklefile = open("picklefile.py" , "rb")
unpicklelist = pickle.load(unpicklefile)
print("\n", unpicklelist)

#To print the items

for items in unpicklelist:
    print(items)


unpicklefile.close()