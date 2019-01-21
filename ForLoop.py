#10TH PROGRAM
#INTRODUCTION TO FORLOOP

new_list = ['Hello' , 'Good Morning']
word = input("Add your word ")
new_list.append(word)

for value in new_list:
    print(value)

# A DEMO PROGRAM
def menu(list, question): 
    for entry in list: print( 1 + list.index(entry), print (")") + entry )
    return input(question) - 1

   
    