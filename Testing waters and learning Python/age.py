"""

You have been hired to create an automated bouncer for the new club ‘Infotheque’. 

People are only permitted to enter the club if they are over the age of 18 and have a valid ID. 

Write a program that takes in a person’s age and whether or not they have a valid ID and prints an appropriate message based on whether:

They are over 18 and have a valid ID

They are over 18 and do not have a valid ID

They are under 18 and have a valid ID

They are under 18 and do not have a valid ID

"""

user_age = int(input("Please enter your age "))
user_id = input("do you have a valid id Yes or No " )

if user_age >=18 and user_id == "Yes":
    print("They are over 18 and have a valid ID")
elif user_age >=18 and user_id == "No":
    print("They are over 18 and have a valid ID")
elif user_age <18 and user_id == "Yes":
    print("They are under 18 and have a valid ID")
elif user_age <18 and user_id == "No":
    print("They are under 18 and have a valid ID")
