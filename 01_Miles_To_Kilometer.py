import tkinter as tk
#from tkinter import ttk 
import ttkbootstrap as ttk # Adds styling

def convert():
    mile_input = (entry_int.get())  # Save the integfer from the entry box  
    km_output = mile_input * 1.61
    output_string.set(km_output)    # Send the outcome of the calculations to output


# Create the main window
#window = tk.Tk()
# Can add themes to the window
window = ttk.Window(themename = 'journal')  # e.g. darkly
# The title of the window
window.title('Demo')
# The size of the visual window
window.geometry('300x150')

# Title >> Text                                                                 'font fontsize bold'
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold')
# Makes the text visible on the window
title_label.pack()

# Need a input field >> Need to put the frame inside the window
input_frame = ttk.Frame(master = window) # This is a frame around the 2 widgets
#Create a seperate variable that can store and udpate variables
entry_int = tk.IntVar()  # Store integer
# Now for the input field and button in the input frame, set those to master >> Need to place those widgets inside the input frame
entry = ttk.Entry(master = input_frame, text = entry_int)    # Anything adding inside the entry field >> will be stored inside entry integer && Updating entryInt going to update the content of the entry field 
# Can add a function in here BUT!! DO NOT CALL THE FUNCTION only use the name of the function, will be called upon pressing the buttom
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)  # Upon pressing want the content of the entry field

# Have the two widgets inside the input frame >> Pack places widgets on top of each other!!
entry.pack(side = 'left', padx = 10)    # Side will place them next to ezach other & padding can be added with padx (x-axis)
button.pack(side = 'left')
input_frame.pack(pady = 10)     # Can use padding to the input from for example on the y-axis

# Output
output_string = tk.StringVar()   # Stores a string instead of integer
output_label = ttk.Label(master = window, 
                         text = 'Output', 
                         font = 'Calibri 24', 
                         textvariable = output_string)      # Textvariable overwrites text which can be used to udpate variables dynamically 

output_label.pack(pady = 5)


# Run the main loop
window.mainloop()