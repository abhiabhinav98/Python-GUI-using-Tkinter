from tkinter import *
root = Tk()
x=root["bg"]
root.geometry("200x200")
root.bind("<Return>", lambda e : root.config(bg="red"))
root.bind("<Escape>", lambda e : root.config(bg=x))
root.mainloop()