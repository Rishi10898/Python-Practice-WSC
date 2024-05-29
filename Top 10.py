#Intoduction with greetings
#------FUNCTIONS—--------
def intro():
    name = input("What's your name?")
    print("Welcome to this quiz,", name)
    print("Do you know the 10 largesst countries in the world?, if so can you name them?")
def get_Passes():
    passes_user = input("How many chances do you want?")
    try: 
        passes_user = int(passes_user)
        if passes_user >= 0:
            return passes_user
        else:
            print("Pls type in a positive number")
    except:
        print("Invalid nummber of passes")
Largest_Countries_in_the_World = ["Russia", "Canada", "China", "United States", "Brazil", "Australia", "India", "Argentina", "Kazakhstan", "Algeria"]
score = 0
while get_Passes() > 0:
    answer = input("Name one of the top 10 biggest countries in the world").lower()
#------MAIN FUNCTIONS------ 
intro()
get_Passes()