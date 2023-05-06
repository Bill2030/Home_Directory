from tkinter import *

root = Tk()
label1 = Label(root, text="This is tutorial about Tkinter", width=30)
label1.pack(side=TOP, expand=True)
label2 = Label(root, text="Do you wish to learn?", fg="Blue",width=30)
label2.pack(side=TOP, expand=True)
button1 = Button(root, text="Accept", fg="Green", command=root.destroy)
button1.pack(side=LEFT, expand=True)
button2 = Button(root, text="Close", fg="Blue", command=root.destroy)
button2.pack(side=RIGHT, expand=True)
root.mainloop()
