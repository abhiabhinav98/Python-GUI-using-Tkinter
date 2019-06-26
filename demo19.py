from datetime import *
from tkinter import *
def dosomething():
    obj = datetime.now()
    x = obj.strftime("%d-%B-%Y %I:%M:%S %p")
    l1.config(text=x)
root = Tk()
root.geometry("200x200")
l1=Label(root, text="Click the button for date and time")
b1=Button(root, text="Click Me", command=dosomething)
b1.pack()
l1.pack()
root.mainloop()