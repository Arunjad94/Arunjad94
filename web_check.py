import requests

def get_number_fact():
    url = f'https://www.youtube.com/watch?v=hzj9kEU8QdA'
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return f"Error: {response.status_code}"

# Example usage
#number_to_check = 18
fact = get_number_fact()
print(f"The fact about  is: {fact}")


import tkinter as tk
from tkinter import scrolledtext, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

def visualize_note():
    try:
        # Assuming the note contains numerical data, you can modify this part based on your data
        data = [float(value) for value in text_widget.get("1.0", "end-1c").split()]
        plt.plot(data)
        plt.title("Visualization of Note")
        plt.xlabel("Index")
        plt.ylabel("Value")

        #Display the plot in a new window
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Note does not contain valid numerical data")

# Create main window
root = tk.Tk()
root.title("EasyNotes")


# Create Text widget with initial text
initial_text = fact
text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20)
load_note()
text_widget.insert(tk.END, initial_text)
text_widget.pack(padx=10, pady=10)

# Create Save, Load, and Visualize buttons
save_button = tk.Button(root, text="Save", command=save_note)
save_button.pack(side=tk.LEFT, padx=5)

load_button = tk.Button(root, text="Load", command=load_note)
load_button.pack(side=tk.LEFT, padx=5)

visualize_button = tk.Button(root, text="Visualize", command=visualize_note)
visualize_button.pack(side=tk.LEFT, padx=5)

# Run the Tkinter event loop
root.mainloop()