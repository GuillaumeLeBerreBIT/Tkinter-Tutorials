import tkinter as tk
from tkinter import ttk

# Setup
window = tk.Tk()
window.geometry('600x400')
window.title('Combo and Spin')


# Combobox
# Create a tuple lsit with all items to get in dropdown box
items = ('Ice cream', 'Pizza', 'Broccoli')
# Can also use a StringVar to set a starting value as well
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(master = window,
                     textvariable = food_string)
# Parse the list to be visible when using dropdown box
combo['values'] = items
#combo.configure(values = items) 
combo.pack()

# Events >> Everytime when selecting an item in combobox will print out whatever value is selected 
# Now whatever is selected from dropdownbox >> It will set/configure it as a new value for the label text
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text = f'Selected value: {food_string.get()}'))  # print(food_string.get())

combo_label = ttk.Label(window, text = 'A label')
combo_label.pack()

# Spinbox
spin_int = tk.IntVar(value = 12)
# Using the from_ and to can select a huge range of numbers want to have & can add an increment which are the steps to go over numbers
spin = ttk.Spinbox(window, 
                   from_ = 3, 
                   to = 20, 
                   increment = 3,
                   textvariable = spin_int, 
                   command = lambda: print(spin_int.get()))

# It has some special events as well such as when pressing either the arrow up or down
spin.bind('<<Increment>>', lambda event: print('Up'))
spin.bind('<<Decrement>>', lambda event: print('Down'))
#spin['value'] = (1,2,3,4,5)
spin.pack()

# Exercise
# Create a spinbox that contains the letters A B C D E 
# And print the value whenever the value is decreased
ex_letters = ('A','B','C','D','E')
spin_str = tk.StringVar(value = ex_letters[0])
spin_ex = ttk.Spinbox(master = window,
                      textvariable = spin_str)
spin_ex['value'] = ex_letters
spin_ex.bind('<<Decrement>>', lambda event: print(spin_str.get()))
spin_ex.pack()

# Run 
window.mainloop() 