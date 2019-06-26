from tkinter import *
from tkinter import colorchooser
def coc():
    color = colorchooser.askcolor(title="Select Color")
    if color[1] is not None:
        root.configure(bg=color[1])
    print(color)
root= Tk()
root.geometry("400x400")
b=Button(root,text="Choose Color", command=coc)
b.pack()
root.mainloop()