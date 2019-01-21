import os #To create and remove directory

#we can read the file in two modes : t : text mode , b: binary mode

# NOTE : Create a new directory
if(os.path.exists("/Users/snehasispanda/Desktop/DemoFolderForPython")):
    print("Folder exists , we will create a file")
else:
    try:
        x = os.mkdir("/Users/snehasispanda/Desktop/DemoFolderForPython")
    except NameError as Name:
        print("Error : " , Name)

# NOTE : Create a File
if(os.path.exists("/Users/snehasispanda/Desktop/DemoFolderForPython")):
    print("File exists")
else:
    try:
       createAfile  = open("/Users/snehasispanda/Desktop/DemoFolderForPython/demo.txt" , "x")
    except NameError as Name:
        print("Error : " , Name)
        print("File created" , createAfile)

# NOTE : Writing to that file
writeToFile = open("/Users/snehasispanda/Desktop/DemoFolderForPython/demo.txt" , "w")
writeToFile.write("Hello !! This is the first statement written")
writeToFile.close()

# NOTE : Appending information 

appendingInformation = open("/Users/snehasispanda/Desktop/DemoFolderForPython/demo.txt" , "a")
appendingInformation.write("\n Adding second line")
appendingInformation.close()


# NOTE : Reading from file
readFromFile = open("/Users/snehasispanda/Desktop/DemoFolderForPython/demo.txt" , "rt")
readFromFile.read(5) # Reading first 5 characters
print(readFromFile.readline()) # Reading first line
print(readFromFile.readline()) #Reading second line
print(readFromFile.readlines())
readFromFile.close()

# NOTE : Reading File from certain postions
readFromCertainPostion = open("/Users/snehasispanda/Desktop/DemoFolderForPython/demo.txt" , "rt") 
ourCursorPostion = readFromCertainPostion.tell()
changeCursorPostion  = readFromCertainPostion.seek(2 ,0)
print(readFromCertainPostion.read())


# NOTE : BELOW CODES TO BE UNCOMMENTED FOR TESTING PURPOSE ONLY

# # NOTE : Removing file
# if(os.path.exists("/Users/snehasispanda/Desktop/DemoFolderForPython/Demo.txt")):
#     try:
#         x = os.remove("/Users/snehasispanda/Desktop/DemoFolderForPython/Demo.txt")
#     except NameError as Name:
#         print("Error : " , Name)
# else:
#     print("File doesn't exists")

# # NOTE : Removing Folder
# if(os.path.exists("/Users/snehasispanda/Desktop/DemoFolderForPython")):
#     try:
#         x = os.rmdir("/Users/snehasispanda/Desktop/DemoFolderForPython")
#     except NameError as Name:
#         print("Error : " , Name)
# else:
#     print("Folder doesn't exists")
    





