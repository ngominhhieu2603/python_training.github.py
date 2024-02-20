from tkinter import *
from tkinter import messagebox

USER_NAME =  'hieuts123'
PASSWORD = '26032000'

def Notice():
    if text_username.get() == USER_NAME and text_password.get() == PASSWORD:
        messagebox.showinfo("Sign in access!")
    else:
        messagebox.showerror("Error")

root = Tk()
root.title("InFO Acount")
root.iconbitmap("thinking.ico")
root.geometry("500x500")
root.resizable(False, False)

lbl_username = Label(root, text= 'User Name', fg= 'blue', font= ('arial', 15))
lbl_username.grid(row= 0, column= 0, padx= 5, pady= 5)

text_username = Entry(root, width= 30)
text_username.grid(row= 0, column= 1, padx= 5, pady= 5)

lbl_password = Label(root, text= 'Pass Word', fg= 'blue', font= ('arial', 15))
lbl_password.grid(row= 1, column= 0, padx= 5, pady= (5, 0))

text_password = Entry(root, width= 30, show= '*')
text_password.grid(row= 1, column= 1, padx= 5, pady= 5)

button_signin = Button(root, text= 'Sign in', command= Notice)
button_signin.grid(row= 2, column= 0)

root.mainloop()