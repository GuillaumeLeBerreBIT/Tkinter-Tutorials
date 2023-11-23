# Need to improt tkinter
import tkinter as tk 
from tkinter import ttk

def button_func():
    print('Something printed')
    
def button_func_ex():
    print('Hello')

# Create a window, what we can place everything on
window = tk.Tk()

# Set the window title
window.title('Window and widgets')
# Here can set the width and the height of the window
# This will be 800 p WIDE x 500 p HEIGHT
window.geometry('800x500')

# ttk widgets
label = ttk.Label(master = window,
                  text = 'This is a test')  # This widget will place a label in middle of master 'window' under text.pack()
label.pack()    #IF PLACED ABOVE IT WILL COME BEFORE TEXT

# Craete a tK widget - Always have to tell what the master is >> Parent where you want to place it and for now want to place it on the window
text = tk.Text(master = window) 
text.pack() # This will create a textbox == PACK WILL PLACE WIDGET IN MIDDLE OF THE TOP ON THE WINDOW/MASTER

# ttk entry widget 
entry = ttk.Entry(master = window) 
entry.pack()

# ttk button
# Everytime pressing the buttom >> Will use the functionn to do something or make something happen. 
button = ttk.Button(master = window,
                    text = 'A button',
                    command = button_func)
button.pack()

# Add one more text label and a button with a function that prints hello
# The label should say "my label" and be between the entry widget and the button

entry = ttk.Entry(master = window) 
entry.pack()

my_label = ttk.Label(master = window,
                     text = 'My label')
my_label.pack()

ex_button = ttk.Button(master = window,
                    text = 'Exercise',
                    command = lambda: print('hello'))
ex_button.pack()

# Run
# This will update the GUI >> See it in results
# This will also checks for events
window.mainloop()   
