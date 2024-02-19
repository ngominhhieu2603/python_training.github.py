# Frames
from tkinter import *

root = Tk()
root.title("Frames Basics")
root.geometry("500x500")
root.iconbitmap("thinking.ico")

# Example of why to use frames ?
""" name_label = Label(root, text= "Enter your name")
name_label.pack()

name_button = Button(root, text= "Submit your name)
name_button.grid(row= 0, column= 1)
"""

# Define frames
pack_frame = Frame(root, bg= 'red')
grid_frame1 = Frame(root, bg= 'blue')
grid_frame2 = LabelFrame(root, text= "Grid System Rules!", borderwidth= 5)

# Pack frames onto root
pack_frame.pack(fill= BOTH, expand= True)
grid_frame1.pack(fill= 'x', expand= True)
grid_frame2.pack(fill= BOTH, expand= True, padx= 10, pady= 10)

# Pack frames 
Label(pack_frame, text= 'test').pack()
Label(pack_frame, text= 'test').pack()
Label(pack_frame, text= 'test').pack()

# Grid on layout
Label(grid_frame1, text= 'test').grid(row= 0, column=0)
Label(grid_frame1, text= 'test').grid(row= 1, column=1)
Label(grid_frame1, text= 'test').grid(row= 2, column=2)

Label(grid_frame1, text= 'aaaaaaaaaaaaaaaaa').grid(row= 3, column= 0)

# Grid 2 layout
Label(grid_frame2, text= 'aaaaaaaaaaaaaaa').grid(row= 0, column= 0)

root.mainloop()