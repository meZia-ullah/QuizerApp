from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Gui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.window.title = "quizzer"
        self.label = Label(text=f"score: {self.quiz.score}", font=("courier", 20, "normal"), fg="white", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.q_text = self.canvas.create_text(150, 125,
                                              text="ads asdf a fd",
                                              fill=THEME_COLOR,
                                              font=("arial", 18, "italic"),
                                              width=280
                                              )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        image_t = PhotoImage(file="images/true.png")
        self.tick = Button(image=image_t, command=self.check_ture, highlightthickness=0)
        self.tick.grid(column=0, row=2)

        image_f = PhotoImage(file="images/false.png")
        self.cross = Button(image=image_f, command=self.check_false, highlightthickness=0)
        self.cross.grid(column=1, row=2)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=question_text)
        else:
            self.canvas.itemconfig(self.q_text, text=f"completed {self.quiz.score}/10")
            self.tick.config(state="disabled")
            self.cross.config(state="disabled")

    def check_ture(self):
        if self.quiz.check_answer("true"):
            self.feedback("green")
        else:
            self.feedback("red")

    def check_false(self):
        if self.quiz.check_answer("false"):
            self.feedback("Green")
        else:
            self.feedback("Red")

    def feedback(self, color):
        self.label.config(text=f"score: {self.quiz.score}")
        self.canvas.config(bg=color)
        self.window.after(1000, self.next_question)
