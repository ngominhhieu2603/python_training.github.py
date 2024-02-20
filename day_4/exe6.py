from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Basics!")
root.iconbitmap("thinking.ico")
root.geometry("700x700")

def make_img():
    global cat_img

    cat_img = ImageTk.PhotoImage(Image.open("cat.jpg"))
    cat_label = Label(root, image= cat_img)
    cat_label.pack()

my_img = PhotoImage(file= 'shield.png')
lbl_img = Label(root, image= my_img)
lbl_img.pack()

my_button = Button(root, image= my_img)
my_button.pack()

make_img()

root.mainloop()