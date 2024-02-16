import pandas as pd
import os
from tkinter import Tk, Label, Button, Text, filedialog, Radiobutton, StringVar, OptionMenu
from datetime import datetime

def convert_to_md(xls_file, template_file, additional_data, selected_radio, selected_filename):
    # Load Excel file
    df = pd.read_excel(xls_file)

    # Get column names
    columns = df.columns.tolist()

    # Create directory to save MD files
    md_dir = "md_files"
    os.makedirs(md_dir, exist_ok=True)

    # Iterate over each row
    for index, row in df.iterrows():
        # Create YAML front matter
        yaml_front_matter = "---\n"
        for column in columns:
            yaml_front_matter += f"{column}: {row[column]}\n"
        current_year = datetime.now().year
        yaml_front_matter += f"additional_data: {additional_data}/{current_year}/{selected_radio}/{selected_filename}\n"
        yaml_front_matter += "---\n\n"

        # Create MD content
        md_content = open(template_file, 'r').read()
        md_content = md_content.replace("{{YAML_DATA}}", yaml_front_matter)

        # Write to MD file
        md_filename = os.path.join(md_dir, f"{row[columns[0]]}.md")
        with open(md_filename, 'w') as md_file:
            md_file.write(md_content)

    print("Conversion completed successfully.")

def select_file(label):
    filename = filedialog.askopenfilename()
    label.config(text=filename)
    return filename

def select_folder():
    foldername = filedialog.askdirectory()
    filenames = [os.path.splitext(file)[0] for file in os.listdir(foldername)]
    filename_dropdown['menu'].delete(0, 'end')
    for name in filenames:
        filename_dropdown['menu'].add_command(label=name, command=lambda value=name: selected_filename.set(value))

def process_files():
    xls_file = xls_label.cget("text")
    template_file = template_label.cget("text")
    additional_data = additional_data_text.get("1.0", "end-1c")
    selected_radio = radio_var.get()

    if xls_file and template_file:
        convert_to_md(xls_file, template_file, additional_data, selected_radio, selected_filename)
    else:
        print("Please select both XLS and template files.")

# Create GUI window
root = Tk()
root.title("XLS to MD Converter")

# Select XLS file
xls_label = Label(root, text="Select XLS file:")
xls_label.pack()
xls_button = Button(root, text="Browse", command=lambda: select_file(xls_label))
xls_button.pack()

# Select template file
template_label = Label(root, text="Select template file:")
template_label.pack()
template_button = Button(root, text="Browse", command=lambda: select_file(template_label))
template_button.pack()

# Additional data
additional_data_label = Label(root, text="Additional data for YAML:")
additional_data_label.pack()
additional_data_text = Text(root, height=4)
additional_data_text.pack()

# Radio buttons for T1, T2, T3
radio_var = StringVar()
radio_var.set("T1")  # Default selection
radio_label = Label(root, text="Select T:")
radio_label.pack()
radio_t1 = Radiobutton(root, text="T1", variable=radio_var, value="T1")
radio_t1.pack(anchor="w")
radio_t2 = Radiobutton(root, text="T2", variable=radio_var, value="T2")
radio_t2.pack(anchor="w")
radio_t3 = Radiobutton(root, text="T3", variable=radio_var, value="T3")
radio_t3.pack(anchor="w")

# Select folder for filenames
select_folder_button = Button(root, text="Select Folder for Filenames", command=select_folder)
select_folder_button.pack()

# Dropdown menu for filenames
selected_filename = StringVar(root)
selected_filename.set("Select Filename")
filename_dropdown = OptionMenu(root, selected_filename, "Select Filename")
filename_dropdown.pack()

# Process button
process_button = Button(root, text="Convert to MD", command=process_files)
process_button.pack()

# Run GUI
root.mainloop()
