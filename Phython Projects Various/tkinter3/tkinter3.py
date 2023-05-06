import tkinter as tk

res = tk.Tk()  # This is the container window
res.title('Incrementing the Process')
button = tk.Button(res, text='Pause', width=40, height=10, command=res.destroy)
button.pack()
res.mainloop()  # This executes the application unless stopped