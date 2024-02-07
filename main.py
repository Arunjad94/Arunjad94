import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Create a popup
messagebox.showinfo("Popup Title", "Hello, this is a popup!")

# Start the Tkinter main loop
root.mainloop()