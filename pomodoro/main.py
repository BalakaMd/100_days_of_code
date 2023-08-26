from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    btn_start.config(state=DISABLED)
    count_down(300)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    canvas.itemconfig(canvas_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 36, "bold"))
canvas.grid(row=1, column=1)

# Create labels
activity_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
activity_label.grid(row=0, column=1)

check_mark = Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

# Create buttons
btn_start = Button(text='Start', highlightthickness=0, highlightbackground=YELLOW,
                   command=start_timer, default=ACTIVE)
btn_start.grid(row=2, column=0)

btn_reset = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW)
btn_reset.grid(row=2, column=2)

window.mainloop()
