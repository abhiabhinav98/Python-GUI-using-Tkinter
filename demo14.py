import tkinter
root = tkinter.Tk()
root.geometry("600x600")
l1=tkinter.Label(root, text="Label 1", bg ="red", fg="white")
l2=tkinter.Label(root, text="Label 2", bg ="green", fg="white")
l1.place(x=0,y=0)
l2.place(x=100,y=50)
root.mainloop()