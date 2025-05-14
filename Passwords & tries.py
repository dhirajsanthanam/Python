"""
Task 5: Passwords & tries (1.5 marks)
This task is similar to Task 4, but:

A password must also be entered,

After 3 unsuccessful tries, the program terminates.

Task Description
Write a program that asks the user to enter a valid username and a valid password. A successful login occurs when the user enters one of the correct usernames and one of the correct passwords. If, after 3 tries, the user did not provide a correct login, the program terminates.

Given the description above, the program can either terminate with a successful login or after 3 unsuccessful attempts.

The usernames and passwords are given below. They are case-sensitive.

Usernames
+----+----+----+----+----+----+----+----+----+----+
| Ava| Leo| Raj| Zoe| Max| Sam| Eli| Mia| Ian| Kim|
+----+----+----+----+----+----+----+----+----+----+
Passwords
+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
| 12345  | abcde  | pass1  | qwert  | aaaaa  | zzzzz  | 11111  | apple  | hello  | admin  |
+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
Input and Output Examples
User inputs are in bold font below.

Example 1
Enter username: Raj
Enter password: pass1
Login successful. Welcome Raj !

Example 2
Enter username: Ian
Enter password: 1234
Login incorrect. Tries left: 2
Enter username: Ava
Enter password: pass1
Login successful. Welcome Ava !


Example 3
Enter username: Rio
Enter password: opqr
Login incorrect. Tries left: 2
Enter username: Ivy
Enter password: pass1
Login incorrect. Tries left: 1
Enter username: Ona
Enter password: aaaaa
Login incorrect. Tries left: 0

"""



"""
Program to check the username and password
Verify them for 3 tries
"""

#mentioning the correct username and password given to be referred
correct_username = ["Ava", "Leo", "Raj", "Zoe", "Max", "Sam", "Eli", "Mia", "Ian", "Kim"]
correct_password = ["12345", "abcde", "pass1", "qwert", "aaaaa", "zzzzz", "11111", "apple", "hello", "admin"]

i = 3 #setting the number of tries to be done in while loop

#using while for infinite loop with 3 tries condition 3,2,1
while i>0 :
    user_name = input("Enter username: ") #collecting the username from the user
    user_password = input("Enter password: ") #getting password

    if user_name in correct_username and user_password in correct_password: #using if statement to check the condition
        print("Login successful. Welcome", user_name,"!")
        break #break to break the infinite loop on success
        
    else : #using else to continue to get the 3 tries from while loop
        i -= 1 #reducing each try from while entry by 1
        if i >= 0: #entering if the condition is met each time from while loop
            print("Login incorrect. Tries left:", i)

