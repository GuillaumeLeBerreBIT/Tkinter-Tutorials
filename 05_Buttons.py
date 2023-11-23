import tkinter as tk
from tkinter import ttk

# Setup
window = tk.Tk()
window.title('Tkinter Buttons')
window.geometry('600x400')

# Button 
def button_func():
    print('a basic button')
    print(radio_var.get())

# Normal button
button_string = tk.StringVar(value = 'A button with StringVar') # This overwrites the text variable
button = ttk.Button(master = window,
                    text = 'A simple button',
                    command = button_func,
                    textvariable = button_string)
button.pack()

# Check button
# TO store and check the value of check need tkinter var
check_var = tk.IntVar()
check_1 = ttk.Checkbutton(window,
                        text = 'Checkbox 1',
                        command = lambda: print(check_var.get()),
                        variable = check_var,   # Has no textvariable option due to variable will jsut store the value whether the box is ticked or not -- > 1 == Ticked & 0 == Empty 
                        onvalue = 10,     # Value returned when the box is ticked on
                        offvalue = 5)       # Value returned when the button os ticked off                                            
check_1.pack()

check_2 = ttk.Checkbutton(window,
                        text = 'Checkbox 2',
                        command = lambda: check_var.set(5))  # WHen clicking on checkbox one this well set the offvalue to off of first checkbox                                         
check_2.pack()

# Radio button == Idea is to only have on button activated == HAVE UNIQUE VALUES
radio_var = tk.StringVar()  # Will convert any type of variable into a string
radio1 = ttk.Radiobutton(window,
                        text = 'Radiobutton 1',     # Default value automatically set is 0, when multiple buttons gets complicated
                        value = 'radio 1',          # When a value is set and there are multiple radio buttons, it will now not trigger together
                        variable = radio_var,
                        command = lambda: print(radio_var.get()))  # This will return the value 'radio 1'
radio1.pack() 
                              
radio2 = ttk.Radiobutton(window,
                        text = 'Radiobutton 2',
                        value = 2,
                        variable = radio_var,   # Setting the same tk variable for 2nd radio button
                        command = lambda: print(radio_var.get()))
radio2.pack()

# Create another checkbutton and 2 radiobuttons
# Radio button:
    # Values for the buttons are A and B
     #Ticking either prints the value of the checkbutton
    # Ticking the radio button unchecks the checkbutton
# Check button:
    # Ticking the checkbutton prints the value of the radio button value
    # Use tkinter var for booleans

# Function to print the values of the Radio but & Tick off Ckeck buttonSS
def radio_func():
    print(ex_check_var.get())
    ex_check_var.set(False)
    
# Tkinter variable to store in vales from Radio button
ex_radio_var = tk.StringVar()
ex_radio_1 = ttk.Radiobutton(window,
                             text = 'RadioButton 1 Exercise',
                             value = 'A',
                             variable = ex_radio_var,
                             command = radio_func)
ex_radio_1.pack()

ex_radio_2 = ttk.Radiobutton(window,
                             text = 'RadioButton 2 Exercise',
                             value = 'B',
                             variable = ex_radio_var,
                             command = radio_func)
ex_radio_2.pack()

ex_check_var = tk.BooleanVar()
check_ex = ttk.Checkbutton(window,
                       text = 'Reset Radiobutton',
                       variable = ex_check_var,
                       offvalue = False,
                       command = lambda: print(ex_radio_var.get()))    
check_ex.pack()  

# Run
window.mainloop()