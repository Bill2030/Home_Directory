import json
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols)  for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_web.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data ={
        website:{
        "email":email,
        "password": password

        }
    }

    if (website)== 0 or len(password)== 0:
        messagebox.showinfo(title="oops", message="Dont leave any of the fields empty")
    else:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)

        with open("data.json", "w") as data_file:
            #saving the updated data
            json.dump(data, data_file, indent=4)
            entry_web.delete(0, END)
            entry_password.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

window.config(width=400, height=400)
window.config(padx=50, height=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)
label_web = Label(text="Website")
label_web.grid(column=0, row=1)

entry_web = Entry(width=35)
entry_web.grid(column=1, row=1, columnspan=3)
entry_web.focus()

label_email = Label(text="Email/Username")
label_email.grid(column=0, row=2)

entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "benardbill@gmail.com")

label_password= Label(text="Password")
label_password.grid(column=0, row=3)

entry_password = Entry(width=35)
entry_password.grid(column=1, row=3, columnspan=2)


button = Button(text="Generate Password", command=generate_password)
button.grid(column=2, row=3)

button_add = Button(text="Add", width=30, command=save)
button_add.grid(column=1, row=4, columnspan=2)


window.mainloop()