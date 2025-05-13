"""
Task 2: Looting items (2 marks)
"Now all we need to do is get the user to pick up loot and store it in the container!" Robbie explains. "Bada bing, bada boom. It's in the bag! Get it?". 

You do.

Task Description
After reading all items and containers, do not print them, but instead ask the user for a container to pick for the adventure. For example,

Enter the name of the container: A backpack
Main menu
Then, a menu with three options will be shown repeatedly. The program prompt of the main menu looks like:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1. Loot item.
Upon entering 1, the program will then ask for the name of an item to loot. If the item can fit in the container given the remaining capacity, the program indicates so, as shown below.

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A rock
Success! Item "A rock" stored in container "A backpack".

If, instead, the remaining capacity is not sufficient to store the item, the item is not looted:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Fibonnaci's recursive call count
Failure! Item "Fibonnaci's recursive call count" NOT stored in container "A backpack".

If the item's name is not one of the known items, then the user is asked for the name again:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A smaller Fibonnaci's recursive call count
"A smaller Fibonnaci's recursive call count" not found. Try again.
Enter the name of the item: Fibonnaci's rabbytes family tree
Success! Item "Fibonnaci's rabbytes family tree" stored in container "A backpack".

See example 1 for a complete example.

Consider using exceptions (including custom ones) to handle the case where a container cannot store an item.

2. List looted items.
Upon entering 2, the program will then print the container and the list of content, in the order they have been looted:

==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A backpack (total weight: 186, empty weight: 40, capacity: 146/5000)
   A rock (weight: 1)
   Fibonnaci's rabbytes family tree (weight: 144)
   A rock (weight: 1)

Notice how the total weight and capacity of the backpack are updated based on the contents.

Examples
User inputs are in bold font below.

Example 1
Initialised 47 items including 15 containers.

Enter the name of the container: A backpack
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A rock
Success! Item "A rock" stored in container "A backpack".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Fibonnaci's recursive call count
Failure! Item "Fibonnaci's recursive call count" NOT stored in container "A backpack".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A backpack (total weight: 41, empty weight: 40, capacity: 1/5000)
   A rock (weight: 1)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A smaller Fibonnaci's recursive call count
"A smaller Fibonnaci's recursive call count" not found. Try again.
Enter the name of the item: Fibonnaci's rabbytes family tree
Success! Item "Fibonnaci's rabbytes family tree" stored in container "A backpack".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A backpack (total weight: 185, empty weight: 40, capacity: 145/5000)
   A rock (weight: 1)
   Fibonnaci's rabbytes family tree (weight: 144)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: A rock
Success! Item "A rock" stored in container "A backpack".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
A backpack (total weight: 186, empty weight: 40, capacity: 146/5000)
   A rock (weight: 1)
   Fibonnaci's rabbytes family tree (weight: 144)
   A rock (weight: 1)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
0


Example 2
Initialised 47 items including 15 containers.

Enter the name of the container: A bag
"A bag" not found. Try again.
Enter the name of the container: A rock
"A rock" not found. Try again.
Enter the name of the container: Joey's water bowl
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Paul's only frontal lobe
Success! Item "Paul's only frontal lobe" stored in container "Joey's water bowl".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Liz's brain cell cluster
Success! Item "Liz's brain cell cluster" stored in container "Joey's water bowl".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Paul's only frontal lobe
Failure! Item "Paul's only frontal lobe" NOT stored in container "Joey's water bowl".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Liz's brain cell cluster
Success! Item "Liz's brain cell cluster" stored in container "Joey's water bowl".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Joey's water bowl (total weight: 17, empty weight: 2, capacity: 15/20)
   Paul's only frontal lobe (weight: 9)
   Liz's brain cell cluster (weight: 3)
   Liz's brain cell cluster (weight: 3)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Chloe's half baked ideas
Success! Item "Chloe's half baked ideas" stored in container "Joey's water bowl".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Sam's water pouch
Failure! Item "Sam's water pouch" NOT stored in container "Joey's water bowl".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
1
Enter the name of the item: Pierre's funny meme collection
Success! Item "Pierre's funny meme collection" stored in container "Joey's water bowl".
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
2
Joey's water bowl (total weight: 22, empty weight: 2, capacity: 20/20)
   Paul's only frontal lobe (weight: 9)
   Liz's brain cell cluster (weight: 3)
   Liz's brain cell cluster (weight: 3)
   Chloe's half baked ideas (weight: 5)
   Pierre's funny meme collection (weight: 0)
==================================
Enter your choice:
1. Loot item.
2. List looted items.
0. Quit.
==================================
0

"""

"""
Code Logic:

1. **Imports**: The `csv` module is imported for reading data from CSV files.

2. **Item Class**: 
   - Depicts an object with a weight and name.
   - The name and weight are initialized using the "__init__" method, which also removes whitespace and converts weight to an integer.
   - The "__repr__" method provides a string representation for improved debugging and display.

3. **Main Prompt Function**: 
   - gives the user the option to quit, list items, or loot stuff in order to engage with the software.

4. **Container Class**:
     Represents a container that holds items, containing properties for name, empty weight, capacity, and a list of contents.
   - The container is initialized and the initial total weight is set to the empty weight using the "__init__" method.
   - The `display_items` method uses a `while` loop to report the container's information and list of items.
   - If an item does not exceed the container's capacity, the `include_item` method inserts it and updates the total weight accordingly.

5. **CSV Reading Functions**:
   - By reading container data from a given CSV file, `read_containers` creates `Container` objects and stores them in a dictionary.
   - read_items is simlar to `read_containers on an item basis. It builds objects with the name {Item} and keeps them in a dictionary.

6. **Printing Functions**:
   - `printItems` and `printContainers`functions are used to sort and print items and containers.

7. **Main Execution Block**:
   - reads from the corresponding CSV files for items and containers.
   - Shows the quantity of initialized containers and items.
   - Creates a loop to enable user communication:
   - Requests the name of the container and verifies its existence.
   - Shows the main menu with the options to quit, list items, or loot items.
   - If the user decides to loot an item, it prompts for an item name and attempts to put it to the chosen container.
   
   Names used in this code :

   1) Empty Weight is used as EWeight.
   2) Weight Capacity is used as capa.
   3) Filename is used as F_name as parameters
   4) To add an item function name is "include_item"
   5) To display the items the funtion name is "Display_items"
   6) option is used as user input choice 


"""

