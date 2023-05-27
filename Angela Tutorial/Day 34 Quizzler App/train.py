from tkinter import *

window = Tk()
window.title("Train")
window.config(width=400, height=400)
window.config(padx=40, pady=40)

false_image = PhotoImage(file="images/false.png")

canvas = Canvas()
canvas.create_image(image=false_image)




window.mainloop()