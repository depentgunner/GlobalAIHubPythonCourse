# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 02:44:34 2021

@author: ozgur
"""


class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "Question1: Who is the coach of Boston Celtics?\n",
     "Question2: Who is the 2019-2020 NBA regular season MVP?\n",
     "Question3: Who is the richest person on the planet?\n",
     "Question4: What is the name of the largest mountain on earth?\n",
     "Question5: What is the name of the actor who plays Heisenberg in Breaking Bad?\n",
     "Question6: Which planet is closest to the sun?\n",
     "Question7: What is the largest country in the world?\n",
     "Question8: What is the type of music the band Dream Theater make?\n",
     "Question9: Who is the greatest basketball player of all time?\n",
     "Questio10: Who is the tennis player known as King Of Rolland Garros?\n"
     
     
]

questions = [
     Question(question_prompts[0], "Brad Stevens"),
     Question(question_prompts[1], "Giannis Antetokounmpo"),
     Question(question_prompts[2], "Jeff Bezos"),
     Question(question_prompts[3], "Everest"),
     Question(question_prompts[4], "Bryan Cranston"),
     Question(question_prompts[5], "Mercury"),
     Question(question_prompts[6], "Russia"),
     Question(question_prompts[7], "Progressive Metal"),
     Question(question_prompts[8], "Lebron James"),
     Question(question_prompts[9], "Rafael Nadal")
     
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 10
     print("you got", score, "points out of", len(questions) * 10)
     
     if score > 50:
          print("Congratulations! You have passed the test.")
     else:
          print("You have failed the test.")




















run_quiz(questions)