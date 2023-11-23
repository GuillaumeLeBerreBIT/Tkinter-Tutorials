import tkinter as tk
from tkinter import ttk
# https://www.pythontutorial.net/tkinter/tkinter-event-binding/

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')


# Basic setup
window = tk.Tk()
window.title('Button, functions and arguments')

text = tk.Text(master = window)
text.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'A button')
button.pack()
 
# Events
# Need to give one argument e.g. event here >> When pressing Alt-a we get the 'An event' printed out
# Need <modifier-type-detail> sometimes, can also check only KeyPress + Function
#button.bind('<Alt-KeyPress-a>', lambda event: print('An event'))
#window.bind('<KeyPress>', lambda event: print(f'A button was pressed {event.char}'))

#window.bind('<Motion>', get_pos)    # Can get the mouse position wherever you are on the window
#text.bind('<Motion>', get_pos)  # Depending what widget then only works it >> TKINTER ONLY CHECKS THE EVENT ON THE WIDGET IT IS SELECTED

# Want to check the entry widget >> When selecting the widget it perform the function OR deselecting perform the other one 
entry.bind('<FocusIn>', lambda event: print('Entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('Entry field was deselected'))

# Exercise
# Print 'Mousewheel' when the user holds down shift and uses the mousewheel while text is selected
text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))

# Run
window.mainloop()