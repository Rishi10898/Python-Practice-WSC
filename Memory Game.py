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
        print(memory_game())
def ask_user_topic():
    print("There are 3 topics based on which the game is made.")
    print("You have to choose any one of those 3 topics.")
def memory_game():
    User_topic = print ("There are 3 topics they are :- World countries and its capitals(combined), Indian states and its capitals + Districts of Tamil nadu(Combined), States of USA and its capitals(Combined)")
    print("World/India/USA :- These are the topics you have to choose")
    User_topic = input("Which topic based on which you want to play now?")
    if User_topic == "World" or " World" 
        elif "India" or " India":
        elif "USA" or " USA":
        print("Ok, We will start the game now!")
    else:
def start_memory_game():
    
# Indian States and its Capitals
Starts_with_A = ["Andhra Pradesh","Amaravati","Arunachal Pradesh","Assam","Aizawl","Agartala"]
Starts_with_B = ["Bangalore","Bhopal","Bihar","Bhubaneshwar"]
Starts_with_C = ["Chandigarh","Chhattisgarh","Chennai","Chandigarh"]
Starts_with_D = ["Dispur","Dehradun"]
Starts_with_G = ["Gujarat","Gandhinagar","Goa","Gangtok"]
Starts_with_H = ["Haryana","Himachal Pradesh","Hyderabad"]
Starts_with_I = ["Itanagar","Imphal"]
Starts_with_J = ["Jharkhand","Jaipur"]
Starts_with_K = ["Karnataka","Kerala","Kohima","Kolkata"]
Starts_with_L = "Lucknow"
Starts_with_M = ["Madhya Pradesh","Maharashtra","Mumbai","Manipur","Meghalaya","Mizoram"]
Starts_with_N = "Nagaland"
Starts_with_O = "Odisha"
Starts_with_P = ["Patna","Punjab","Panaji"]
Starts_with_R = ["Rajasthan","Ranchi","Raipur"]
Starts_with_S = ["Shimla","Shillong","Sikkim"]
Starts_with_T = ["Thiruvananthapuram","Tamil Nadu","Telangana","Tripura"]
Starts_with_U = ["Uttarakhand","Uttar Pradesh"]
Starts_with_W = "West Bengal"
# Districts of Tamil Nadu
Starts_with_A = "Ariyalur"
Starts_with_C = ["Chengalpattu","Chennai","Coimbatore","Cuddalore"]
Starts_with_D = ["Dharmapuri","Dindigul"]
Starts_with_E = "Erode"
Starts_with_K = ["Kallakurichi","Kancheepuram","Karur","Krishnagiri","Kanniyakumari"]
Starts_with_M = ["Madurai","Mayiladuthurai"]
Starts_with_N = ["Nagapattinam","Namakkal"]
Starts_with_P = ["Perambalur","Pudukottai"]
Starts_with_R = ["Ramanathapuram","Ranipet"]
Starts_with_S = ["Salem","Sivagangai"]
Starts_with_T = ["Tenkasi","Thanjavur","Theni","Thiruvallur","Thiruvarur","Thoothukudi","Trichirappalli","Thirunelveli","Tirupathur","Tiruppur","Tiruvannamalai","The Nilgiris"]
Starts_with_V = ["Vellore","Viluppuram","Virudhunagar"]
# USA states and its capitals
Starts_with_A = ["Alabama","Alaska", "Arizona", "Arkansas", "Atlanta", "Augusta","Annapolis", "Austin", "Albany" ]
Starts_with_B = ["Boise", "Baton Rouge","Boston","Bismarck"]
Starts_with_C = ["California","Colorado","Connecticut ","Carson City","Concord","Columbia", "Charleston", "Cheyenne", "Columbus"]
Starts_with_D = ["Delaware ", "Denver", "Dover", "Des Moines"]
Starts_with_F = ["Florida ", "Frankfort"]
Starts_with_G = "Georgia"
Starts_with_H = ["Hawaii ", "Hartford", "Honolulu", "Helena", "Harrisburg"]
Starts_with_I = ["Idaho","Illinois","Indiana" ,"Iowa", "Indianapolis"]
Starts_with_J = ["Juneau", "Jackson","Jefferson City" ]
Starts_with_K = ["Kansas", "Kentucky"] 
Starts_with_L = ["Louisiana", "Little Rock","Lansing","Lincoln"]
Starts_with_M = ["Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana", "Montpelier", "Madison", "Montgomery"] 
Starts_with_N = ["Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota", "Nashville"]
Starts_with_O = ["Ohio","Oklahoma","Oregon", "Oklahoma City", "Olympia"]
Starts_with_P = ["Pennsylvania", "Phoenix","Providence","Pierre"]
Starts_with_R = ["Rhode Island", "Raleigh", "Richmond"]
Starts_with_S = ["South Carolina","South Dakota","Sacramento","Springfield","Saint Paul", "Santa Fe","Salem","Salt Lake City"]
Starts_wiht_T = ["Tennessee","Texas","Tallahassee","Topeka","Trenton"] 
Starts_with_U = "Utah" 
Starts_with_V = ["Vermont","Virginia"]
Starts_with_W = ["Washington","West Virginia","Wisconsin","Wyoming"]# Introduction and Rules
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
        print(memory_game())
