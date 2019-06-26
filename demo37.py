from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
def accept():
    num = simpledialog.askinteger("Input","Enter voters age", minvalue=18,maxvalue=100)
    if num is not None:
        messagebox.showinfo("Hello","You entered "+str(num))
root= Tk()
root.geometry("200x200")
btn=Button(root,text="Click me",command=accept)
btn.pack()
root.mainloop()