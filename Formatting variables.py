"""
Task 5: Formatting variables (2 marks)
Task Description
Write a program that, on top of the previous options, offers to format variables to snake_case.

Main menu
The main menu now looks like:

==================================
Enter your choice:
1. Print program.
2. List.
3. Format.
0. Quit.
==================================

3. Format
Upon inputting 3, the program asks you to pick one of the variables, and changes its case to snake_case throughout the whole program. For example, if a variable name is:

RobbieTheRobbotor robbieTheRobbot, then it becomes robbie_the_robbot,

robbie_the_robbot, then it remainsrobbie_the_robbot.

If the variable name input by the user does not exist, the program asks again. This is case-sensitive.

Examples
User inputs are in bold font below.

Example 1
Enter the Python program to analyze, line by line. Enter 'end' to finish.
aBC = DeF + a_b_x
end
==================================
Enter your choice:
1. Print program.
2. List.
3. Format.
0. Quit.
==================================
2
Variables:
DeF
aBC
a_b_x
==================================
Enter your choice:
1. Print program.
2. List.
3. Format.
0. Quit.
==================================
3
Pick a variable:
aBC
==================================
Enter your choice:
1. Print program.
2. List.
3. Format.
0. Quit.
==================================
1
Program:
a_b_c = DeF + a_b_x
==================================
Enter your choice:
1. Print program.
2. List.
3. Format.
0. Quit.
==================================
3
Pick a variable:
skibidi
This is not a variable name.
Pick a variable:
a_b_x
==================================
Enter your choice:
1. Print program.
2. List.
3. Format.
0. Quit.
==================================
2
Variables:
DeF
a_b_c
a_b_x
==================================
Enter your choice:
1. Print program.
2. List.
3. Format.
0. Quit.
==================================
0

    
"""

'''
Extending the previous program to add fromatting options
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

#main menu to display the choices and get user choice 
def main_menu():
    user_program = get_input() #calling method to get input from user
    while True: #to execute until terminate
        print("==================================")
        print("Enter your choice:")
        print("1. Print program.")
        print("2. List.")
        print("3. Format.")
        print("0. Quit.")
        print("==================================")
        user_choice = input("") #getting user choice out of 1,2,0
        if user_choice == '1': #if user enter 1:
            print_program(user_program) #print the program
        elif user_choice == '2': #if user enter 2:
            characters = print_variables(user_program) #print the variables 
        elif user_choice == '3': #if user enter 3:
            characters = set(re.findall(r'\b[a-zA-Z_][a-zA-Z_]*\b', "\n".join(user_program)))
            print_different_format(user_program,characters) #print to snake case
        else:
            break


def print_program(user_program): #creating a function for user program
    print("Program:")
    for character in user_program:
        print(character)

def print_variables(user_program):
    variables = set()  #setting variables as set to only contain unique values 
    #to get all python reserved keywords from library and assign to set
    keywords = set(keyword.kwlist)   
    #iterate through the user entered program
    for character in user_program: #iterating each character
        #using regex here because it may only contain lowercase or uppercase character,i.e. a-z and A-Z, and underscores, i.e. _,
        letters = re.findall(r'\b[a-zA-Z_][a-zA-Z_]*\b', character) 
        for letter in letters: #for each letter (character) in letters 
            if letter not in keywords:  #if that string isn't a keyword
                variables.add(letter) #add that letter to variables       
    print("Variables:") #display variables
    for variable_character in sorted(variables) : #sort in alphabetical order
        print(variable_character) #display variables 

def convert_snake_case(variable): #convert to snake case (insert underscore)
    snake_case_variable = re.sub(r'(?<!^)(?=[A-Z])', '_', variable).lower() #the new snake case variables substitutes with '_' in the place of characters in regex
    return snake_case_variable #return new variable in snake case

#print the user picked variable in different format (snake case)
def print_different_format(user_program,characters):
    while True: #execute until valid variable entered
        picked_variable= input("Pick a variable:\n") #get user picked variable
        #check if picked variable exist in the list of variables (named characters to avoid overriding)
        if picked_variable in characters:
            #if exist then, convert to snake case 
            snake_case_var = convert_snake_case(picked_variable)
           #iterate through the start to end of user program
            for i in range(len(user_program)):
                #replace all occurences of user program with the snake case and handle special characters (used in regex)
                user_program[i] = re.sub(r'\b' + re.escape(picked_variable) + r'\b', snake_case_var, user_program[i])          
            #remove and update user picked variable
            characters.remove(picked_variable)
            #adds newly changed user picked variable in that place 
            characters.add(picked_variable)
            break #stop execution
        else: #if the user picked variable name does not exist then, display not valid
            print(f"This is not a variable name.")

main_menu() #invoking main menu to begin