def ask_user_topic():
    print("There are 3 topics based on which the game is made.")
    print("You have to choose any one of those 3 topics.")
def memory_game():
    User_topic = print ("There are 3 topics they are :- World countries and its capitals(combined), Indian states and its capitals + Districts of Tamil nadu(Combined), States of USA and its capitals(Combined)")
    print("World/India/USA :- These are the topics you have to choose")
    User_topic = input("Which topic based on which you want to play now?")
    if User_topic == "World" or " World" 
        elif "India" or " India":
        elif "USA" or " USA":
        print("Ok, We will start the game now!")
    else:
def start_memory_game():
    
# Indian States and its Capitals
Starts_with_A = ["Andhra Pradesh","Amaravati","Arunachal Pradesh","Assam","Aizawl","Agartala"]
Starts_with_B = ["Bangalore","Bhopal","Bihar","Bhubaneshwar"]
Starts_with_C = ["Chandigarh","Chhattisgarh","Chennai","Chandigarh"]
Starts_with_D = ["Dispur","Dehradun"]
Starts_with_G = ["Gujarat","Gandhinagar","Goa","Gangtok"]
Starts_with_H = ["Haryana","Himachal Pradesh","Hyderabad"]
Starts_with_I = ["Itanagar","Imphal"]
Starts_with_J = ["Jharkhand","Jaipur"]
Starts_with_K = ["Karnataka","Kerala","Kohima","Kolkata"]
Starts_with_L = "Lucknow"
Starts_with_M = ["Madhya Pradesh","Maharashtra","Mumbai","Manipur","Meghalaya","Mizoram"]
Starts_with_N = "Nagaland"
Starts_with_O = "Odisha"
Starts_with_P = ["Patna","Punjab","Panaji"]
Starts_with_R = ["Rajasthan","Ranchi","Raipur"]
Starts_with_S = ["Shimla","Shillong","Sikkim"]
Starts_with_T = ["Thiruvananthapuram","Tamil Nadu","Telangana","Tripura"]
Starts_with_U = ["Uttarakhand","Uttar Pradesh"]
Starts_with_W = "West Bengal"
# Districts of Tamil Nadu
Starts_with_A = "Ariyalur"
Starts_with_C = ["Chengalpattu","Chennai","Coimbatore","Cuddalore"]
Starts_with_D = ["Dharmapuri","Dindigul"]
Starts_with_E = "Erode"
Starts_with_K = ["Kallakurichi","Kancheepuram","Karur","Krishnagiri","Kanniyakumari"]
Starts_with_M = ["Madurai","Mayiladuthurai"]
Starts_with_N = ["Nagapattinam","Namakkal"]
Starts_with_P = ["Perambalur","Pudukottai"]
Starts_with_R = ["Ramanathapuram","Ranipet"]
Starts_with_S = ["Salem","Sivagangai"]
Starts_with_T = ["Tenkasi","Thanjavur","Theni","Thiruvallur","Thiruvarur","Thoothukudi","Trichirappalli","Thirunelveli","Tirupathur","Tiruppur","Tiruvannamalai","The Nilgiris"]
Starts_with_V = ["Vellore","Viluppuram","Virudhunagar"]
# USA states and its capitals
Starts_with_A = ["Alabama","Alaska", "Arizona", "Arkansas", "Atlanta", "Augusta","Annapolis", "Austin", "Albany" ]
Starts_with_B = ["Boise", "Baton Rouge","Boston","Bismarck"]
Starts_with_C = ["California","Colorado","Connecticut ","Carson City","Concord","Columbia", "Charleston", "Cheyenne", "Columbus"]
Starts_with_D = ["Delaware ", "Denver", "Dover", "Des Moines"]
Starts_with_F = ["Florida ", "Frankfort"]
Starts_with_G = "Georgia"
Starts_with_H = ["Hawaii ", "Hartford", "Honolulu", "Helena", "Harrisburg"]
Starts_with_I = ["Idaho","Illinois","Indiana" ,"Iowa", "Indianapolis"]
Starts_with_J = ["Juneau", "Jackson","Jefferson City" ]
Starts_with_K = ["Kansas", "Kentucky"] 
Starts_with_L = ["Louisiana", "Little Rock","Lansing","Lincoln"]
Starts_with_M = ["Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana", "Montpelier", "Madison", "Montgomery"] 
Starts_with_N = ["Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota", "Nashville"]
Starts_with_O = ["Ohio","Oklahoma","Oregon", "Oklahoma City", "Olympia"]
Starts_with_P = ["Pennsylvania", "Phoenix","Providence","Pierre"]
Starts_with_R = ["Rhode Island", "Raleigh", "Richmond"]
Starts_with_S = ["South Carolina","South Dakota","Sacramento","Springfield","Saint Paul", "Santa Fe","Salem","Salt Lake City"]
Starts_wiht_T = ["Tennessee","Texas","Tallahassee","Topeka","Trenton"] 
Starts_with_U = "Utah" 
Starts_with_V = ["Vermont","Virginia"]
Starts_with_W = ["Washington","West Virginia","Wisconsin","Wyoming"]# Introduction and Rules
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
        print(memory_game())
