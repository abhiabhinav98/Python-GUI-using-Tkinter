import tkinter
import tkinter.font
tw=tkinter.Tk()
tw.title("My GUI App 2")
img = tkinter.PhotoImage(file="C:/Users/HP/Desktop/images/loginlogo1.png")
tw.iconphoto(tw,img)
s=tkinter.StringVar()
tw.geometry("600x200")
tw.resizable(False,False)
lbl=tkinter.Label(tw, textvariable=s)
lbl.pack()
s.set("welcome")
tw.mainloop()