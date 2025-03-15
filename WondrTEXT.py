import sys
import time
import tkinter as tk
from tkinter import filedialog, Text, Button, Label, Menu, IntVar

# Create the main window
root = tk.Tk()
root.title("Wonder Text Editor")  # Set the title
text = Text(root)
text.grid()

# WPM timing
start_time = None  # Declare global start time
WPM = 0

def SaveAs():
    t = text.get("1.0", "end-1c")
    saveloc = filedialog.asksaveasfilename()
    if saveloc:  # Ensure a file is selected
        with open(saveloc, "w+") as filesaved:
            filesaved.write(t)

# Save button
SveButton = Button(root, text="Save", command=SaveAs)
SveButton.grid()

# Fonts function
def FontHelv():
    text.config(font="Helvetica")

def FontCal():
    text.config(font="Calibri")  # Fixed font name

def Timesnewr():
    text.config(font="Times New Roman")

# WPM Calculation
def on_press(event):
    global start_time, WPM  

    if start_time is None:
        start_time = time.time()

    content = text.get("1.0", "end-1c")
    word_count = len(content.split())  

    # Update WPM every time a key is pressed
    elapsed_time = time.time() - start_time
    if elapsed_time > 0:
        WPM = int((word_count / elapsed_time) * 60)
    else:
        WPM = 0

    wpm_label.config(text=f"WPM: {WPM}")  

# WPM label
wpm_label = Label(root, text="WPM: 0")
wpm_label.grid()

# Bind key press event to track typing
text.bind("<KeyPress>", on_press)

# Menu setup
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Font menu
font_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Font", menu=font_menu)

helvetica = IntVar()
Times_New_Roman = IntVar()
Calibri = IntVar()

font_menu.add_checkbutton(label="Helvetica", variable=helvetica, command=FontHelv)
font_menu.add_checkbutton(label="Calibri", variable=Calibri, command=FontCal)
font_menu.add_checkbutton(label="Times New Roman", variable=Times_New_Roman, command=Timesnewr)

# Run the application
root.mainloop()