def ask_user_topic():
    print("There are 3 topics based on which the game is made.")
    print("You have to choose any one of those 3 topics.")
def memory_game():
    User_topic = print ("There are 3 topics they are :- World countries and its capitals(combined), Indian states and its capitals + Districts of Tamil nadu(Combined), States of USA and its capitals(Combined)")
    print("World/India/USA :- These are the topics you have to choose")
    User_topic = input("Which topic based on which you want to play now?")
    if User_topic == "World" or " World" 
        elif "India" or " India":
        elif "USA" or " USA":
        print("Ok, We will start the game now!")
    else:
def start_memory_game():
    
# Indian States and its Capitals
Starts_with_A = ["Andhra Pradesh","Amaravati","Arunachal Pradesh","Assam","Aizawl","Agartala"]
Starts_with_B = ["Bangalore","Bhopal","Bihar","Bhubaneshwar"]
Starts_with_C = ["Chandigarh","Chhattisgarh","Chennai","Chandigarh"]
Starts_with_D = ["Dispur","Dehradun"]
Starts_with_G = ["Gujarat","Gandhinagar","Goa","Gangtok"]
Starts_with_H = ["Haryana","Himachal Pradesh","Hyderabad"]
Starts_with_I = ["Itanagar","Imphal"]
Starts_with_J = ["Jharkhand","Jaipur"]
Starts_with_K = ["Karnataka","Kerala","Kohima","Kolkata"]
Starts_with_L = "Lucknow"
Starts_with_M = ["Madhya Pradesh","Maharashtra","Mumbai","Manipur","Meghalaya","Mizoram"]
Starts_with_N = "Nagaland"
Starts_with_O = "Odisha"
Starts_with_P = ["Patna","Punjab","Panaji"]
Starts_with_R = ["Rajasthan","Ranchi","Raipur"]
Starts_with_S = ["Shimla","Shillong","Sikkim"]
Starts_with_T = ["Thiruvananthapuram","Tamil Nadu","Telangana","Tripura"]
Starts_with_U = ["Uttarakhand","Uttar Pradesh"]
Starts_with_W = "West Bengal"
# Districts of Tamil Nadu
Starts_with_A = "Ariyalur"
Starts_with_C = ["Chengalpattu","Chennai","Coimbatore","Cuddalore"]
Starts_with_D = ["Dharmapuri","Dindigul"]
Starts_with_E = "Erode"
Starts_with_K = ["Kallakurichi","Kancheepuram","Karur","Krishnagiri","Kanniyakumari"]
Starts_with_M = ["Madurai","Mayiladuthurai"]
Starts_with_N = ["Nagapattinam","Namakkal"]
Starts_with_P = ["Perambalur","Pudukottai"]
Starts_with_R = ["Ramanathapuram","Ranipet"]
Starts_with_S = ["Salem","Sivagangai"]
Starts_with_T = ["Tenkasi","Thanjavur","Theni","Thiruvallur","Thiruvarur","Thoothukudi","Trichirappalli","Thirunelveli","Tirupathur","Tiruppur","Tiruvannamalai","The Nilgiris"]
Starts_with_V = ["Vellore","Viluppuram","Virudhunagar"]
# USA states and its capitals
Starts_with_A = ["Alabama","Alaska", "Arizona", "Arkansas", "Atlanta", "Augusta","Annapolis", "Austin", "Albany" ]
Starts_with_B = ["Boise", "Baton Rouge","Boston","Bismarck"]
Starts_with_C = ["California","Colorado","Connecticut ","Carson City","Concord","Columbia", "Charleston", "Cheyenne", "Columbus"]
Starts_with_D = ["Delaware ", "Denver", "Dover", "Des Moines"]
Starts_with_F = ["Florida ", "Frankfort"]
Starts_with_G = "Georgia"
Starts_with_H = ["Hawaii ", "Hartford", "Honolulu", "Helena", "Harrisburg"]
Starts_with_I = ["Idaho","Illinois","Indiana" ,"Iowa", "Indianapolis"]
Starts_with_J = ["Juneau", "Jackson","Jefferson City" ]
Starts_with_K = ["Kansas", "Kentucky"] 
Starts_with_L = ["Louisiana", "Little Rock","Lansing","Lincoln"]
Starts_with_M = ["Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana", "Montpelier", "Madison", "Montgomery"] 
Starts_with_N = ["Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota", "Nashville"]
Starts_with_O = ["Ohio","Oklahoma","Oregon", "Oklahoma City", "Olympia"]
Starts_with_P = ["Pennsylvania", "Phoenix","Providence","Pierre"]
Starts_with_R = ["Rhode Island", "Raleigh", "Richmond"]
Starts_with_S = ["South Carolina","South Dakota","Sacramento","Springfield","Saint Paul", "Santa Fe","Salem","Salt Lake City"]
Starts_wiht_T = ["Tennessee","Texas","Tallahassee","Topeka","Trenton"] 
Starts_with_U = "Utah" 
Starts_with_V = ["Vermont","Virginia"]
Starts_with_W = ["Washington","West Virginia","Wisconsin","Wyoming"]# Introduction and Rules
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
        print(memory_game())
