from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="White")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Some Quiz",
                                                     fill=THEME_COLOR,
                                                     font=(20)
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2)
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(column= 0,row=2 )

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)
        self.window.mainloop()

def get_next_question(self):
    q_text = self.quiz.next_question()
    self.canvas.itemconfig(self.question_text, text=q_text)




