from tkinter import *

root = Tk()
root.title("Radio Button Basic")
root.iconbitmap("thinking.ico")
root.geometry("350x350")
root.resizable(0, 0)

def make_label():
    if number.get() == 1:
        text = Label(output_frame, text= '1 one 1')
    elif number.get() == 2:
        text = Label(output_frame, text= '2 two 2')
    text.pack()

input_frame = LabelFrame(root, text= 'This is fun', width= 350, height= 100)
output_frame = Frame(root, width= 350, height= 250)

input_frame.pack(padx= 10, pady= 10)
output_frame.pack(padx= 10, pady= (0, 10))

number = IntVar()
number.set(2)
radio_button1 = Radiobutton(input_frame, text= 'Print the number one', variable= number, value= 1)
radio_button2 = Radiobutton(input_frame, text= 'Print the number two', variable= number, value= 2)
print_button = Button(input_frame, text= 'Print the number!', command= make_label)

radio_button1.grid(row= 0, column= 0, padx= 10, pady= 10)
radio_button2.grid(row= 0, column= 1, padx= 10, pady= 10)
print_button.grid(row= 2, column= 0, columnspan= 2, padx= 10, pady= 10)

root.mainloop()