def ask_user_topic():
    print("There are 3 topics based on which the game is made.")
    print("You have to choose any one of those 3 topics.")
def memory_game():
    User_topic = print ("There are 3 topics they are :- World countries and its capitals(combined), Indian states and its capitals + Districts of Tamil nadu(Combined), States of USA and its capitals(Combined)")
    print("World/India/USA :- These are the topics you have to choose")
    User_topic = input("Which topic based on which you want to play now?")
    if User_topic == "World" or " World" 
        elif "India" or " India":
        elif "USA" or " USA":
        print("Ok, We will start the game now!")
    else:
def start_memory_game():
    
# Indian States and its Capitals
Starts_with_A = ["Andhra Pradesh","Amaravati","Arunachal Pradesh","Assam","Aizawl","Agartala"]
Starts_with_B = ["Bangalore","Bhopal","Bihar","Bhubaneshwar"]
Starts_with_C = ["Chandigarh","Chhattisgarh","Chennai","Chandigarh"]
Starts_with_D = ["Dispur","Dehradun"]
Starts_with_G = ["Gujarat","Gandhinagar","Goa","Gangtok"]
Starts_with_H = ["Haryana","Himachal Pradesh","Hyderabad"]
Starts_with_I = ["Itanagar","Imphal"]
Starts_with_J = ["Jharkhand","Jaipur"]
Starts_with_K = ["Karnataka","Kerala","Kohima","Kolkata"]
Starts_with_L = "Lucknow"
Starts_with_M = ["Madhya Pradesh","Maharashtra","Mumbai","Manipur","Meghalaya","Mizoram"]
Starts_with_N = "Nagaland"
Starts_with_O = "Odisha"
Starts_with_P = ["Patna","Punjab","Panaji"]
Starts_with_R = ["Rajasthan","Ranchi","Raipur"]
Starts_with_S = ["Shimla","Shillong","Sikkim"]
Starts_with_T = ["Thiruvananthapuram","Tamil Nadu","Telangana","Tripura"]
Starts_with_U = ["Uttarakhand","Uttar Pradesh"]
Starts_with_W = "West Bengal"
# Districts of Tamil Nadu
Starts_with_A = "Ariyalur"
Starts_with_C = ["Chengalpattu","Chennai","Coimbatore","Cuddalore"]
Starts_with_D = ["Dharmapuri","Dindigul"]
Starts_with_E = "Erode"
Starts_with_K = ["Kallakurichi","Kancheepuram","Karur","Krishnagiri","Kanniyakumari"]
Starts_with_M = ["Madurai","Mayiladuthurai"]
Starts_with_N = ["Nagapattinam","Namakkal"]
Starts_with_P = ["Perambalur","Pudukottai"]
Starts_with_R = ["Ramanathapuram","Ranipet"]
Starts_with_S = ["Salem","Sivagangai"]
Starts_with_T = ["Tenkasi","Thanjavur","Theni","Thiruvallur","Thiruvarur","Thoothukudi","Trichirappalli","Thirunelveli","Tirupathur","Tiruppur","Tiruvannamalai","The Nilgiris"]
Starts_with_V = ["Vellore","Viluppuram","Virudhunagar"]
# USA states and its capitals
Starts_with_A = ["Alabama","Alaska", "Arizona", "Arkansas", "Atlanta", "Augusta","Annapolis", "Austin", "Albany" ]
Starts_with_B = ["Boise", "Baton Rouge","Boston","Bismarck"]
Starts_with_C = ["California","Colorado","Connecticut ","Carson City","Concord","Columbia", "Charleston", "Cheyenne", "Columbus"]
Starts_with_D = ["Delaware ", "Denver", "Dover", "Des Moines"]
Starts_with_F = ["Florida ", "Frankfort"]
Starts_with_G = "Georgia"
Starts_with_H = ["Hawaii ", "Hartford", "Honolulu", "Helena", "Harrisburg"]
Starts_with_I = ["Idaho","Illinois","Indiana" ,"Iowa", "Indianapolis"]
Starts_with_J = ["Juneau", "Jackson","Jefferson City" ]
Starts_with_K = ["Kansas", "Kentucky"] 
Starts_with_L = ["Louisiana", "Little Rock","Lansing","Lincoln"]
Starts_with_M = ["Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana", "Montpelier", "Madison", "Montgomery"] 
Starts_with_N = ["Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota", "Nashville"]
Starts_with_O = ["Ohio","Oklahoma","Oregon", "Oklahoma City", "Olympia"]
Starts_with_P = ["Pennsylvania", "Phoenix","Providence","Pierre"]
Starts_with_R = ["Rhode Island", "Raleigh", "Richmond"]
Starts_with_S = ["South Carolina","South Dakota","Sacramento","Springfield","Saint Paul", "Santa Fe","Salem","Salt Lake City"]
Starts_wiht_T = ["Tennessee","Texas","Tallahassee","Topeka","Trenton"] 
Starts_with_U = "Utah" 
Starts_with_V = ["Vermont","Virginia"]
Starts_with_W = ["Washington","West Virginia","Wisconsin","Wyoming"]# Introduction and Rules
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
        print(memory_game())
