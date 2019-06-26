import tkinter
from tkinter import *
def dosomething():
    print("Welcome")

root = tkinter.Tk()
root.geometry("200x200")
b1=tkinter.Button(root, text="Click Me", command=dosomething)
b1.pack()
root.mainloop()