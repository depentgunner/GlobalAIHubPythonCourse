# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:25:57 2021

@author: ozgur
"""


username = "ozgur"

password = "123"

userInput = input("Username:\n")

if userInput == username:
    userInput = input("Password:\n")   
    if userInput == password:
        print("User has been identified, Welcome", username)
    else:
        print("That is the wrong password.")
else:
    print("That is the wrong username.")
 