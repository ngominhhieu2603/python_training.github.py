import tkinter as tk
from tkinter import ttk

# Define Window
root = tk.Tk()
root.title("Metric Helper")
root.iconbitmap("ruler.ico")
root.resizable(False, False)

# Define Font, Color
field_font = ("Cambria", 10)
bg_color = '#c75c5c'
button_color = '#f5cf87'

# Define Function
def convert():
    """Convert from one metric prefix to another"""
    metric_values = {
                "femto": 10**-15,
        "pico": 10**-12,
        "nano": 10**-9,
        "micro": 10**-6,
        "milli": 10**-3,
        "centi": 10**-2,
        "deci": 10**-1,
        "base value": 10**0,
        "deca": 10**1,
        "hecto": 10**2,
        "kilo": 10**3,
        "mega": 10**6,
        "giga": 10**9,
        "tera": 10**12,
        "peta": 10**15
    }

    # Clear output_field
    output_field.delete(0, tk.END)

    # Get all user information
    start_value = float(input_field.get())
    start_prefix = input_combobox.get()
    end_prefix = output_combobox.get()

    # Convert to the base unit first
    base_value = start_value * metric_values[start_prefix]
    
    end_value = base_value / metric_values[end_prefix]

    # Update output field
    output_field.insert(0, str(end_value))

# Define layout
# Create input, output entry field
input_field = tk.Entry(root, width= 20, font= field_font, bg= bg_color, borderwidth= 3)
output_field = tk.Entry(root, width= 20, font= field_font, bg= bg_color, borderwidth= 3)
equal_label = tk.Label(root, text= '=', font= field_font, bg= bg_color)

input_field.grid(row= 0, column= 0, padx= 10, pady= 10)
output_field.grid(row= 0, column= 2, padx= 10, pady= 10)
equal_label.grid(row= 0, column= 1, padx= 10, pady= 10)

input_field.insert(0, "Enter your quantity")

# Create Dropdown for metric values
metric_list = [
        "femto", "pico", "nano", "micro", "milli", "centi", "deci", "base value",
        "deca", "hecto", "kilo", "mega", "giga", "tera", "peta"
]

input_combobox = ttk.Combobox(root,
                              values= metric_list,
                              font= field_font,
                              justify= tk.CENTER)
output_combobox = ttk.Combobox(root,
                               values= metric_list,
                               font= field_font,
                               justify= tk.CENTER)
to_label = tk.Label(root, text= 'to', font= field_font, bg= bg_color)

input_combobox.grid(row= 1, column= 0, padx= 10, pady= 10)
output_combobox.grid(row= 1, column= 2, padx= 10, pady= 10)
to_label.grid(row= 1, column= 1, padx= 10, pady= 10)

input_combobox.set('base value')
output_combobox.set('base value')

# Create convert button
convert_button = tk.Button(root,
                           text= "Convert",
                           font= field_font,
                           bg= bg_color,
                           command= convert)
convert_button.grid(row= 2, column= 0, columnspan= 3, padx= 10, pady= 10, ipadx= 50)

# Run Window's main loop
root.mainloop()