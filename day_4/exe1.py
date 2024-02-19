# Label and pack
from tkinter import *

# Define Window
root = Tk()
root.title("Label Basic!")
root.geometry("400x400")
root.iconbitmap("thinking.ico")
root.resizable(0, 0)
root.config(bg= 'blue')

# Create Widgets
name_label_1 = Label(root, text= "Hello, my name is Mike.")
name_label_1.pack()

name_label_2 = Label(root, text= "Hello, my name is John.", font= ('arial', 18, 'bold'))
name_label_2.pack()

name_label_3 = Label(root)
name_label_3.config(text= "Hello, my name is Paul")
name_label_3.config(font= ("Segoe UI", 10))
name_label_3.config(bg= '#f00')
name_label_3.pack(padx= 10, pady= 50)

name_label_4 = Label(root, text= "Hello, my name is Sue", bg= '#000', fg= 'green')
name_label_4.pack(pady= (0,10), ipadx= 50, ipady= 10, anchor= 'w')

name_label_5 = Label(root, text= "Hello, my name is Pat.", bg= '#fff', fg= '#123456')
name_label_5.pack(fill= BOTH, expand= True, padx= 10, pady= 10)

root.mainloop()