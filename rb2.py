from tkinter import *
from tkinter import messagebox
def showgender():
    messagebox.showinfo("Gender","You selected: "+x.get())
root = Tk()
root.geometry("200x200")
x = StringVar()
l=Label(root,text="Select Your Gender")
rb1= Radiobutton(root, text="Male", command=showgender, variable=x, value="Male", tristatevalue="x")
rb2= Radiobutton(root, text="Female", command=showgender, variable=x, value="Female", tristatevalue="x")
l.pack()
rb1.pack()
rb2.pack()
root.mainloop()