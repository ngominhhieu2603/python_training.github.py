import tkinter as tk
import time

root = tk.Tk()
root.title("digital clock")
root.iconbitmap("digital_clock.ico")
root.geometry("300x150")
root.resizable(False, False)
root.config(bg= 'black')

def update_label():
    week = int(time.strftime("%w"))

    cur_time = f"thu {week}\n" + time.strftime("%I: %M: %S %p\n%d-%m-%Y")
    clock_label.config(text= cur_time)

    clock_label.after(1000, update_label)

clock_label = tk.Label(root, font= ('arial', 18), bg= 'black', fg= 'cyan')
clock_label.pack(pady= 15)


update_label()
root.mainloop()