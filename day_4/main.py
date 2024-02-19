# Window Basics
from tkinter import *

# Define Window
root = Tk()
root.title("Window Basics!")
root.iconbitmap("thinking.ico")
root.geometry("250x700")
root.resizable(0,0)
root.config(bg= "blue")

# Second Window
top = Toplevel()
top.title("Second Window")
top.config(bg= '#123456')
top.geometry("200x200+500+50")

# Run root Window's mainloop
root.mainloop()