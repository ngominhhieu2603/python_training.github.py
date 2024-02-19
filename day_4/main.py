# Window Basics
from tkinter import *

roof = Tk()
roof.title("Window Basics!")
roof.iconbitmap("thinking.ico")
roof.geometry("250x700")
roof.resizable(0, 0)
roof.config(bg= 'blue')

# second Window
top = Toplevel()
top.title("Second Windows")
top.geometry("400x250+400+300")
top.config(bg= '#123456')

roof.mainloop()
