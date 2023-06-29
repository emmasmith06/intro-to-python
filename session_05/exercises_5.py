# Session 5 Exercises

## Section A
# 1. Print 10 random numbers.
import random
for i in range(10):
  num = random.random()
  print(num)
  i=i+1

# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".
#     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .
luckynum = 1
while luckynum != 7:
  luckynum = int(input("What is your lucky number? "))
# luckynum = random.randint(1,10)
  if luckynum == 7:
    print("Wow lucky number 7!")

# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. 
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.
import math
width = int(input("What is the width in cm? "))
height = int(input("What is the height in cm? "))
area = width * height
if len(str(area))>4:
  area = math.ceil(area/10000)
  print("The area is " + str(area) + " m2")
else:
  print("The area is " + str(area) + " cm2")

# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure" and then ask them to enter it again. 
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".
counter = 0
while counter<4:
  password = input("What is the password ")
  if password == "Qwerty":
    print("You have successfully logged in")
    break
  else:
    print("Password Failure")
  counter += 1

# 5. Add up all the numbers from 1 to 500 and print the answer.
counter = 1
sum = 0
while counter < 501:
  sum += counter
  counter += 1
print(sum)

# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. 
#   Find the index at which the user entered the number 99.
list = []
counter = 0
while counter < 10:
  num = int(input("Choose a number (1 must be 99) "))
  list.append(num)
  counter += 1
print(list.index(99))

# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36
for i in range(16):
  print(str(i)+" x 18 = "+str(i*18))

# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.
counter = 1
while counter<101:
  print(counter)
  counter +=1

# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.


# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name
counter = 1
names = []
while name!= " ":
  name = input("What is the name of someone in the prize draw? (Enter blank to stop)")
  names.append(name)
  counter +=1

print(random.choice[names])

# 11. Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games
choices = ["Rock","Papar","Scissors"]
i=1
wincount = 0
losecount = 0
while i<4:
  userchoice = input("What is your choice? ")
  if userchoice == random.choice(choices):
    print("Draw")
  elif userchoice == "Rock" and random.choice(choices) == "Paper":
    print("You lose")
    losecount += 1
  elif userchoice == "Rock" and random.choice(choices) == "Scissor":
    print("You win")
    wincount += 1
  elif userchoice == "Scissor" and random.choice(choices) == "Paper":
    print("You win")
    wincount += 1
  elif userchoice == "Scissor" and random.choice(choices) == "Rock":
    print("You lose")
    losecount += 1
  elif userchoice == "Paper" and random.choice(choices) == "Rock":
    print("You win")
    wincount += 1
  elif userchoice == "Paper" and random.choice(choices) == "Scissor":
    print("You lose")
    losecount += 1  
if wincount > losecount:
  print("You win")
elif wincount< losecount:
  print("You lose")
else:
  print("It's a draw")