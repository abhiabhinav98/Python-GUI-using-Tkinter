from tkinter import *
def changeclr(e):
    x=e.char
    if x=="r":
        root.configure(bg="red")
    elif x=="g":
        root.configure(bg="green")
    elif x=="b":
        root.configure(bg="blue")

root = Tk()
root.geometry("200x200")
root.bind("<Key>", changeclr)
root.mainloop()