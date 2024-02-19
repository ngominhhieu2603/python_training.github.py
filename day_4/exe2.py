# Buttons and grid
from tkinter import *

root = Tk()
root.title("Button Basic!")
root.iconbitmap("thinking.ico")
root.geometry("500x500")
root.resizable(0, 0)

name_Button = Button(root, text= "Name")
name_Button.grid(row= 0, column= 0)

time_Button = Button(root, text= "Time", bg= '#0ff')
time_Button.grid(row= 0, column= 1)

place_Button = Button(root, text= "Place", bg= '#0ff', activebackground= "#f00")
place_Button.grid(row= 0, column= 2, padx= 10, pady= 10, ipadx= 15)

day_Button = Button(root, text= "Day", bg= 'black', fg= 'white', borderwidth= 5)
day_Button.grid(row= 1, column= 0, columnspan= 3, sticky= 'We')

test1 = Button(root, text="Test 1")
test2 = Button(root, text="Test 2")
test3 = Button(root, text="Test 3")
test4 = Button(root, text="Test 4")
test5 = Button(root, text="Test 5")
test6 = Button(root, text="Test 6")

test1.grid(row=2, column=0, padx=5, pady=5)
test2.grid(row=2, column=1, padx=5, pady=5)
test3.grid(row=2, column=2, padx=5, pady=5, sticky="W")
test4.grid(row=3, column=0, padx=5, pady=5)
test5.grid(row=3, column=1, padx=5, pady=5)
test6.grid(row=3, column=2, padx=5, pady=5, sticky="W")

root.mainloop()