"""
Task 1: Items and containers (0.5 marks)
In preparation for the summer break, Robbie is coding up an adventure game. He's asked whether you could take care of the looting aspect of the game. With Fibonacci as product manager, what could possibly go wrong?

Task Description
Write a program that reads items and containers from files items.csv and containers.csv, and prints the list of items.

For this and following tasks, do not create files or write into existing files.

As in previous assignments, you are allowed to use any standard Python feature and module. In particular, sorted can be useful here.

We recomend you read all tasks to plan the design of your program so as to minimise the refactoring effort from task to task.

Items
An item has:

a name, and

a weight.

We recommend you create a class to represent items.

Containers
A container has: 

a name,

an empty weight, i.e. their weight when they are empty, and

a weight capacity, i.e. the maximum combined weight that the container can hold.

- Two copies of the same item or container can exist. If two items or containers have the same name, then they have the same characteristics (e.g. weight).
- Throughout the assignment, all weights and weight-related measures (i.e. weight capacities) are non-negative integers.

We recommend you create a class to represent containers.

Expected output
In the output below, notice "47 items". This is because the containers are included in this count.

There are no user inputs in the example below.

Initialised 47 items including 15 containers.

Items:
A normal cheese platter (weight: 1000)
A rock (weight: 1)
Bhagya's publications (weight: 8002)
Charlie's unread emails (weight: 247)
Chloe's half baked ideas (weight: 5)
Chloe's late assignments (weight: 999999)
Crimpy's destroyed cat toys (weight: 27)
Ed's forum posts (weight: 678)
Elena's fishing count (weight: 3500)
Fibonnaci's rabbytes family tree (weight: 144)
Fibonnaci's recursive call count (weight: 10946)
Gabe's Steam game library (weight: 0)
Hui's Hidden Hamster Hoard (weight: 3141)
Lifi's browser tabs (weight: 1337)
Liz's brain cell cluster (weight: 3)
Michael's stack of unmarked assignments (weight: 10000)
Paul's cringe tiktok compilation (weight: 23)
Paul's missing aura points (weight: 22)
Paul's only frontal lobe (weight: 9)
Pierre's daily cheese wheel (weight: 100)
Pierre's funny meme collection (weight: 0)
Pierre's meme collection (weight: 9001)
Pierre's outdated meme collection (weight: 9001)
Pierre's secret meme collection (weight: 420)
Rehan's Book collection (weight: 7005)
Robbie's final drop of sanity (weight: 0)
Robbie's shower thoughts (weight: 150)
Sam's water pouch (weight: 1)
Tan's Tamagotchi Support Group (weight: 410)
Taylor's ex-lovers list (weight: 999)
Vanessa's hit list (weight: 299)
Vanessa's secret gold stash (weight: 2028)

Containers:
A backpack (total weight: 40, empty weight: 40, capacity: 0/5000)
A carrybag for pets (total weight: 50, empty weight: 50, capacity: 0/2000)
A coles shopping bag (total weight: 1, empty weight: 1, capacity: 0/1000)
A container (total weight: 100, empty weight: 100, capacity: 0/250000)
A delicate flower vase (total weight: 5, empty weight: 5, capacity: 0/25)
A full bag of chips (total weight: 2, empty weight: 2, capacity: 0/5)
A large pouch (total weight: 3, empty weight: 3, capacity: 0/80)
A medium pocket (total weight: 0, empty weight: 0, capacity: 0/200)
A small pocket (total weight: 0, empty weight: 0, capacity: 0/100)
A small pouch (total weight: 1, empty weight: 1, capacity: 0/20)
A suitcase (total weight: 100, empty weight: 100, capacity: 0/20000)
A wheelbarrow (total weight: 100, empty weight: 100, capacity: 0/10000)
A woolworths shopping bag (total weight: 1, empty weight: 1, capacity: 0/1200)
Joey's water bowl (total weight: 2, empty weight: 2, capacity: 0/20)
One of those blue ikea tote bags (total weight: 3, empty weight: 3, capacity: 0/8000)


Use left and right arrow keys to adjust the split region size
"""


"""
Logic:
1. **Item Class**: 
   - Represents an item (items.csv) with a name and weight(integer).
   - The constructor initializes these attributes, the constructor makes sure the weight is converted to an integer and that any additional whitespace is removed from the name.

2. **Container Class**:
   - Represents a Holder (container) that can hold items, defined by its name, empty weight, and capacity.
   - Similar to the `Item` class, the constructor ensures values are properly formatted.

3. **Reading Functions**:
   - `read_items(F_name)`: reads item information from a given CSV file. It examines each row without reading the header and produces an instance of {Item} for every row that is valid.
   - `read_containers(F_name)`: Works similarly for containers, making sure that before generating a new instance of a `Container`, it makes sure that each row has sufficient data.

4. **Main Function**:
   - creates lists of things and containers by calling the reading functions.
   - Prints the total number of items and containers initialized.
   - Sorts and displays the items using PrintItems and containers using PrintContainers by name 

5. **CSV Handling**:
   - The code takes CSV files  "items.csv" and "containers.csv", where a row of data represents each item or container.

6. **Execution**:
   - Python commonly uses this technique to allow file imports without running the main function, meaning that the `main()` function is only called when the script is performed directly.

   Names used in this code 

   1) Empty Weight is used as EWeight.
   2) Weight Capacity is used as capa.
   3) Filename is used as F_name as parameters
   4) Cont is considered as container in this code

"""




import csv

# The Item class
class Item:
    def __init__(self, name, Weight):
        self.name = name.strip()
        self.Weight = int(Weight.strip())

    def __repr__(self):
        return f"{self.name} (weight: {self.Weight})"

# The Container class.
class Container:
    def __init__(self, name, EWeight, cap):
        self.name = name.strip()
        self.EWeight = int(EWeight.strip())  
        self.cap = int(cap.strip())  

    def __repr__(self):
        return f"{self.name} (total weight: {self.EWeight}, empty weight: {self.EWeight}, capacity: 0/{self.cap})"

#Function for reading data from a CSV file
def Read_Containers(F_Name):
    cont = []
    with open(F_Name, mode='r') as file:
        csv_readline = csv.reader(file)
        next(csv_readline)  # Do not read the header row.
        for line in csv_readline:
            if line :  
                name, EWeight, capa = line
                cont.append(Container(name, EWeight, capa))
    return cont

# Function printItems is used to print the Items 
def printItems(item):
    for line in sorted(item, key=lambda x: x.name):
        print(line)

# Function for reading data from a CSV file
def Read_Items(F_Name):
    ReadItems = []
    with open(F_Name, mode='r') as file:
        csv_readline = csv.reader(file)
        next(csv_readline)  # Do not read the header row.
        for line in csv_readline:
            if line : 
                name, weight = line
                ReadItems.append(Item(name, weight))
    return ReadItems

# Function printContainers is used to print the Containers 
def printContainers(cntr):
    for line in sorted(cntr, key=lambda x: x.name):
        print(line)

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


# Main function
if __name__ == "__main__":
    
    # Open files and read items and container
    items = Read_Items('items.csv')
    containers = Read_Containers('containers.csv')
    sorted_items = Bubble_Sort_items(items)
    sorted_containers = Bubble_Sort_containers(containers)

    #Print the total number of initialized items and containers.
    print(f"Initialised {len(items) + len(containers)} items including {len(containers)} containers.\n")
    print("Items:")
    printItems(sorted_items)
    print("\nContainers:")
    printContainers(sorted_containers)
    print()

