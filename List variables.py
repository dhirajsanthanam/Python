"""
Task 4: List variables (2 marks)
Fibonacci seems exhausted. Intrigued, I mean concerned, you ask Fibo what's on his mind. "I've been marking assignments all weekend", he confesses, while yawning. "What drives me mad is the inconsistency of the variable formatting." You wouldn't happen to be able to help my students with that, would you?". Turns out, you are actually working on the perfect tool to help your mate Fibo!

Task Description
Write a program that allows a user to list the variables of a Python program. We suppose that each variable follows one of three cases:

snake_case,

camelCase, or

PascalCase (a.k.a. Upper camel case).

The programs provided as input may not make sense or be correct. Ignore that.

Program input
When the program is run, the user first inputs the program. For example:

Enter the Python program to analyze, line by line. Enter 'end' to finish.
a = b + c
end
Main menu
Once the program is input, the main menu is displayed. The program prompt of the main menu looks like:

==================================
Enter your choice:
1. Print program.
2. List.
0. Quit.
==================================
If the user inputs 1, 2 or 0, it runs the corresponding function. Assume no other input is provided.

We recommend you create at least one function for each menu option.

1. Print program
Upon inputting 1, your program will then print the program that was provided in input (without the "end"):

==================================
Enter your choice:
1. Print program.
2. List.
0. Quit.
==================================
1
Program:
a = b + c

The programs provided as input may have indentation and/or extra spaces. They need to appear as provided when printing the program. See example 1.

2. List
Upon inputting 2, your program will list the variables of the input program. They are provided in alphanumerical order. Each variable is listed only once.

==================================
Enter your choice:
1. Print program.
2. List.
0. Quit.
==================================
2
Variables:
a
b
c

Use Python's sorting functions, such as sorted. You will notice that uppercase words will be listed before lowercase words. This is what we want.

1
print(sorted(["robbie", "Robbie"]))
For the purpose of this and the following task, all variable names
1. start with a lowercase or uppercase character,i.e. a-z and A-Z,
2. may only contain lowercase or uppercase character,i.e. a-z and A-Z, and underscores, i.e. _,
3. cannot be a Python keyword,
4. are surrounded by at least one space on either side.

The programs provided may contain Python keywords. These are not variables. You can programmatically obtain a list of the possible keywords using keyword.kwlist. See example below.

12
import keyword
print(keyword.kwlist)
The input programs do not contain string literals, such as "hello".

Examples
User inputs are in bold font below.

Example 1
Enter the Python program to analyze, line by line. Enter 'end' to finish.
myVar =   your_var + TheirVar      
for your_var in newVar :
    myVar   += TheirVar
end
==================================
Enter your choice:
1. Print program.
2. List.
0. Quit.
==================================
2
Variables:
TheirVar
myVar
newVar
your_var
==================================
Enter your choice:
1. Print program.
2. List.
0. Quit.
==================================
1
Program:
myVar =   your_var + TheirVar
for your_var in newVar :
    myVar   += TheirVar
==================================
Enter your choice:
1. Print program.
2. List.
0. Quit.
==================================
0
"""


''' to develop a program that allows user to list variables that 
follows :
1. snake case  - each space is replaced with underscore(_)
2. camel case  - writing phrases without spaces or punctuation
3. pascal case  - First letter of compound word in variable is captitalized

so, the program executes as follows:
1. gets input from user until types "end".
2. store the entered line in list.
3. display each line in the list.
4. list the variable function : snake/camel/pascal
 '''

#importing keyword library to exclude python's reserved keywords 
import keyword
#importing re library to sind the reoccurences of a string to return as list 
import re

#method to get input from user 
def get_input():
    user_program = [] #assigning user entered program input with empty list
    print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
    while True: #to execute until terminated by user
        pgm = input() #pgm - program , get the program from user 
        if pgm != 'end': #till the string is not end , read input
            user_program.append(pgm) #add the program to the list 
        else : #if its end - > terminate 
            break
    return user_program #return user program 

def main_menu(): #main funtion to get user choice 
    user_program = get_input()
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Print program.")
        print("2. List.")
        print("0. Quit.")
        print("==================================")
        user_choice = input("") #getting user choice out of 1,2,0
        if user_choice == '1': #if user enter 1:
            print_program(user_program) #print the program
        elif user_choice == '2': #if user enter 2:
            print_list(user_program) #print the variables 
        else:
            break


def print_program(user_program): #creating a function for user program
    print("Program:")
    for character in user_program:
        print(character)

def print_list(user_program):
    variables = set()  #setting variables as set to only contain unique values 
    #to get all python reserved keywords from library and assign to set
    keywords = set(keyword.kwlist)  
    #iterate through the user entered program
    for character in user_program: #iterating each character
        #using regex here because it may only contain lowercase or uppercase character,i.e. a-z and A-Z, and underscores, i.e. _,
        letters = re.findall(r'\b[a-zA-Z_][a-zA-Z_]*\b', character)
        for letter in letters: #for each letter (character) in letters
            if letter not in keywords: #if that string isn't a keyword
                variables.add(letter) #add that letter to variables   
    print("Variables:") #priting variables and using for to sort
    for variable_character in sorted(variables) :
        print(variable_character)

main_menu() #invoking main menu to begin


