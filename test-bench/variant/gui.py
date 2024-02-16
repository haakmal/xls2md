import tkinter as tk
from tkinter import filedialog
from convert import convert_excel_to_md

def process_excel_and_template():
    # Get the path of the Excel file
    excel_file = filedialog.askopenfilename(title="Select Excel file", filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))

    # Get the path of the template markdown file
    template_file = filedialog.askopenfilename(title="Select Template Markdown file", filetypes=(("Markdown files", "*.md"), ("All files", "*.*")))

    # Get additional data from the text box
    additional_data = additional_data_text.get("1.0", "end-1c")

    # Get the value of the checkbox
    checkbox_value = checkbox_var.get()

    # Get the selected term from the radio buttons
    selected_term = term_var.get()

    # Convert Excel to Markdown
    convert_excel_to_md(excel_file, template_file, additional_data, checkbox_value, selected_term)

# Create the main window
root = tk.Tk()
root.title("Excel to Markdown Converter")

# Create a text box for additional data input
additional_data_label = tk.Label(root, text="Additional Data:")
additional_data_label.pack()
additional_data_text = tk.Text(root, height=4, width=50)
additional_data_text.pack()

# Create a checkbox
checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Include Checkbox Value", variable=checkbox_var)
checkbox.pack()

# Create radio buttons for selecting the term
term_var = tk.StringVar()
term_var.set("")  # initialize

term_label = tk.Label(root, text="Select Term:")
term_label.pack()

terms = [("T1", "T1"), ("T2", "T2"), ("T3", "T3")]
for text, term in terms:
    radio_button = tk.Radiobutton(root, text=text, variable=term_var, value=term)
    radio_button.pack()

# Create a button to process the Excel file and template
process_button = tk.Button(root, text="Process Excel File and Template", command=process_excel_and_template)
process_button.pack()

# Run the GUI
root.mainloop()
