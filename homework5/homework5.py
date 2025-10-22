
# Homework 1-2 Review
'''
Git vs Github. Git is the program that connects to Github, where Github is an online repository to store and save your code. 
Git is just the program that allows this transfer

Terminal vs Command Line. The terminal is the central place in your computer to run code, and the command line is the input 
space to allow a user to input commands into the terminal

Local vs Remote Repository. The local repository is a local saved file that holds information temporarily for accessible use. 
The remote repository is an online repository to store longer lasting larger files and projects for permanent use.

Version Control. Helps keep a version history saved so a file's changes can be tracked and edited. 

Staging Area. The "area" you push files into to get them ready for Github.

Git Add. Add the files into the staging area.

Git Commit. "Commits" the files into the staging area to be pushed.

Git Push. Actually pushes the files to Github.

Git Status. Shows the file status and location.

Git Pull. "Pulls" information from the remote repository and updates a local one.

Pwd. Shows current working directory.

Ls. Lists everything in the directory.

Cd. Change directory.

Nano. A text editing file in the terminal.

Touch. Creates a new file in the working directory.

Mv. Moves a file to another location.

Rm. Removes a file.

Cat. Display, combine, or move files in the terminal.
'''


# A Directory Tree
'''
1 - pwd, to see what directory you are in
2 - ls, to list everything
3 - cd brianna_repo 
4 - mv homework.py homework/
5 - cd homework.py
6 - ls or nano to see the actual text
7 - git add, git commit and git push
8 - Pull the changes the remote repo has onto the local, and then push again to save
9 - pwd will show the absolute path to the recent folder
'''

# Data Types
print(
type(3.14),
type(True))

# Conditionals

def is_even_or_odd(number):
  if number % 2 == 0:
    return 'Even'
  else:
    return 'Odd'
print(is_even_or_odd(4)) # even
print(is_even_or_odd(5)) # odd


# For Loops

def calculate_sum(number2):
  
  total = 0  # Start with a total of zero
  for number2 in number2:
    total += number2  # Add each number to the total
  return total
my_list = [1,2,3,4,5]
print(calculate_sum(my_list)) # =15


# Duplicate Lists

def duplicate_list(items):
  new_list=[]
  for item in items:
    new_list.append(item)
    new_list.append(item)
  return new_list
print(duplicate_list([1,2,3,4,5])) # Returns [1,1,2,2,3,3,...]


# def square(num) 
# return num * num
# The fix is:
def square(num):
  return num **2
print(square(4))



# Favorite Function:
'''
def calculate_sum(number2):
  
  total = 0 
  for number2 in number2:
    total += number2 
  return total
my_list = [1,2,3,4,5]
'''
print(calculate_sum(my_list))