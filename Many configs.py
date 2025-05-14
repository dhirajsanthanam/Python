"""
Task 8: Many configs (2 marks)
This task uses the same movement rules as Task 7, but this time Robbie has multiple keyboard configurations to choose from, and will choose the one that requires the fewest moves. 

Task Description
Write a program that asks the user to input a string, then choose a keyboard, then plans the actions of Robbie the robot so that it can type this string on a keyboard.

For a given input string,

If there is a single keyboard on which in can be typed, then Robbie picks that one.

If it can be typed on multiple keyboards, Robbie picks a single keyboard as follows:

The one that requires the fewest moves, or, if there is a tie, 

The first best keyboard configuration (in the order we give them).

Finally, there may not be a keyboard that can type that string.

The keyboards have the configurations below.

Configuration 0

abcdefghijklm
nopqrstuvwxyz
Configuration 1

789
456
123
0.-
Configuration 2

chunk
vibex
gymps
fjord
waltz
Configuration 3

bemix
vozhd
grypt
clunk
waqfs
Robbie starts at the top left position of the chosen keyboard.

Input and Output Examples
User inputs are in bold font below.

Example 1
Enter a string to type: k
Configuration used:
---------
| chunk |
| vibex |
| gymps |
| fjord |
| waltz |
---------
The robot must perform the following operations:
rrrrp


Example 2
Enter a string to type: .716
Configuration used:
-------
| 789 |
| 456 |
| 123 |
| 0.- |
-------
The robot must perform the following operations:
rdddpluuupddprrup


Example 3
Enter a string to type: y
Configuration used:
---------
| chunk |
| vibex |
| gymps |
| fjord |
| waltz |
---------
The robot must perform the following operations:
rddp


Example 4
Enter a string to type: (╯°□°)╯︵ ┻━┻
The string cannot be typed out.

"""


"""
A program to assume as Robbie with multiple keyboard cofigurations and chooses the fewest moves
"""

#four distinct keyboard layouts, each described as a 2D list where each inner list represents a row of keys, are contained in the configurations list.
configurations = [
    [["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"],
     ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]],
    
    [["7", "8", "9"],
     ["4", "5", "6"],
     ["1", "2", "3"],
     ["0", ".", "-"]],
    
    [["c", "h", "u", "n", "k"],
     ["v", "i", "b", "e", "x"],
     ["g", "y", "m", "p", "s"],
     ["f", "j", "o", "r", "d"],
     ["w", "a", "l", "t", "z"]],
    
    [["b", "e", "m", "i", "x"],
     ["v", "o", "z", "h", "d"],
     ["g", "r", "y", "p", "t"],
     ["c", "l", "u", "n", "k"],
     ["w", "a", "q", "f", "s"]]
]

#assigning a variable keystrokes as empty
keystrokes = ""

#using function if and for loop to check for the characters in the string
def check_keyword(point, validkey):
    for letter in point:
        if letter not in validkey:
            return False
    return True

#similar to above using function, for and if to find the coordinates of the key
def find_keystroke(point, keyboard):
    for y, line in enumerate(keyboard):
        for x, key in enumerate(line):
            if key == point:
                return [x, y]
   
#getting the position of the keys from x and y 
def write_route(position_1, to_position):
    x_initial, y_initial = position_1
    x_final, y_final = to_position

#now calculating the distances between the two positions
    route = ""
    distance1 = x_final - x_initial
    distance2 = y_final - y_initial

#appending the string horizontally r moves right and l moves left
    if (distance1 > 0):
        route = route + distance1 * "r"
    else:
        route = route + abs(distance1) * "l"

#same as above here its done vertically d moves down and u moves up
    if (distance2 > 0):
        route = route + distance2 * "d"
    else:
        route = route + abs(distance2) * "u"

    global position
    position = to_position
    return route + "p"
   
#getting the input and verifying with the given string
entry = input("Enter a string to type: ")

#in order to monitor the optimal keyboard setup, this line initializes variables with the number of movements and no configuration.
config1 = None
keystrokes1 = None
moves1 = float('inf')

#This code determines whether the specified string may be typed using each keyboard setting. It determines how many changes are needed and updates the optimal configuration using the fewest possible steps. 
for value, config in enumerate(configurations):
    if not check_keyword(entry, [key for row in config for key in row]):
        continue
    
    position = [0, 0]
    keystrokes = ""
    moves = 0
    
    for letter in entry:
        to_position = find_keystroke(letter, config)
        if to_position is None:
            break
        route = write_route(position, to_position)
        keystrokes += route
        moves += len(route)
        position = to_position
    
    if moves < moves1:
        moves1 = moves
        keystrokes1 = keystrokes
        config1 = value

#This code determines if a working keyboard setup was discovered. If so, it prints the keyboard layout that has been chosen as well as the steps the robot must take to enter the string. The user is notified that the string cannot be inputted if no valid configuration can be located.
if config1 is not None:
    print("Configuration used:")
    if config1 == 0:
        print("-----------------")
    else:
        print("---------" if config1 != 1 else "-------")
    for row in configurations[config1]:
        print("| " + ''.join(row) + " |")
    if config1 == 0:
        print("-----------------")
    else:
        print("---------" if config1 != 1 else "-------")
    print("The robot must perform the following operations:")
    print(keystrokes1)
else:
    print("The string cannot be typed out.")



