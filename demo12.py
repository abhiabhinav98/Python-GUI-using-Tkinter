import tkinter
import tkinter.font
tw=tkinter.Tk()
lbl1=tkinter.Label(tw, text="Red Sun", bg="red", fg="white" )
lbl1.pack(fill=tkinter.X, padx=(5,0),pady=5)
lbl2=tkinter.Label(tw, text="Blue Moon", bg="blue", fg="white" )
lbl2.pack(fill=tkinter.X, padx=5,ipadx=50)
tw.mainloop()