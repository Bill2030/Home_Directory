from tkinter import *
import math

def converter():
    usd_cad = label_amount.get()
    

window = Tk()
window.minsize(width=300, height=400)
window.config(pady=30, padx=30)

label = Label(text="Currency Converter", font=(18))
label.grid(column=3, row=1)
label_amount = Label(text="Enter Amount")
label_amount.grid(column=2, row=2)
input_amount = Entry(width=30)
input_amount.grid(column=3, row=3)
label_from = Label(text="From")
label_from.grid(column=2, row=4)
button = Button(text="USD")
button.grid(column=2, row=5)
label_to = Label(text="To")
label_to.grid(column=4, row=4)
button_cad= Button(text="CAD")
button_cad.grid(column=4, row=5)
label_display = Label(text=0)
label_display.grid(column=2, row=6)
button_convert = Button(text="Convert")
button_convert.grid(column=3, row=7)




window.mainloop()