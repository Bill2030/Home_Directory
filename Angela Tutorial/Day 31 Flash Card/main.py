from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card
    current_card = random.choice(to_learn)
    print()
    canvas.itemconfig(card_title, text= "French")
    canvas.itemconfig(card_word, text=current_card["French"])
    window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(card_title, text= "English")
    canvas.itemconfig(card_word, text=current_card["English"])


window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0,columnspan=2)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 26, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 45, "bold"))


unknown_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_image,highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image,highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)

next_card()



window.mainloop()

