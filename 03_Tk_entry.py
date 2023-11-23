import tkinter as tk
from tkinter import ttk 

# Every widget has a config method  
# Inside label can use "config" to update the text
def button_func():
    # Get the content of the Entry >> Get method
    entry_text = entry.get()  # Saving the content in a variable can do things with it

    # Update the label >> Once pressed will set this as text on the label
    #label.configure(text = 'Some other text')  
    label['text'] = entry_text     # Same purpose 
    entry['state'] = 'disabled'     # This will disable the button after pressing once
    # print(label.configure()) # Will return all of the options can work with
    
def restore_func():
    # Change the text back
    label['text'] = 'Some text'
    # Enables the button >> WAnt to call previous button
    entry['stat'] = 'normal'   
    
# Creating the basic window
window = tk.Tk()
# Title of the window
window.title('Getting and setting widgets')
# Size of visual window
window.geometry('200x150') 


# Widgets
label = tk.Label(master = window,
                 text = 'Some text')
label.pack()

entry = tk.Entry(master = window)
entry.pack()

button = tk.Button(master = window,
                  text = 'Button',
                  command = button_func)
button.pack()

# Exercise
# Add another button that changes text back to 'some text' and that enables entry

restore_button = tk.Button(master = window,
                           text = 'Enable button',
                           command = restore_func)
restore_button.pack()

# To run the window
window.mainloop()