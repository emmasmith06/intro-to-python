# Session 2 Exercises
length = len("LaanTuring")
middle_letter = "alanTuring"[int(length/2)].lower()
print(middle_letter)
## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
width = 1
height = 2
area = width * height
print("A rectangle with width " + str(width) + " and height " + str(height) + " has an area of " + str(area))

# 2. Write code that prints the length of the string, 'python'.
print(len("Python"))

# 3. Print out the first and third letter of the word 'python'.
print("Python"[0] + "Python"[2])

# 4. Ask the user to enter their name, and print out `Hello, <name>`.
name = input(str("what is your name?"))
print("Hello, " + name)

# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
age = input(int("What is your age?"))
print("In 15 years time you will be " + str(int(age) + 15))

# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.
print("Hello, "+name+", you are currently "+str(age)+" years old. In 15 years time you will be "+str(age+15))

# 7. Ask the user to enter their hometown, print it out in uppercase letters.
hometown= input(str("What is you're hometown?"))
print(hometown.upper())

# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.
fav_colour = input(str("What is your favourite colour?"))
print(len(fav_colour))

# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.
month = input(str("What is the month? "))
weather = input(int("What temperature is it today? "))
print("It is " +month+" and the weather is "+weather)

# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.
month = input(str("What is the month? "))
temp1 = input(int("What is temperature is it for the next 5 days? Day 1: "))
temp2 = input(int("What is temperature is it for the next 5 days? Day 2: "))
temp3 = input(int("What is temperature is it for the next 5 days? Day 3: "))
temp4 = input(int("What is temperature is it for the next 5 days? Day 4: "))
temp5 = input(int("What is temperature is it for the next 5 days? Day 5: "))
avg_temp = (temp1+temp2_temp3+temp4+temp5)/5
print("It is " +month+" and the average temperature is "+str(avg_temp))

# 11. Print out the above sentence but make the month upper case.
print("It is " +month.upper()+" and the average temperature is "+str(avg_temp))

# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.
fav_animals = input("What are your favourite animals? ")
print("Your favourite animals are" + fav_animals)

# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.
name = input("What is your name?" )
fav_number = int(input("What is your favourite whole number? "))
print(name[fav_number])

# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
Welcome_mess = "WelcometoPython"
print(Welcome_mess.slice(1,-1,2))