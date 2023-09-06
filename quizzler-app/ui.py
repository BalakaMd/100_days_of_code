from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.resizable(width=False, height=False)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create a canvas
        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, font=('Arial', 20, 'italic'), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Create a buttons
        btn_false_image = PhotoImage(file='images/false.png')
        btn_true_image = PhotoImage(file='images/true.png')

        self.btn_false = Button(image=btn_false_image, highlightthickness=0,
                                command=self.false_btn_pressed)
        self.btn_false.grid(column=0, row=3)
        self.btn_true = Button(image=btn_true_image, highlightthickness=0,
                               command=self.true_btn_pressed)
        self.btn_true.grid(column=1, row=3)

        # Create a label
        self.lbl_score = Label(text='Score: 0', fg='white', background=THEME_COLOR)
        self.lbl_score.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            new_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=new_question)
            self.lbl_score.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="grey")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the questions.\n"
                                                            f"You score is {self.quiz.score}/10")
            self.btn_true.config(state=DISABLED)
            self.btn_false.config(state=DISABLED)

    def true_btn_pressed(self):
        self.get_feedback(self.quiz.check_answer('True'))

    def false_btn_pressed(self):
        self.get_feedback(self.quiz.check_answer('False'))

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="Green")
        else:
            self.canvas.config(background="Red")
        self.window.after(1000, self.get_next_question)
