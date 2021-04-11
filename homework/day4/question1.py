# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:42:33 2021

@author: ozgur
"""

dict = {}

while True:
    student = input("Please enter students name: ")
    if student == "q":
        break
    midterm = input("Please enter students midterm grade: ")
    project = input("Please enter students project grade: ")
    final = input("Please enter students final grade: ")
    passingGrade = float(midterm) * 0.3 + float(project) * 0.3 + float(final) * 0.4
    dict[student] = passingGrade
    
print(dict)

sırasız = list(dict.values())
names = list(dict.keys())

sıralı = sorted(sırasız)
highest = sıralı[-1]
kim = sırasız.index(highest)
highest1 = names[kim]
print(round(highest,1))
print("Student with the highest Grade is:" +highest1)