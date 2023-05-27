from tkinter import *
import requests

My_URL = "https://v2.jokeapi.dev/joke/Any?amount=4"

def press():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?type=Single&amount=1")
    response.raise_for_status()
    data = response.json()
    output = data["joke"]
    canvas.itemconfig(some_text, text= output)


window = Tk()
window.config(width=300, height=300)
window.config(padx=20, pady=20)


canvas = Canvas(width=300, height=300, bg="green")
canvas.grid(column=0, row=0)
some_text = canvas.create_text(150, 207, text="Some Text", width=250, font=("Arial", 14, "bold"), fill="white")
canvas.grid(row=0, column=0)
press_button = Button(text="Press the Button for meme", width=25, command=press)
press_button.grid(column=0, row=1)
window.mainloop()