def ask_user_topic():
    print("There are 3 topics based on which the game is made.")
    print("You have to choose any one of those 3 topics.")
def memory_game():
    User_topic = print ("There are 3 topics they are :- World countries and its capitals(combined), Indian states and its capitals + Districts of Tamil nadu(Combined), States of USA and its capitals(Combined)")
    print("World/India/USA :- These are the topics you have to choose")
    User_topic = input("Which topic based on which you want to play now?")
    if User_topic == "World" or " World" 
        elif "India" or " India":
        elif "USA" or " USA":
        print("Ok, We will start the game now!")
    else:
def start_memory_game():
    
# Indian States and its Capitals
Starts_with_A = ["Andhra Pradesh","Amaravati","Arunachal Pradesh","Assam","Aizawl","Agartala"]
Starts_with_B = ["Bangalore","Bhopal","Bihar","Bhubaneshwar"]
Starts_with_C = ["Chandigarh","Chhattisgarh","Chennai","Chandigarh"]
Starts_with_D = ["Dispur","Dehradun"]
Starts_with_G = ["Gujarat","Gandhinagar","Goa","Gangtok"]
Starts_with_H = ["Haryana","Himachal Pradesh","Hyderabad"]
Starts_with_I = ["Itanagar","Imphal"]
Starts_with_J = ["Jharkhand","Jaipur"]
Starts_with_K = ["Karnataka","Kerala","Kohima","Kolkata"]
Starts_with_L = "Lucknow"
Starts_with_M = ["Madhya Pradesh","Maharashtra","Mumbai","Manipur","Meghalaya","Mizoram"]
Starts_with_N = "Nagaland"
Starts_with_O = "Odisha"
Starts_with_P = ["Patna","Punjab","Panaji"]
Starts_with_R = ["Rajasthan","Ranchi","Raipur"]
Starts_with_S = ["Shimla","Shillong","Sikkim"]
Starts_with_T = ["Thiruvananthapuram","Tamil Nadu","Telangana","Tripura"]
Starts_with_U = ["Uttarakhand","Uttar Pradesh"]
Starts_with_W = "West Bengal"
# Districts of Tamil Nadu
Starts_with_A = "Ariyalur"
Starts_with_C = ["Chengalpattu","Chennai","Coimbatore","Cuddalore"]
Starts_with_D = ["Dharmapuri","Dindigul"]
Starts_with_E = "Erode"
Starts_with_K = ["Kallakurichi","Kancheepuram","Karur","Krishnagiri","Kanniyakumari"]
Starts_with_M = ["Madurai","Mayiladuthurai"]
Starts_with_N = ["Nagapattinam","Namakkal"]
Starts_with_P = ["Perambalur","Pudukottai"]
Starts_with_R = ["Ramanathapuram","Ranipet"]
Starts_with_S = ["Salem","Sivagangai"]
Starts_with_T = ["Tenkasi","Thanjavur","Theni","Thiruvallur","Thiruvarur","Thoothukudi","Trichirappalli","Thirunelveli","Tirupathur","Tiruppur","Tiruvannamalai","The Nilgiris"]
Starts_with_V = ["Vellore","Viluppuram","Virudhunagar"]
# USA states and its capitals
Starts_with_A = ["Alabama","Alaska", "Arizona", "Arkansas", "Atlanta", "Augusta","Annapolis", "Austin", "Albany" ]
Starts_with_B = ["Boise", "Baton Rouge","Boston","Bismarck"]
Starts_with_C = ["California","Colorado","Connecticut ","Carson City","Concord","Columbia", "Charleston", "Cheyenne", "Columbus"]
Starts_with_D = ["Delaware ", "Denver", "Dover", "Des Moines"]
Starts_with_F = ["Florida ", "Frankfort"]
Starts_with_G = "Georgia"
Starts_with_H = ["Hawaii ", "Hartford", "Honolulu", "Helena", "Harrisburg"]
Starts_with_I = ["Idaho","Illinois","Indiana" ,"Iowa", "Indianapolis"]
Starts_with_J = ["Juneau", "Jackson","Jefferson City" ]
Starts_with_K = ["Kansas", "Kentucky"] 
Starts_with_L = ["Louisiana", "Little Rock","Lansing","Lincoln"]
Starts_with_M = ["Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana", "Montpelier", "Madison", "Montgomery"] 
Starts_with_N = ["Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota", "Nashville"]
Starts_with_O = ["Ohio","Oklahoma","Oregon", "Oklahoma City", "Olympia"]
Starts_with_P = ["Pennsylvania", "Phoenix","Providence","Pierre"]
Starts_with_R = ["Rhode Island", "Raleigh", "Richmond"]
Starts_with_S = ["South Carolina","South Dakota","Sacramento","Springfield","Saint Paul", "Santa Fe","Salem","Salt Lake City"]
Starts_wiht_T = ["Tennessee","Texas","Tallahassee","Topeka","Trenton"] 
Starts_with_U = "Utah" 
Starts_with_V = ["Vermont","Virginia"]
Starts_with_W = ["Washington","West Virginia","Wisconsin","Wyoming"]# Introduction and Rules
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
        print(memory_game())
