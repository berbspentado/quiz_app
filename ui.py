from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.var = StringVar()
        self.window.title("Quiz")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        
        self.score = Label(textvariable=self.var, font=("Arial",13),background=THEME_COLOR,fg='#fff')
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0,bg="white")
        self.question = self.canvas.create_text(150,110,text="Random questions.", fill="black", font=("Arial", 15, "italic"),width=300)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        right_bt = PhotoImage(file="images/true.png")
        self.button_right = Button(image=right_bt, highlightthickness=0,command=self.is_true)
        self.button_right.grid(column=0,row=2,)

        wrong_bt = PhotoImage(file="images/false.png",)
        self.button_wrong = Button(image=wrong_bt, highlightthickness=0, command= self.is_false)
        self.button_wrong.grid(column=1,row=2,)


        self.var.set(f"Score: {self.quiz.score}")
        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
       q_text =  self.quiz.next_question()
       self.canvas.itemconfig(self.question, text=q_text)

    def is_true(self):

        # self.quiz.check_answer(True)
        self.change_color()
#    
        # self.canvas.config(bg="green")
        # self.canvas.after(10000,lambda: self.config(bg="white"))
        self.var.set(f"Score: {self.quiz.score}")
        self.get_next_question()
    
        return 
    

    def is_false(self):
        # self.quiz.check_answer(False)
        self.change_color()
        self.var.set(f"Score: {self.quiz.score}")
        # self.canvas.config(bg="red")
        self.get_next_question()
        return False
    
    def change_color(self):
        if self.quiz.check_answer(True) == True:
            self.canvas.config(bg="green")
            self.canvas.after(500,lambda: self.canvas.config(bg="white"))
        else:
            self.canvas.config(bg="red")
            self.canvas.after(500,lambda: self.canvas.config(bg="white"))

  