import math

print("Welcome to my game created following my python training course")
print("This programme can be used to solve a sudoku")
#puzzle = input("Enter a sudoku puzzle in the following format [[],[],...,[]], where each [] contains the values in a row with blanks replaced by the value 0")

## Finds next empty space in sudoku
def find_next_empty(puzzle):
  # finds the next row and column with no value in
  # row and column numbers range from 0-8
  # return (none, None) if no blank spaces exist
  for row in range(9):
    for col in range(9):
      if puzzle[row][col] == 0:
        return row, col
  return None, None

## Determines if a cell guess is valid. Returns True if valid and False otherwise
def is_valid(puzzle, guess, row, col):
  # Searching the row
  row_values = puzzle[row]
  if guess in row_values:
    return False
  # Searching the column
  col_values = []
  for r in range(9):
    col_values.append(puzzle[r][col])
  if guess in col_values:
    return False
  # Searching the square
  groupr = (math.floor(row/3))*3
  groupc = (math.floor(col/3))*3
  for r in range(3):
    for c in range(3):
      if puzzle[groupr + r][groupc + c] == guess:
        return False
  #  Else the guess is valid
  return True

## Solves sudoku
def solve_sudoku(puzzle):
  row, col = find_next_empty(puzzle)

  #if there are no blank spaces the sudoku is solved
  if row is None:
    return True
  #make a guess for the number in a space
  for guess in range(1,10):
    if is_valid(puzzle,guess,row,col):
      puzzle[row][col] = guess
      # Recursively call our function
      # If the next free space can have a value places there, then call the function again and so on
      if solve_sudoku(puzzle) == True:
        return True
  # If our guess is not valid or our guess does not solve the puzzle, we need to back-track
    puzzle[row][col] = 0 #reset the guess - now find_next_empty will return this again
  solve_sudoku(puzzle)
  # If there are no combinations that will solve the soduko then return False
  return False

##Prints the solved puzzle in an easily readable format
def print_solved_sudoku(puzzle):
  for r in range(9):
    for c in range(9):
      print(puzzle[r][c],end = " ")
    print()
    
#Test run
puzzle = [[6,3,1,8,0,9,4,2,7],
        [9,7,2,3,0,1,6,0,8],
        [8,5,4,2,7,6,1,0,3],
        [7,1,0,4,6,8,2,3,5],
        [5,4,3,9,0,2,8,7,6],
        [2,6,8,5,3,7,9,0,0],
        [4,9,0,6,2,3,7,8,1],
        [3,0,7,1,9,4,0,6,2],
        [1,2,6,7,8,5,3,4,0]]

if solve_sudoku(puzzle):
  print("Here is your solved sudoku: ")
  print_solved_sudoku(puzzle)
else:
  print("Your sudoku cannot be solved")