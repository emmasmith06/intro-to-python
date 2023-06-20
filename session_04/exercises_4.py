# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.
items = ["Apple","Cherry","Pear","Pineapple","Peach"]

# 2. Add "Grapes" to the list and print the list.
items.append("Grapes")
print(items)

# 3. Change "Pears" to "Strawberries" and print the list.
items[2] = "Strawberry"
print(items)
type(items)

# 4. Remove "Apples" from the list and print the list.
del(items[0])
print(items)

# 5. Print out the current length of the list.
print(len(items))

# 6. Order the list alphabetically.
items.sort()

# 7. Print out the list again.
print(items)



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.
for item in items:
  print(item)

# 2. Print the numbers 1 to 100 (including the number 100).
numbers = range(1,101)
for number in numbers:
  print(number)

# 3. Print all odd numbers from 1 to 100.
for number in numbers:
  if number%2 == 1:
    print(number)

# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).
years = range(1896,2023,4)
for year in years:
  if year not in [1916,1940,1944,2020]:
    print(year)
  
# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
randomnums = randrange(10)
evencount = 0
offcount = 0
for num in randomnums:
  if num%2==0:
    evencount += num
  else:
    oddcount += num

# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
names = ["Em","Rach","Amy"]
for name in names:
  print("Hello " + name)

# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".
word = "supercalifragilisticexpialidocious"
for letter in word:
  print(letter)

# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
numbers = [1,2,3,4,5]
for num in numbers:
  numbers.append(num^2)
  
# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.
names = ["Em","Rach","Amy"]
for name in names:
  names.append("Dr "+ name)
print(names)

# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```
