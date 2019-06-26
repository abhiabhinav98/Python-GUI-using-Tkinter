from tkinter import *
from tkinter import messagebox
def showgender():
    if x.get()==1:
        messagebox.showinfo("x", "You selected Male" )
    elif x.get() == 2:
        messagebox.showinfo("x", "You selected Female")
root = Tk()
root.geometry("200x200")
x = IntVar()
l=Label(root,text="Select Your Gender")
rb1= Radiobutton(root, text="Male", command=showgender, variable=x, value=1)
rb2= Radiobutton(root, text="Female", command=showgender, variable=x, value=2)
l.pack()
rb1.pack()
rb2.pack()
root.mainloop()