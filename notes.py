import tkinter as tk
from tkinter import scrolledtext

def save_note():
    note = text_widget.get("1.0", "end-1c")
    with open("note.txt", "w") as file:
        file.write(note)

def load_note():
    try:
        with open("note.txt", "r") as file:
            saved_note = file.read()
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, saved_note)
    except FileNotFoundError:
        pass  # File doesn't exist yet

# Create main window
root = tk.Tk()
root.title("EasyNotes")

# Create Text widget
text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20)
text_widget.pack(padx=10, pady=10)
# Create Save and Load buttons
save_button = tk.Button(root, text="Save", command=save_note)
save_button.pack(side=tk.LEFT, padx=5)

load_button = tk.Button(root, text="Load", command=load_note)
load_button.pack(side=tk.LEFT, padx=5)



# Run the Tkinter event loop
root.mainloop()
