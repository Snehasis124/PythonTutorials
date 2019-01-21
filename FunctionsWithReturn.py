#7TH PROGRAM
#THIS WILL HELP US IN KNOWING THE USE OF "RETURN" STATEMENT

def hello_world():
    print("Hello World without return statement")
def hello_world_return():
    print("Hello world")
    return("Hello world with return statement")

print("Calling hello_world")
hello_world()

print("Calling hello_world_with_return")
hello_world_return()
returned_value = hello_world_return()
print("Returned Value from hello_world_return() is ->" , returned_value)