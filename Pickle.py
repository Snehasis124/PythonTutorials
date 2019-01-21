#15TH PROGRAM
#Here we learn how to pickle an object (i.e. putting an object into a file)
#To pickle , we have to import pickle module

import pickle
picklelist = [1,"two","three",4,5,"countitOut"]

picklefile = open('/Users/snehasispanda/Desktop/Python_Programs/picklefile.py' , 'wb' )
#Note the "wb" in above code , it means the data has to be written in binary code (bytes) rather than normally
pickle.dump(picklelist,picklefile)
picklefile.close
