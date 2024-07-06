# Introduction and Rules
def Intro():
    user_name = input("What is your name?")
    greet_user = print("Hi,", user_name, "Welcome to this Mormory game !")
    print("In this Memory game there are two topics based on which the game will be played by you and me.")
    print("This game is a lot chalenging !!!")
def rule():
    print("In this Memory game we need to remember the whole list of words and then add a new word extra to it.")
    print("For example the game starts, In my turn- Apple, say apple and your turn comes, you say- orange, My turn comes again then I say from apple to orange in an order and then I add- banana. ")
    print("The games goes on exactly like the example provided as above. Remember that you have to tell from the starting in order as the game starts and goes on.!")
    print("The game stops at a point where any one player is unable to recollect/remember and say the whole list of words from the starting in order and added a new word to it.")
    print("You can tell any word at random but you should be following the rules as stated above.")
def understand_rule():
    ask_user = input ("Did you understand the rules of this game")
    if ask_user == "no" or " no":
        print(rule())
    else: 
        print()
def ask_user_topic():
    print("There are 3 topics based on which the game is made.")
    print("You have to choose any one of those 3 topics.")
def memory_game_start():
    input("")