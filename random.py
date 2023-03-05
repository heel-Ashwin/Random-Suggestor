# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 20:11:16 2022

@author: ramsh
"""

import string
import random

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for password/end generation from these :
         1. Letters
         2. Digits
         3. Special characters
         4. Exit''')

characterList = ""

# Getting character set for password
choice = int(input("Pick a number "))
if (choice == 1):
        # Adding letters to possible characters
    characterList += string.ascii_letters
elif (choice == 2):
        # Adding digits to possible characters
    characterList += string.digits
elif (choice == 3):
        # Adding special characters
    characterList += string.punctuation
elif (choice == 4):
    print("Thank you")
else:
    print("Please pick a valid option!")

password = []
# password is generated only after exiting 

for i in range(length):
    # Picking a random character from our
    # character list
    randomchar = random.choice(characterList)

    # appending a random character to password
    password.append(randomchar)

# printing password as a string
print("The random password is " + "".join(password))
