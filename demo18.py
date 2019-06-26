from tkinter import *
def dosomething():
    l1.config(text="welcome to python")
root = Tk()
root.geometry("200x200")
l1=Label(root)
b1=Button(root, text="Click Me", command=dosomething)
b1.pack()
l1.pack()
root.mainloop()