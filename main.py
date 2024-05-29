# Greetings 

print("Hi")
print("First question")
Score = 0 
Name = input("What's your name?")
#Comments
Comments_1 = ["Correct Answer", "Fantastic"]
Comment_2 = ["Wrong Answer", "Oops!"]
# All Questions 
QS_0 = [input("What is the capital of Australia?").lower().upper()]
qs_0 =["Canberra", "Melbourne", "Adelaide"] 
if QS_0 == (qs_0[0]).lower().upper():
   print(Comments_1[0])
   Score = 5
else:
   print(Comment_2[0])
QS_1 = [input("What is the capital of New Zealand?").lower().upper()]
qs_1 = ["Cantenbury", "Wellington", "Auckland"]
if QS_1 == (qs_1[1]).lower().upper():
   print(Comments_1[1])
   Score = 10
else:
   print(Comment_2[1])
QS_2 = [input("What is the capital of India?").lower().upper()]
qs_2 = ["New Mumbai", "New Delhi", "New york"]
if QS_2 == (qs_2[1]).lower().upper():
   print(Comments_1[0])
   Score = 15
else:
   print(Comment_2[0])
QS_3=  [input("What is the capital of Bahrain?").lower().upper()]
qs_3 = ["Alabama", "Manama", "Panama"]
if QS_3 == (qs_3[1]).lower().upper():
   print(Comments_1[1])
   Score = 20
else:
   print(Comment_2[1])
QS_4 = [input("What is the capital of Tamil nadu?").lower().upper()]
qs_4 = ["Pondicherry", "Madras", "Chennai"]
if QS_4 == (qs_4[2]).lower().upper():
   print(Comments_1[0])
   Score = 25
else:
   print(Comment_2[0])
print("Thank you {} for playing, Your Total score is {}").format(Name).format(Score)
play = "Yes".lower().upper()
while play == input("Want to play again?"):
   print("Let's begin our quiz again!")
   play = input("Do you want to play again?")
while True:
   try:
      Attempts = (input("How many attempts do you want for each question? 1-4"))
      Attempts = int(Attempts - 1)
      break
   except:
      print("That's not a number")
while play == "Yes":
   question_attempts = Attempts
QS_0 = [input("What is the capital of Australia?").lower().upper()]
qs_0 =["Canberra", "Melbourne", "Adelaide"] 

   