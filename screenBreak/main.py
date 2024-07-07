from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
BLUE = "#2C4E80"
GREEN = "#00F400"
YELLOW = "#FFE0B5"
RED = "FF0000"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timmer():
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text = "00:00")
    title_lable.config(text="Timer")
    checkMarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short_break_sec)
        title_lable.config(text="Break", fg=PINK)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        title_lable.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        title_lable.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timerText, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔️"
        checkMarks.config(text = mark) 


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Screen Break")
window.config(padx=100, pady= 100, bg=YELLOW)

title_lable = Label(text="TIMER", fg=BLUE, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_lable.grid(column=1, row=0)

canvas = Canvas(width=240, height=305, highlightthickness=0, bg=YELLOW)
clockImg = PhotoImage(file="red-apple.png")
canvas.create_image(119, 153, image=clockImg)
timerText = canvas.create_text(115, 200, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


startButton = Button(text="START", font=(FONT_NAME, 25, "bold"), command=start_timer)
resetButton = Button(text="RESET", font=(FONT_NAME, 25, "bold"), command=reset_timmer)
startButton.grid(column=0, row=2)
resetButton.grid(column=2, row=2)

checkMarks = Label(fg=GREEN, bg=YELLOW)
checkMarks.grid(column=1, row=3)


window.mainloop()