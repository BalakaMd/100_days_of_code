import math
from tkinter import *
import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, './tomato.png')

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark_count = ""
timer = ...


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global mark_count
    global reps
    window.after_cancel(timer)
    btn_start.config(default=ACTIVE, state=ACTIVE, )
    canvas.itemconfig(canvas_text, text="00:00")
    activity_label.config(text="Timer")
    mark_count = ""
    check_mark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    btn_start.config(state=DISABLED)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        activity_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        activity_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        activity_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"
    canvas.itemconfig(canvas_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()
        window.focus_force()
        if reps % 2 == 0:
            global mark_count
            mark_count += "✔"
            check_mark.config(text=mark_count)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=90, pady=50, bg=YELLOW)
window.resizable(width=False, height=False)
x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 3
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 3
window.wm_geometry("+%d+%d" % (x, y))

# Create a canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file=file_path)
canvas.create_image(100, 112, image=tomato_image)
canvas_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 36, "bold"))
canvas.grid(row=1, column=1)

# Create labels
activity_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
activity_label.grid(row=0, column=1)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

# Create buttons
btn_start = Button(text='Start', highlightthickness=0, highlightbackground=YELLOW,
                   command=start_timer, default=ACTIVE)
btn_start.grid(row=2, column=0)

btn_reset = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW,
                   command=reset_timer)
btn_reset.grid(row=2, column=2)

window.mainloop()
