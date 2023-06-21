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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_set, text="00:00")
    title_label.config(text="Timer", fg=RED)
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_brake_sec = SHORT_BREAK_MIN * 60
    long_brake_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_brake_sec)
        title_label.config(text="Long brake", fg=RED)
    elif reps % 2 == 0:
        count_down(short_brake_sec)
        title_label.config(text="Short brake", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    global timer
    minute = (count//60)
    sec = count%60
    if sec < 10:
        time_str = f"{minute}:0{sec}"
    else:
        time_str = f"{minute}:{sec}"

    canvas.itemconfig(timer_set, text=time_str)
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)


# label
title_label = Label(text='Timer', font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

# tomato
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=tomato_img)
timer_set = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)


# button Start
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# button Reset
reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(column=2, row=2)

# check marks
check_marks = Label(font=(FONT_NAME, 18, "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)




window.mainloop()