def ask_user_topic():
    print("There are 3 topics based on which the game is made.")
    print("You have to choose any one of those 3 topics.")
def memory_game():
    User_topic = print ("There are 3 topics they are :- World countries and its capitals(combined), Indian states and its capitals + Districts of Tamil nadu(Combined), States of USA and its capitals(Combined)")
    print("World/India/USA :- These are the topics you have to choose")
    User_topic = input("Which topic based on which you want to play now?")
    if User_topic == "World" or " World" 
        elif "India" or " India":
        elif "USA" or " USA":
        print("Ok, We will start the game now!")
    else:
def start_memory_game():
    
# Indian States and its Capitals
Starts_with_A = ["Andhra Pradesh","Amaravati","Arunachal Pradesh","Assam","Aizawl","Agartala"]
Starts_with_B = ["Bangalore","Bhopal","Bihar","Bhubaneshwar"]
Starts_with_C = ["Chandigarh","Chhattisgarh","Chennai","Chandigarh"]
Starts_with_D = ["Dispur","Dehradun"]
Starts_with_G = ["Gujarat","Gandhinagar","Goa","Gangtok"]
Starts_with_H = ["Haryana","Himachal Pradesh","Hyderabad"]
Starts_with_I = ["Itanagar","Imphal"]
Starts_with_J = ["Jharkhand","Jaipur"]
Starts_with_K = ["Karnataka","Kerala","Kohima","Kolkata"]
Starts_with_L = "Lucknow"
Starts_with_M = ["Madhya Pradesh","Maharashtra","Mumbai","Manipur","Meghalaya","Mizoram"]
Starts_with_N = "Nagaland"
Starts_with_O = "Odisha"
Starts_with_P = ["Patna","Punjab","Panaji"]
Starts_with_R = ["Rajasthan","Ranchi","Raipur"]
Starts_with_S = ["Shimla","Shillong","Sikkim"]
Starts_with_T = ["Thiruvananthapuram","Tamil Nadu","Telangana","Tripura"]
Starts_with_U = ["Uttarakhand","Uttar Pradesh"]
Starts_with_W = "West Bengal"
# Districts of Tamil Nadu
Starts_with_A = "Ariyalur"
Starts_with_C = ["Chengalpattu","Chennai","Coimbatore","Cuddalore"]
Starts_with_D = ["Dharmapuri","Dindigul"]
Starts_with_E = "Erode"
Starts_with_K = ["Kallakurichi","Kancheepuram","Karur","Krishnagiri","Kanniyakumari"]
Starts_with_M = ["Madurai","Mayiladuthurai"]
Starts_with_N = ["Nagapattinam","Namakkal"]
Starts_with_P = ["Perambalur","Pudukottai"]
Starts_with_R = ["Ramanathapuram","Ranipet"]
Starts_with_S = ["Salem","Sivagangai"]
Starts_with_T = ["Tenkasi","Thanjavur","Theni","Thiruvallur","Thiruvarur","Thoothukudi","Trichirappalli","Thirunelveli","Tirupathur","Tiruppur","Tiruvannamalai","The Nilgiris"]
Starts_with_V = ["Vellore","Viluppuram","Virudhunagar"]
# USA states and its capitals
Starts_with_A = ["Alabama","Alaska", "Arizona", "Arkansas", "Atlanta", "Augusta","Annapolis", "Austin", "Albany" ]
Starts_with_B = ["Boise", "Baton Rouge","Boston","Bismarck"]
Starts_with_C = ["California","Colorado","Connecticut ","Carson City","Concord","Columbia", "Charleston", "Cheyenne", "Columbus"]
Starts_with_D = ["Delaware ", "Denver", "Dover", "Des Moines"]
Starts_with_F = ["Florida ", "Frankfort"]
Starts_with_G = "Georgia"
Starts_with_H = ["Hawaii ", "Hartford", "Honolulu", "Helena", "Harrisburg"]
Starts_with_I = ["Idaho","Illinois","Indiana" ,"Iowa", "Indianapolis"]
Starts_with_J = ["Juneau", "Jackson","Jefferson City" ]
Starts_with_K = ["Kansas", "Kentucky"] 
Starts_with_L = ["Louisiana", "Little Rock","Lansing","Lincoln"]
Starts_with_M = ["Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana", "Montpelier", "Madison", "Montgomery"] 
Starts_with_N = ["Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota", "Nashville"]
Starts_with_O = ["Ohio","Oklahoma","Oregon", "Oklahoma City", "Olympia"]
Starts_with_P = ["Pennsylvania", "Phoenix","Providence","Pierre"]
Starts_with_R = ["Rhode Island", "Raleigh", "Richmond"]
Starts_with_S = ["South Carolina","South Dakota","Sacramento","Springfield","Saint Paul", "Santa Fe","Salem","Salt Lake City"]
Starts_wiht_T = ["Tennessee","Texas","Tallahassee","Topeka","Trenton"] 
Starts_with_U = "Utah" 
Starts_with_V = ["Vermont","Virginia"]
Starts_with_W = ["Washington","West Virginia","Wisconsin","Wyoming"]# Introduction and Rules
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
        print(memory_game())
