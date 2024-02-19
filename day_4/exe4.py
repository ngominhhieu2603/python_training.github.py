from tkinter import *

root = Tk()
root.title("Entry Basics")
root.iconbitmap('thinking.ico')
root.resizable(0, 0)
root.geometry("500x500")

def make_label():
    text = Label(out_frame, text= text_entry.get(), bg= '#f00')
    text.pack()
    text_entry.delete(0, END)

def count_up(number):
    text = Label(out_frame, text= number, bg= 'red')
    text.pack()
    value = number + 1

input_frame = Frame(root, bg= '#00f', width= 500, height= 100)
input_frame.pack(padx= 10, pady= 10)

out_frame = Frame(root, bg= '#f00', width= 500, height= 400)
out_frame.pack(padx= 10, pady= (0, 10))

text_entry = Entry(input_frame, width= 40)
text_entry.grid(row= 0, column= 0, padx= 5, pady= 5)
input_frame.grid_propagate(False)

print_button = Button(input_frame, text= 'Print', command= make_label)
print_button.grid(row= 0, column= 1, padx= 5, pady= 5, ipadx= 30)
out_frame.grid_propagate(False)

value = True
count_button = Button(input_frame, text= "Count", command= lambda: count_up(value))
count_button.grid(row = 1, column= 0, columnspan= 2, padx= 5, pady= 5, sticky= 'WE' )

root.mainloop()