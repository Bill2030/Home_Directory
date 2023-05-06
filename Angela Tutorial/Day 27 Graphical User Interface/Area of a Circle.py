from tkinter import *
import math
def area_circle():
    radius = float(radius_entry.get())
    area = int(math.pi*radius**2)
    result_meters_label.config(text=f"{area}")


window = Tk()
window.minsize(width=300, height=400)
window.config(bg="light green", padx=50, pady=50)

radius_entry = Entry()
radius_entry.grid(column=1, row=0)

radius_label = Label(text="Radius")
radius_label.grid(column=2, row=0)

is_equal_to_label = Label(text="Is Equal to")
is_equal_to_label.grid(column=0, row=1)

result_meters_label = Label(text=0)
result_meters_label.grid(column=1, row=1)

meters_label = Label(text="M")
meters_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=area_circle)
calculate_button.grid(column=1, row=2)




window.mainloop()