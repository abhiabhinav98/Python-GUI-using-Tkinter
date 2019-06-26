import tkinter
import tkinter.font
tw=tkinter.Tk()
tw.title("My GUI App 2")
img = tkinter.PhotoImage(file="C:/Users/HP/Desktop/images/loginlogo1.png")
sw=tw.winfo_screenwidth()
sh=tw.winfo_screenheight()
xc=sw//4
yc=sh//4
rw=sw//2
rh=sh//2
tw.geometry(f"{rw}x{rh}+{xc}+{yc}")
tw.resizable(False,False)
lbl=tkinter.Label(tw,image=img, text="Welcome",compound=tkinter.RIGHT)
lbl.pack()
tw.mainloop()