# Session 7 Exercises

## Section A
# 1. Write a function that prints your name
def printName():
  name = input("What is you name? ")
  print(name)

# 2. Write a function that accepts a name as a parameter and prints "Hello, <name>".
def printName2(name):
  print("Hello, " + name)
printName2("Emma")

# 3. Loop through the list ["Alice", "Bob", "Charlie"] and call the function you just wrote.
listOfNames = ["Alice", "Bob", "Charlie"]
for name in listOfNames:
  printName2(name)

# 4. Write a function that prints the area of two passed in parameters.
def area(x,y):
  print(str(x*y))
area(3,2)
# 5. Write a function called 'print_list' that accepts a list as a parameter and then prints out each item of the list.
def print_list(list):
  for name in list:
    print(str(name))
  
# 6. Put the following into a function that accepts age as a parameter:
#     1. If they are younger than 11, print "You're too young to go to this school".
#     2. If they are between 11 and 16, print "You can can come to this school".
#     3. If they are over 16, print 'You're too old for school".
#     4. If they are 0, print "You're not born yet!".
def canGoSchool(age):
  if age ==0:
    print("You are not born yet")
  elif age<=11:
    print("You are too young")
  elif age<=16:
    print("You can come")
  else:
    print("Too old)")

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Write a function called is_odd that will return True or False if the integer passed as a parameter is odd (hint: x % 2 will return true for all odd numbers).
def is_off(x):
  if x%2!=0:
    return True
  else:
    return False

# 2. Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'.
def word_back(word):
  x = len(word)
  ouput = ''
  for i in range (0,x,-1):
    output += word[i]

# 3. Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars on each line, E.g:
# ```
# *****
# ****
# ***
# **
# *
# ```
def printStar(num):
  star = ""
  for x in range(0,num):
    star += "*"
  print(star)
  if num > 1:
    printStar(num-1)
printStar(2)

# 4. Create a padlock function. You need to be able to pass in a passcode and if its correct it should return "Unlock", else "Locked".
def padlcok(password):
  if password == "MyPassword":
    return "Unlocked"
  else:
    return "Locked"

# 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
#   For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
def multiples(limit):
  sum = 0
  for number in range(1,limit+1):
    if number%3==0 and number%5==0:
      sum += number
    elif number%3==0:
      sum += number
    elif number%5 == 0:
      sum += number
    else:
      sum=sum
  print(sum)
multiples(5)
multiples(6)


# 6. Write a function called is_prime() that accepts a number and return True or False if the number of prime or not.

def is_prime(num):
  count = 0
  for i in range (2,num):
    if num%i == 0:
      count +=1
      break
  if count==0 and num!=1:
    print("prime number")
    return True
  else:
    print("Not prime")
    return False
      
# 7. Write a function that checks to see if a string is a pallindrome, if it is, it will return True and False if it is not.
def isPallindrome(word):
  word = word.lower()
  x = len(word)
  for i in range (0,x):
    if word[i]!=word[-i-1]:
      return False
      break
  return True

print(isPallindrome("Emma"))
print(isPallindrome("Hannah"))

# 8. Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is not. 
#   Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.
def isPallindrome2(sentence):
  sentenceLower = isPallindrome.lower()
  sentenceWord = sentenceLower.replace(" ","")
  x = len(sentenceWord)
  for i in range (0,x,-1):
    if sentenceWord[i]!=sentenceWord[-i-1]:
      return False
      break
  return True

print(isPallindrome("Emma is happy "))
print(isPallindrome("Hannah sis hannah"))
  
  