import html
from tkinter import messagebox
from os import  system
from time import sleep
import sys
import os
class QuizBrain:

    def __init__(self, q_list, ):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        try:
            self.current_question = self.question_list[self.question_number]
        except:
            messagebox.showinfo(title="Score", message=f"Your score is: {self.score} / 10 ")
            answer = messagebox.askokcancel(title="askokcancel", message="Want to try again?")
            if answer == True:
                print("true")
                self.restart()
                
            else:
                quit()

        self.question_number += 1
        quest_unescape = html.unescape(self.current_question.text)
        if self.question_number <= 10:
            return f"Q.{self.question_number}: {quest_unescape}"
       
        


    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if str(user_answer) == correct_answer:
            self.score += 1

            return True
            # print("You got it right!")
        else:
            # print("That's wrong.")
            return False

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")


    def restart(self):
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restart now")
        
        os.execv(sys.executable, ['python'] + sys.argv)
     
