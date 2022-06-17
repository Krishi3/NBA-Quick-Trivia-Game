print ("Hello! Welcome to the anual NBA trivia! Please enter your name below to begin.")
name = str(input('Name:'))
print ("Hi",name,",")
print("Before beginning this NBA trivia, please note that you must enter full forms of your answers to get them correct!")
#question 1
q1 = print("Who is currently the #1 team in the west coast conference in the NBA?")
a1= str(input('Answer:'))
if a1 == "Pheonix Suns":
  print("You are correct! You just gained 100 points:)")
  sum = 100
elif a1 != "Pheonix Suns":
  print("You are incorrect! It is Pheonix Suns.")
q2 = print("Which NBA player made the most 3 pointers in their career")
a2= str(input('Answer:'))
#question 2
if a2 == "Steph Curry":
  print("You are correct! You just gained 50 points:)")
  sum1 = 50
elif a2 != "Steph Curry":
  print("You are incorrect! It is Steph Curry.")
#question 3
q3 = print("In what year did the Toronto Raptors win the championship?")
a3= str(input('Answer:'))
if a3 == "2018":
  print("You are correct! You just gained 200 points:)")
elif a3 != "2018":
  print("You are incorrect. The Toronto Raptors won the NBA Championship in 2018.")
#question 4
q4 = print("Who won the 2020-2021 NBA Finals?")
a4= str(input('Answer:'))
if a4 == "Milwaukee Bucks":
  print("You are correct! You just gained 300 points:)")
elif a4 != "Milwaukee Bucks":
  print("You are incorrect. The Milwaukee Bucks won the NBA Championship in 2020-2021.")
#question 5
q5 = print("Who is your favourite NBA team?")
a5= str(input('Answer:'))
if a5 == "Milwaukee Bucks" or a5 != "Milwaukee Bucks":
  print("Any answer is correct! You just gained 400 points:)")
print("Thank you for playing the NBA trivia game! Hope you enjoyed.")
