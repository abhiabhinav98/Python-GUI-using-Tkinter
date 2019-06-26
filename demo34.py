from tkinter import *
from tkinter import messagebox
def finish():
    ans = messagebox.askyesno("Question","Do you want to cancel?")
    if ans == True:
        sys.exit()
def divide():
    try:
        e3.config(fg="red")
        x=int(e1.get())
        y=int(e2.get())
        c=x/y
        e3.insert(0, str(c))
        e3.config(fg="green")
    except ZeroDivisionError:
        messagebox.showerror("Error","Denominator zero not allowed")
    except ValueError:
        messagebox.showerror("Error", "Only Integers allowed")
def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e1.focus()
root = Tk()
s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
l1 = Label(root, text="First Number")
l2 = Label(root, text="Last Number")
l3 = Label(root, text="Result")
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
b1 = Button(root, text="Divide", command=divide)
b2 = Button(root, text="Clear", command=clear)
b3 = Button(root, text="Quit", command=finish)
l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
l2.grid(row=1, column=0)
e2.grid(row=1, column=1)
l3.grid(row=2, column=0)
e3.grid(row=2, column=1, columnspan=2)
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
root.mainloop()