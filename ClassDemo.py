#12TH PROGRAM
#HERE WE WILL UNDERSTAND THE CONCEPTS OF CLASS
#SYNTAX USED : 
# class class_name: [statement1] [statement1] [statement1] [etc]

#DEFINE A CLASS
class Group:
    def __init__(self,group_name,roles):
        self.group_name = group_name
        self.roles = roles
    ageOfMember = 0
    def putPost(self,postTitle,postDesc):
        self.postTitle = postTitle
        self.postDesc = postDesc
        return postTitle + "\t " + postDesc + "by " + self.group_name
    def setLikes(self,noOfLikes):
        self.noOfLikes = noOfLikes
        return "We got " + str(noOfLikes) + " likes for our first post"

#Creating single group and single member

lucky = Group("RiderLucky" , "Admin")
myFirstPost = lucky.putPost("My First Post" ," This post relevants to my future posts !!")
print(myFirstPost)
myFirstPageLikes = lucky.setLikes(100)
print(myFirstPageLikes)


# Create some groups and members (Multiple) using dictionary:

groupDictionary  = {}

groupDictionary["Micky"] = Group("MikeLabs", "Admin")
groupDictionary["Prasanna"] = Group("MikeLabs", "Editor")
groupDictionary["Bhusan"] = Group("MikeLabs", "Moderator")

groupDictionary["Micky"].ageOfMember = 24
groupDictionary["Prasanna"].ageOfMember = 26
groupDictionary["Bhusan"].ageOfMember = 27

print(groupDictionary["Micky"].putPost("Welcome to MikeLabs", "This is our post welconing you"))
print(groupDictionary["Micky"].ageOfMember)

#INHERITANCE
class NewGroup(Group):
    def __init__(self,group_name,role_name,approvals):
         self.group_name = group_name
         self.role_name = role_name
         self.approvals = approvals
    def message(self, welcomeMessage):
        return welcomeMessage

Micky = NewGroup("MikeLabsDev" , "Admin" , "Granted")
Micky.ageOfMember = 24
print(Micky.ageOfMember)
print(Micky.message("We welcome you"))





