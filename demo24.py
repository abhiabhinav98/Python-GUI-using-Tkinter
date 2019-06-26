from tkinter import *
def changeclr(e):
    root.configure(bg="red")
root = Tk()
root.geometry("200x200")
b1=Button(root,text="click me")
b1.bind("<Button>",changeclr)
b1.pack()
root.mainloop()