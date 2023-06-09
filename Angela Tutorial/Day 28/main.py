import math
from tkinter import *
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
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count -1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Application")
window.minsize(width=400, height=200)
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image= tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=4, row=2)
label = Label(text="Timer",font=(FONT_NAME, 35,), fg=GREEN)
label.grid(column=4, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=3, row=4)
start_button.config(width=15)

label_tick = Label(text="✔", fg=GREEN)
label_tick.grid(column=4, row=4)

reset_button = Button(text="Reset")
reset_button.grid(column=5, row=4)
reset_button.config(width=15)




window.mainloop()