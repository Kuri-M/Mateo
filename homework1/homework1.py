#file homework1.py

# --- Variables and Data Types ---

a = 10 
print(a)
print(type(a))
# a is an integer 

b = 1.5
print(b)
print(type(b))
# b is a "float" (decimal)

c = 3j
print(c)
print(type(c))
# c is "complex" (containing a complex (i) componet)

d = "hello"
print(d)
print(type(d))
# d is "str" (string of charaters)

e = [1,2,3]
print(e)
print(type(e))
# e is a "list" (list of numbers)

f = {"Mateo", "blackberry"}
print(f)
print(type(f))
# f is a "set" (unordered collection of unique data types)

g = (1, 2)
print(g)
print(type(g))
# g is a "tuple" (similar to set, though ordered and not unique)

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
# h is another "list"

i = True
print(i)
print(type(i))
# i is a "bool" (boolean values only contain "true" or "false")

j = None 
print(j)
print(type(j))
# j is "NoneType" (represents the absence of a value)

k = [True, "blue", 12]
print(k)
print(type(k))
# k is another "list"

l = str(14)
print(l)
print(type(l))
# l is another string but this time defined by the command str

m = 1e4
print(m)
print(type(m))
# m is scientific notation for 1 * 10^4 and is a "float"


'''
1) I counted 9, as d and l are both strings, b and m are both floats, and e, h, and k are lists. 
2) Integer, float, complex, str, list, set, tuple, bool, nonetype
3) d and l are both strings, b and m are both floats, and e, h, and k are lists. 
4) str(14) changes the integer to a string of 1 and 4, the command changes the data type.
5) range is a looped squence of numbers
'''

# --- Booleans ---

print(10 > 9)
# True, 10 is greater than 9

print(10 == 9)
# False, 10 is not identical to 9

print(10 <= 9)
# False, 10 is not less than or equal to 9

print(bool("abc"))
# True, strings are true

print(bool(123))
# True, integers are true

print(bool(["apple", "cherry", "banana"]))
# True, lists are true

print(bool(True))
# True, true is true

print(bool(False))
# False, false is false 

print(bool(0))
# False, 0 is false 

print(bool(""))
# False, there is nothing in the quotation marks 

print(bool(" "))
# True, there is a space in the quotation marks

print(bool(()))
# False, there is nothing in the ()

print(bool([]))
# False, there is nothing in the []

print(bool({}))
# False, there is nothing in the {}

print(bool(True and False))
# False, both are not true

print(bool(True and True))
# True, both are true

print(bool(False and False))
# False, both are false

print(bool(True or False))
# True, True is first, so "or" prints true
 
print(bool(True or True))
# True, both are true, so true is printed

print(bool(False or False))
# False, both are false, so false is printed

print(bool(not(False)))
# True, not false is true

print(bool(not(True)))
# False, not true is false


'''
1) If false is present, the statement returns false, meanining true only exists if all are true
2) How senstitive true seems to be!
3) print(not(not(true))), double negatives!
4) print(True and True and True and False), one false makes the statement false
'''

# --- Operators ---

# - Arithmetic Operators - 

print(10 + 5)
# 15, + is addition

print(10 - 5)
# 5, - is subtraction

print(2 * 4)
# 8, * is multiplication

print(6 / 3)
# 2 / is division

print(5 % 2)
# 1, % a remainder after division

print(3 ** 2) 
# 9, ** is 3^2

print(15 // 2)
# 7, divides and rounds to nearest integer

# - Comparison Operators -

print(5 == 2)
# False, 5 is not identical to 2

print(10 != 10)
# False, 10! is not 10

print(2 < 5)
# True, 2 is less than 5

print(12 > 5)
# True, 12 is greater than 5

print(5 <= 6)
# True, 5 is less than 6

print(1 >= 10)
# False, 1 is not greater than 10

# - Assignment Operators 

x = 5
print(x)
# x = 5

x += 5
print(x)
# x = 10, 5 + 5

x -= 4
print(x)
# x = 6, 10 - 4 = 6

x *= 3
print(x)
# x = 18, 6 * 3 = 18

# - Logical Operators - 


''' 
1) "and" tests both values, print(True and True) is true because both are true, but print(True and False) is false because one is false
2) "or" prints true when at lease 1 statement is true, print(True or False) is true, while print(False or False) is false 
3) "not" is a negative, giving what the statement is not. print(not(True)) is false, while print(not(False)) is true

More Questions

1) / is exact division, while // is rounded division
2) % gives the remainder of division while / gives exact value
3) %, 5 % 2 is 1 because 5/2 has a remainder of 1
4) Assignment Operators work by re-assigning a value to a variable and sequentially using that new variable
'''

# --- Strings ---

my_string = "hello"
print(my_string)
# Prints "hello"

print(my_string[0])
# Prints the 0th letter of "hello", "h"

print(my_string[1])
# Prints the frist letter, "e"

print(my_string[2])
# Prints the second letter "l"

print(my_string[3])
# Prints the third letter "l"

print(my_string[4])
# Prints the 4th letter "o"

print(my_string[-1])
# Prints the -1st letter, "o"

print(my_string[1:3])
# Prints letters 1 and 3, "e" and "l"

print(my_string[0:5:2])
# Prints letters 0, 5 and 2, "h", "l", and "o"

print(len(my_string))
# The lenth of hello is 5 letters

print(my_string + "goodbye")
# Prints "hello" and "goodbye"

print(7 * my_string)
# Prints "hello" 7 times

'''
1) Using [:] you can print only certain parts of a given variable. We used it to print certain parts of "hello"
2) This gives the result "hello my name is oski," because "name" acts like a variable
3) There is no difference! The f string is a function that defines {name} to be oski.

'''
name = "oski"
print("hello, my name is", name)
print(f"hello, my name is {name}")

# --- Terminal Commands ---

'''
- cd
Change Directory
Changes folder location
cd python_decal_fall25

- ls
list files
lists files
python_decal_fall25 % ls

-ls -a 
lists files, shows hidden folders
python_decal_fall25 % ls -a

- mkdir
Make Directory
makes directory
mkdir homework1

- cat
Concatenate
Text editior
python_decal_fall25 % cat

- pwd
Print Working Directory 
shows the directory your currenlty in
python_decal_fall25 % pwd

- cd ..
Change Directory (to parent)
changes directory to the partent directory
python_decal_fall25 % cd.. -> mateo.kuri

- cd. 
Change Directory (single)
typically doesnt change directory
python_decal_fall25 % cd.

- cd ~ 
Change Directory to home
Changes directory to home
python_decal_fall25 % cd ~ -> mateo.kur

- cp
Copy
Copies
cp homework1

- mv
Move
Moves files
mv homework1 /path/to/homework2/

- rm
Remove
Removes files
rm homework1

-clear
Clear
clears the terminal of text
clear

- grep
Global Regualr Expression Print
searches plaintext data for a given text globaly
grep "hello"

Questions 

1) 
rmdir: Removes an empty directory, 
touch <file_name>: Creates an empty file or updates the timestamp of an existing file
less <file_name>: Displays file content page by page, allowing scrolling.

2) ls -a forces the terminal to show all hiddent folders, while ls only shows non hidden folders

3) 
-h, human readable size
-r recursivly copy directories
-v Verbose output, showing what is being copied

'''