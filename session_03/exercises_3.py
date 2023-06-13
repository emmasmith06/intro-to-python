# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!"
name = input(str("What is your name? "))
if name == "Bob":
  print("Welcome " + name)

# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".
name = input(str("What is your name? "))
if name != "Alice":
  print("You're not Alice")

# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure".
password = input(str("What is your password? "))
if password == "querty124":
  print("You have successfully logged in")
else:
  print("Password failure")

# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".
num = int(input("Enter a number: "))
if num % 2 == 0:
  print("Even")
else:
  print("Odd")

# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
num1  = float(input("What is your first number? "))
num2  = float(input("What is your second number? "))
if num1 + num2 > 21:
  print("Bust")
else:
  print("Safe")
  
# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.
length = float(input("What is the length? "))
width = float(input("What is the width? "))
if length == width:
  print("It is a square")
else:
  print("It is not a square")

# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
salary = float(input("What is your current salary? "))
service = int(input("How long have you worked here (in years) ? "))
if service > 3:
  print("Your salary is " + str(salary) + " and your bonus is " + str(salary*0.1))
else:
  print("No bonus")
  
# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
num = int(input("Choose a whole number "))
if num > 0:
  print(str(num^3))
elif num < 0:
  print(str(num/2))

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".
name = input(str("What is your name? "))
if name == "Bob":
  print("You're not Bob! I'm Bob")
elif name == "Alice":
  print("Hello Alice")
else:
  print("You must be Charlie")

# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"
age = int(input("What is your age? "))
if age==0:
  print("You're not born yet")
elif age<11:
  print("You're too young for school")
elif age>=11 and age<16:
  print("You can come to school")
elif age>-16:
  print("You're too old")

# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".
name = input(str("What is your name? "))
month = input(str("Enter a month "))
if month in ("March", "April", "May"):
  print(month + " is in spring")
elif month in ("June", "July", "August"):
  print(month + " is in summer")
elif month in ("September", "October", "November"):
  print(month + " is in autumn")
elif month in ("December", "January", "February"):
  print(month + " is in winter")
else:
  print("I don't know")

# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.
num1  = float(input("What is your first number? "))
num2  = float(input("What is your second number? "))
if num1%2==0 and num2%2 ==0:
  print("Even")
elif num1%2==1 and num2%2==1:
  print("Odd")
else:
  print(str(num1*num2))

# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.
num1  = float(input("What is your first number? "))
num2  = float(input("What is your second number? "))
if num1>num2:
  print(num1)
elif num1==num2:
  print(str(num1) + "The numbers are the same")
else:
  print(str(num1*num2))

# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
salary = int(input("What is your current salary? "))
service = int(
  
  input("How many years have you worked here? "))
if service >7:
  print("Your bonus is " + str(salary*0.2))
elif service >5:
  print("Your bonus is " + str(salary*0.15))
elif service >3:
  print("Your bonus is " + str(salary*0.1))
else:
  print("No bonus")

# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.
name1 = input("What is the first name? ")
age1 = int(input("What is " + name1 +"'s age"))
name2 = input("What is the second name? ")
age2 = int(input("What is " + name2 +"'s age"))
name3 = input("What is the third name? ")
age3 = int(input("What is " + name3 +"'s age"))
if age1>age2 and age1>age3 and age2<age3:
  print(name1+ " is the oldest and " + name2 +" is the youngest")
elif age1>age2 and age1>age3 and age2>age3:
  print(name1+ " is the oldest and " + name3 +" is the youngest")
elif age2>age1 and age2>age3 and age1<age3:
  print(name2+ " is the oldest and " + name1 +" is the youngest")
elif age2>age1 and age2>age3 and age1>age3:
  print(name2+ " is the oldest and " + name3 +" is the youngest")
elif age3>age1 and age3>age2 and age1<age2:
  print(name3+ " is the oldest and " + name1 +" is the youngest")
elif age3>age1 and age3>age2 and age1>age2:
  print(name3+ " is the oldest and " + name2 +" is the youngest")
else:
  print("Everyone is the same age")
  
# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
lesson1 = input("Input your lesson ")
grade1 = int(input("What is your first mark? "))
lesson2 = input("Input your lesson ")
grade2 = int(input("What is your second mark? "))
lesson3 = input("Input your lesson ")
grade3 = int(input("What is your third mark? "))
if lesson1>80:
  print(lesson1 + ": A")
elif lesson1>=60:
  print(lesson1 + ": B")
elif lesson1>=50:
  print(lesson1 + ": C")
elif lesson1>=45:
  print(lesson1 + ": D")
elif lesson1>=25:
  print(lesson1 + ": E")
else:
  print(lesson1 + ": F")