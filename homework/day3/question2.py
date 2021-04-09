# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:16:45 2021

@author: ozgur
"""

database={'ozgur': '123', 'gumus': '456', 'abc': '789'}

username = input("Username:\n")
if username in database:
    password = input("Password:\n")   
    if password in database[username]:
        print("User has been identified, Welcome", username)
    else:
        print("That is the wrong password.")
else:
    print("That is the wrong username.")