def ask_user_topic():
    print("There are 3 topics based on which the game is made.")
    print("You have to choose any one of those 3 topics.")
def memory_game():
    User_topic = print ("There are 3 topics they are :- World countries and its capitals(combined), Indian states and its capitals + Districts of Tamil nadu(Combined), States of USA and its capitals(Combined)")
    print("World/India/USA :- These are the topics you have to choose")
    User_topic = input("Which topic based on which you want to play now?")
    if User_topic == "World" or " World" 
        elif "India" or " India":
        elif "USA" or " USA":
        print("Ok, We will start the game now!")
    else:
def start_memory_game():
    
# Indian States and its Capitals
Starts_with_A = ["Andhra Pradesh","Amaravati","Arunachal Pradesh","Assam","Aizawl","Agartala"]
Starts_with_B = ["Bangalore","Bhopal","Bihar","Bhubaneshwar"]
Starts_with_C = ["Chandigarh","Chhattisgarh","Chennai","Chandigarh"]
Starts_with_D = ["Dispur","Dehradun"]
Starts_with_G = ["Gujarat","Gandhinagar","Goa","Gangtok"]
Starts_with_H = ["Haryana","Himachal Pradesh","Hyderabad"]
Starts_with_I = ["Itanagar","Imphal"]
Starts_with_J = ["Jharkhand","Jaipur"]
Starts_with_K = ["Karnataka","Kerala","Kohima","Kolkata"]
Starts_with_L = "Lucknow"
Starts_with_M = ["Madhya Pradesh","Maharashtra","Mumbai","Manipur","Meghalaya","Mizoram"]
Starts_with_N = "Nagaland"
Starts_with_O = "Odisha"
Starts_with_P = ["Patna","Punjab","Panaji"]
Starts_with_R = ["Rajasthan","Ranchi","Raipur"]
Starts_with_S = ["Shimla","Shillong","Sikkim"]
Starts_with_T = ["Thiruvananthapuram","Tamil Nadu","Telangana","Tripura"]
Starts_with_U = ["Uttarakhand","Uttar Pradesh"]
Starts_with_W = "West Bengal"
# Districts of Tamil Nadu
Starts_with_A = "Ariyalur"
Starts_with_C = ["Chengalpattu","Chennai","Coimbatore","Cuddalore"]
Starts_with_D = ["Dharmapuri","Dindigul"]
Starts_with_E = "Erode"
Starts_with_K = ["Kallakurichi","Kancheepuram","Karur","Krishnagiri","Kanniyakumari"]
Starts_with_M = ["Madurai","Mayiladuthurai"]
Starts_with_N = ["Nagapattinam","Namakkal"]
Starts_with_P = ["Perambalur","Pudukottai"]
Starts_with_R = ["Ramanathapuram","Ranipet"]
Starts_with_S = ["Salem","Sivagangai"]
Starts_with_T = ["Tenkasi","Thanjavur","Theni","Thiruvallur","Thiruvarur","Thoothukudi","Trichirappalli","Thirunelveli","Tirupathur","Tiruppur","Tiruvannamalai","The Nilgiris"]
Starts_with_V = ["Vellore","Viluppuram","Virudhunagar"]
# USA states and its capitals
Starts_with_A = ["Alabama","Alaska", "Arizona", "Arkansas", "Atlanta", "Augusta","Annapolis", "Austin", "Albany" ]
Starts_with_B = ["Boise", "Baton Rouge","Boston","Bismarck"]
Starts_with_C = ["California","Colorado","Connecticut ","Carson City","Concord","Columbia", "Charleston", "Cheyenne", "Columbus"]
Starts_with_D = ["Delaware ", "Denver", "Dover", "Des Moines"]
Starts_with_F = ["Florida ", "Frankfort"]
Starts_with_G = "Georgia"
Starts_with_H = ["Hawaii ", "Hartford", "Honolulu", "Helena", "Harrisburg"]
Starts_with_I = ["Idaho","Illinois","Indiana" ,"Iowa", "Indianapolis"]
Starts_with_J = ["Juneau", "Jackson","Jefferson City" ]
Starts_with_K = ["Kansas", "Kentucky"] 
Starts_with_L = ["Louisiana", "Little Rock","Lansing","Lincoln"]
Starts_with_M = ["Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana", "Montpelier", "Madison", "Montgomery"] 
Starts_with_N = ["Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota", "Nashville"]
Starts_with_O = ["Ohio","Oklahoma","Oregon", "Oklahoma City", "Olympia"]
Starts_with_P = ["Pennsylvania", "Phoenix","Providence","Pierre"]
Starts_with_R = ["Rhode Island", "Raleigh", "Richmond"]
Starts_with_S = ["South Carolina","South Dakota","Sacramento","Springfield","Saint Paul", "Santa Fe","Salem","Salt Lake City"]
Starts_wiht_T = ["Tennessee","Texas","Tallahassee","Topeka","Trenton"] 
Starts_with_U = "Utah" 
Starts_with_V = ["Vermont","Virginia"]
Starts_with_W = ["Washington","West Virginia","Wisconsin","Wyoming"]# Introduction and Rules
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
        print(memory_game())
