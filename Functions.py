#6TH PROGRAM 
# This file will provide how we can implement functions in Python
# NOTE When a function runs , computer doesn't see the function name 
#                              instead it sees the result received from the function.
# NOTE Mark the usage of colons in the functions

#Syntax  :
# 1 Calling A Function
    # function_name(param)

# 2 Defining A Function
    # def function_name(param):

#Program : Create a calculator program which involves addition , subtraction , multiplication, division & remainder calculation

#START PROGRAM

#FUNCTION DEFINITIONS
def add(a , b):
    c = a + b
    print("Sum is " , c)
def sub (a , b):
    c = a - b
    print("Subtracted Value is " , c)
def mul(a , b):
    c = a * b
    print("Multiplied Value is " , c)
def div(a ,b):
    c = a / b 
    print("Division is " , c)
def rem(a , b):
    c = a % b
    print("Remainder is " , c)

loop_value = 1
while loop_value == 1: 
    print("Welcome to the world of Calculator ::")
    print ("We are entering the menu ::")
    print("1:Addition")
    print("2:Subtraction")
    print("3:Multiplication")
    print("4:Division")
    print("5:Remainder")
    print("6:Quit")
    actions  = int(input("Enter your choice to perform certain actions : "))
    if(actions == 1):
        value1 = float(input("Enter the value for first number "))
        value2 = float(input("Enter the value for second number "))
        add(value1 , value2)
        choice = int(input("Want to enter Calculator Again !! Press 1 "))
        if(choice == 1):
            loop_value = 1
        else:
            loop_value = 0    
    elif (actions == 2):
        value1 = float(input("Enter the value for first number "))
        value2 = float(input("Enter the value for second number "))
        sub(value1 , value2)
        choice = int(input("Want to enter Calculator Again !! Press 1 "))
        if(choice == 1):
            loop_value = 1
        else:
            loop_value = 0  
    elif (actions == 3):
        value1 = float(input("Enter the value for first number "))
        value2 = float(input("Enter the value for second number "))
        mul(value1 , value2)
        choice = int(input("Want to enter Calculator Again !! Press 1 "))
        if(choice == 1):
            loop_value = 1
        else:
            loop_value = 0  
    elif (actions ==4):
        value1 = float(input("Enter the value for first number "))
        value2 = float(input("Enter the value for second number "))
        div(value1 , value2)
        choice = int(input("Want to enter Calculator Again !! Press 1 "))
        if(choice == 1):
            loop_value = 1
        else:
            loop_value = 0  
    elif(actions == 5):
        value1 = float(input("Enter the value for first number "))
        value2 = float(input("Enter the value for second number "))
        rem(value1 , value2)
        choice = int(input("Want to enter Calculator Again !! Press 1 "))
        if(choice == 1):
            loop_value = 1
        else:
            loop_value = 0  
    elif(actions == 6):
        print("Closing Calculator")
        loop_value = 0
    else:
        print("You are trying to access something which is beyond your limit")
        
print("Thank You for using Calculator")       

  













