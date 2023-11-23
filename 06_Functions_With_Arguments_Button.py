import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print('Button was pressed')
    print(entry_string.get())
    
def outer_func(parameter):
    def inner_func():
        print('A button was pressed')
        print(parameter.get())
    return inner_func
    
# Basic setup
window = tk.Tk()
window.title('Button, functions and arguments')

# Widgets 
entry_string = tk.StringVar(value = 'test')
entry = ttk.Entry(master = window, textvariable = entry_string)
entry.pack()
# The lambda function will tell python to only execute the code when pressing the button >> By default lmabda not called >> What happens now lmabda called when rpessing
# >> Then the button function called and that is what the command sees
#button = ttk.Button(master = window, text = 'A button', command = lambda: button_func(entry_string))
# OR
# Now when python executes that function >> Inside function another one that prints simple string and the parameter value
# IMPORTANT >> return inner_func because that is what is being returned through the command argument
button = ttk.Button(master = window, text = 'A button', command = outer_func(entry_string))
button.pack()
 
# Run
window.mainloop()