def ask_user_topic():
    print("There are 3 topics based on which the game is made.")
    print("You have to choose any one of those 3 topics.")
def memory_game():
    User_topic = print ("There are 3 topics they are :- World countries and its capitals(combined), Indian states and its capitals + Districts of Tamil nadu(Combined), States of USA and its capitals(Combined)")
    print("World/India/USA :- These are the topics you have to choose")
    User_topic = input("Which topic based on which you want to play now?")
    if User_topic == "World" or " World" 
        elif "India" or " India":
        elif "USA" or " USA":
        print("Ok, We will start the game now!")
    else:
def start_memory_game():
    
# Indian States and its Capitals
Starts_with_A = ["Andhra Pradesh","Amaravati","Arunachal Pradesh","Assam","Aizawl","Agartala"]
Starts_with_B = ["Bangalore","Bhopal","Bihar","Bhubaneshwar"]
Starts_with_C = ["Chandigarh","Chhattisgarh","Chennai","Chandigarh"]
Starts_with_D = ["Dispur","Dehradun"]
Starts_with_G = ["Gujarat","Gandhinagar","Goa","Gangtok"]
Starts_with_H = ["Haryana","Himachal Pradesh","Hyderabad"]
Starts_with_I = ["Itanagar","Imphal"]
Starts_with_J = ["Jharkhand","Jaipur"]
Starts_with_K = ["Karnataka","Kerala","Kohima","Kolkata"]
Starts_with_L = "Lucknow"
Starts_with_M = ["Madhya Pradesh","Maharashtra","Mumbai","Manipur","Meghalaya","Mizoram"]
Starts_with_N = "Nagaland"
Starts_with_O = "Odisha"
Starts_with_P = ["Patna","Punjab","Panaji"]
Starts_with_R = ["Rajasthan","Ranchi","Raipur"]
Starts_with_S = ["Shimla","Shillong","Sikkim"]
Starts_with_T = ["Thiruvananthapuram","Tamil Nadu","Telangana","Tripura"]
Starts_with_U = ["Uttarakhand","Uttar Pradesh"]
Starts_with_W = "West Bengal"
# Districts of Tamil Nadu
Starts_with_A = "Ariyalur"
Starts_with_C = ["Chengalpattu","Chennai","Coimbatore","Cuddalore"]
Starts_with_D = ["Dharmapuri","Dindigul"]
Starts_with_E = "Erode"
Starts_with_K = ["Kallakurichi","Kancheepuram","Karur","Krishnagiri","Kanniyakumari"]
Starts_with_M = ["Madurai","Mayiladuthurai"]
Starts_with_N = ["Nagapattinam","Namakkal"]
Starts_with_P = ["Perambalur","Pudukottai"]
Starts_with_R = ["Ramanathapuram","Ranipet"]
Starts_with_S = ["Salem","Sivagangai"]
Starts_with_T = ["Tenkasi","Thanjavur","Theni","Thiruvallur","Thiruvarur","Thoothukudi","Trichirappalli","Thirunelveli","Tirupathur","Tiruppur","Tiruvannamalai","The Nilgiris"]
Starts_with_V = ["Vellore","Viluppuram","Virudhunagar"]
# USA states and its capitals
Starts_with_A = ["Alabama","Alaska", "Arizona", "Arkansas", "Atlanta", "Augusta","Annapolis", "Austin", "Albany" ]
Starts_with_B = ["Boise", "Baton Rouge","Boston","Bismarck"]
Starts_with_C = ["California","Colorado","Connecticut ","Carson City","Concord","Columbia", "Charleston", "Cheyenne", "Columbus"]
Starts_with_D = ["Delaware ", "Denver", "Dover", "Des Moines"]
Starts_with_F = ["Florida ", "Frankfort"]
Starts_with_G = "Georgia"
Starts_with_H = ["Hawaii ", "Hartford", "Honolulu", "Helena", "Harrisburg"]
Starts_with_I = ["Idaho","Illinois","Indiana" ,"Iowa", "Indianapolis"]
Starts_with_J = ["Juneau", "Jackson","Jefferson City" ]
Starts_with_K = ["Kansas", "Kentucky"] 
Starts_with_L = ["Louisiana", "Little Rock","Lansing","Lincoln"]
Starts_with_M = ["Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana", "Montpelier", "Madison", "Montgomery"] 
Starts_with_N = ["Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota", "Nashville"]
Starts_with_O = ["Ohio","Oklahoma","Oregon", "Oklahoma City", "Olympia"]
Starts_with_P = ["Pennsylvania", "Phoenix","Providence","Pierre"]
Starts_with_R = ["Rhode Island", "Raleigh", "Richmond"]
Starts_with_S = ["South Carolina","South Dakota","Sacramento","Springfield","Saint Paul", "Santa Fe","Salem","Salt Lake City"]
Starts_wiht_T = ["Tennessee","Texas","Tallahassee","Topeka","Trenton"] 
Starts_with_U = "Utah" 
Starts_with_V = ["Vermont","Virginia"]
Starts_with_W = ["Washington","West Virginia","Wisconsin","Wyoming"]
