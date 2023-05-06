from tkinter import *

def miles_km():
    miles = float(miles_entry.get())
    km = round(miles * 1.609)
    Kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to KM Project")
window.config(padx=30, pady=30)
window.minsize(width=300, height=400)

miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)


is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

Kilometer_result_label = Label(text=0)
Kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="calculate", command=miles_km)
calculate_button.grid(column=1, row=2)








window.mainloop()