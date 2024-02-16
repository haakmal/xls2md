import os
import tkinter as tk
from tkinter import ttk

def get_markdown_files(folder_path):
    markdown_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".md"):
            markdown_files.append(os.path.splitext(file)[0])
    return markdown_files

def save_selection():
    selected_file.set(drop_down_var.get())
    selected_label.config(text=f"Selected File: {drop_down_var.get()}")

# Folder path where markdown files are located
folder_path = "/Users/z3534868/Library/CloudStorage/OneDrive-UNSW/Academia/20 Databases/22 People"

# Create Tkinter window
root = tk.Tk()
root.title("Markdown File Selector")

# Fetch markdown file names
markdown_files = get_markdown_files(folder_path)

# Create a variable to store selected file
selected_file = tk.StringVar(root)

# Create label
label = ttk.Label(root, text="Select a Markdown File:")
label.grid(row=0, column=0, padx=10, pady=10)

# Create drop down list
drop_down_var = ttk.Combobox(root, textvariable=selected_file, values=markdown_files, state="readonly", width=30)
drop_down_var.grid(row=0, column=1, padx=10, pady=10)

# Create button to save selection
save_button = ttk.Button(root, text="Save Selection", command=save_selection)
save_button.grid(row=1, columnspan=2, padx=10, pady=10)

# Create label to display selected file
selected_label = ttk.Label(root, text="")
selected_label.grid(row=2, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
