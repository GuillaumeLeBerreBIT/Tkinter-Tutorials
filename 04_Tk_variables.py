# Tkinter has inbuilt variables that are designed to work with widgets
# They are automatically updated by a widget and they update a widget
# Altough they still store basic data like string, integers & Booleans
# Entry -- Automatic getting -- > StringVar (Sets also value of entry) -- Automatic setting -- > Label

import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get()) # Using the get function to get the value from string_var
    string_var.set('Button pressed')    # Once the button is pressed >> Set the stringvar to that specific value

# Create window + caption + set size
window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('200x150')

# Tkinter variable
# This will contain some string >> Passed in the label >> Overwrite the text SINCE ITS START VALUE
string_var = tk.StringVar(value = 'Start value') # IntVar, BooleanVar, DoubleVar
# Using value can set the start value

# Widgets
# All these widgets will beb updated because they all share the same string
# What is in one will be in another
label = ttk.Label(master = window,
                 text = 'Some text',
                 textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window,
                  textvariable = string_var)
entry.pack()

entry_2 = ttk.Entry(master = window,
                  textvariable = string_var)
entry_2.pack()

button = ttk.Button(master = window,
                    text = 'button',
                    command = button_func)
button.pack()

# Create 2 entry fields and 1 labels, they should all be connected via a StringVar
# Set a start value of 'test'

ex_string_var = tk.StringVar(value = 'test')
#ex_string_var.set('test')

entry_ex_1 = tk.Entry(master = window,
                    textvariable = ex_string_var)
entry_ex_1.pack()

entry_ex_2 = tk.Entry(master = window,
                    textvariable = ex_string_var)
entry_ex_2.pack()

label_ex = tk.Label(master = window,
                    textvariable = ex_string_var)
label_ex.pack()

# Visualize window
window.mainloop()