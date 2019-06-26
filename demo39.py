from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
def accept():
    file_name = filedialog.askopenfilename(filetypes=[("mp3 files","*.mp3")],title="Select your favourite song")
    if len(file_name) !=0:
        messagebox.showinfo("Hello", "You selected " + file_name)
root= Tk()
root.geometry("200x200")
btn=Button(root,text="Open File",command=accept)
btn.pack()
root.mainloop()