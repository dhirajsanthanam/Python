"""
TONY'S PYTHON PRACTICE SCRIPT - Version 1.0
-------------------------------------------
Author: Tony
Date: 2025-05-04

This script contains:
1. A reminder to document your code
2. A year checker that tells if a year is before or after 2000
"""

# --- Part 1: Documentation Reminder ---

# Prompt user for their name
user_name = input("Please enter your name >> ").strip().title()

# Display reminder message
output_message = f"Hello {user_name}. Please remember to document your code~"
print(output_message)

print("\n---\n")  # Simple line break between parts

# --- Part 2: Year Checker ---

# Prompt user for a year
user_year = int(input("Please enter a year: "))

# Determine if year is before, after, or exactly 2000
if user_year < 2000:
    print(f"The year {user_year} is before 2000.")
elif user_year > 2000:
    print(f"The year {user_year} is after 2000.")
else:
    print("The year is exactly 2000.")