import csv


# The Item class
class Item:
    def __init__(self, name, weight):
        self.name = name.strip()
        self.weight = int(weight.strip())  # Strip spaces and convert to int

    def __repr__(self):
        return f"{self.name} (weight: {self.weight})"
        
# Function to give the user option
def mainprompt():
        print("==================================")
        print("Enter your choice:")
        print("1. Loot item.")
        print("2. List looted items.")
        print("0. Quit.")
        print("==================================")

# The Container class
class Container:    
    def __init__(self, name, Eweight, cap):
        self.name = name.strip()
        self.Eweight = int(Eweight.strip())  ## Strip spaces and convert to int
        self.cap = int(cap.strip())  ## Strip spaces and convert to int
        self.items = []
        self.total_weight = self.Eweight
     
    # Function to display items looted    
    def display_items(self):
        print(f'{self.name} (total weight: {self.total_weight}, empty weight: {self.Eweight}, capacity: {self.total_weight-self.Eweight}/{self.cap})')
        index = 0
        while index < len(self.items):
            item = self.items[index]
            print(f'   {item}')
            index += 1
            
    # Function to add an item in the container by checking the weight 
    def include_item(self, item):
        
        # Verify if the item is larger than the allowed amount.
        if self.total_weight + item.weight > self.cap + self.Eweight:
            print(f'Failure! Item "{item.name}" NOT stored in container "{self.name}".')
        else:
            self.items.append(item)
            self.total_weight = self.total_weight + item.weight
            print(f'Success! Item "{item.name}" stored in container "{self.name}".')

    def __repr__(self):
        return f"{self.name} (total weight: {self.Eweight}, empty weight: {self.Eweight}, capacity: 0/{self.cap})"

#Function for reading data from a CSV file
def read_containers(F_name):
    cont = {}
    with open(F_name, mode='r') as file:
        csv_readline = csv.reader(file)
        next(csv_readline)  # Do not read the header row.
        for row in csv_readline:
            if row:  
                name, Eweight, cap = row
                cont[name.strip()] = Container(name, Eweight, cap)
    return cont
    
# Function printItems is used to print the Items 
def printItems(item):
    for line in sorted(item, key=lambda x: x.name):
        print(line)

# Function for reading data from a CSV file
def read_items(F_name):
    ReadItems = {}
    with open(F_name, mode='r') as file:
        csv_readline = csv.reader(file)
        next(csv_readline)   # Do not read the header row.
        for row in csv_readline:
            if row:  
                name, weight = row
                ReadItems[name.strip()] = Item(name, weight)
    return ReadItems
 
# Function printContainers is used to print the Containers  
def printContainers(cntr):
    for line in sorted(cntr, key=lambda x: x.name):
        print(line)

"""
#Bubble sort alogorithm for sorting and printing 
def Bubble_Sort_items(items):
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j].name > items[j+1].name:
                items[j], items[j+1] = items[j+1], items[j]
    return items

def Bubble_Sort_containers(containers):
    n = len(containers)
    for i in range(n):
        for j in range(0, n-i-1):
            if containers[j].name > containers[j+1].name:
                containers[j], containers[j+1] = containers[j+1], containers[j]
    return containers
"""

# Main function 
if __name__ == "__main__":
    
    # Open files and read items and container
    items = read_items('items.csv')
    #sorted_items = Bubble_Sort_items(items)
    containers = read_containers('containers.csv')
    #sorted_containers = Bubble_Sort_containers(containers)

    #Print the total number of initialized items and containers.
    print(f"Initialised {len(items) + len(containers)} items including {len(containers)} containers.\n")
    
    #print("Items:")
    #printItems(sorted_items)
    #print("\nContainers:")
    #printContainers(sorted_containers)
    #print()

    #Control Flow : 
    #The structure allows users to continuously interact with
    #containers and items until they choose to exit the program.
    #Option == 0, is used at first for time efficiency 

    while 1:
        container_Username = input("Enter the name of the container: ")
        if container_Username in containers:
            chosen_container = containers[container_Username]
            break
        else:
            print(f'"{container_Username}" not found. Try again.')        
    
    while 1:
        mainprompt() # Display available options
        option = input()

        match option:
            case "0": # Quit option
                break
            case "2":
                chosen_container.display_items()
            case "1": # Loot item option
                while 1:
                    item_Username = input("Enter the name of the item: ")
                    if item_Username not in items:
                        print(f'"{item_Username}" not found. Try again.') # Error if item not found
                    else:
                        item = items[item_Username] # Get the selected item
                        chosen_container.include_item(item) # Attempt to add the item to the container
                        break


