#Intoduction with greetings
#------FUNCTIONS—--------
def intro():
    name = input("What's your name?")
    print("Welcome to this quiz,", name)
    print("Do you know the 10 largesst countries in the world?, if so can you name them?")
def create_password():
    Password_Create = input("Pls create your password here...")
def typein_password():
    Password_input = input("Pls type in your password here...")
    if Password_input == create_password:
        return
    else:
        print("Oops!.Try Again")
#------MAIN FUNCTIONS------ 
intro()
create_password()
typein_password()
