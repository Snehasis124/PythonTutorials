#14TH PROGRAM
#Here we will try the file system in Python

#Opening File
openfile = open('/Users/snehasispanda/Desktop/Python_Programs/P04-11012019-Loops/Loops.py', 'r+')
print("We are printing normally" ,openfile.read())
#Telling the cursor positon
cursorPosition = openfile.tell()
print(cursorPosition , "\n")
#Seeking the position of the file and reading it
openfile.seek(14,0)
print(openfile.read())
#Reading Line
print(openfile.readline()) #TODO Analyze more
#Reading Lines
print(openfile.readlines()) #TODO Analyze more
#Writing Information
openfile.seek(250,0)
openfile.write("We are writing something here")
openfile.close()
#File cannot be read as the file is closed , open the file to read it again
newFile = open('/Users/snehasispanda/Desktop/Python_Programs/P04-11012019-Loops/Loops.py', 'r')
print(newFile.read())



