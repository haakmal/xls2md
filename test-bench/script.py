# Made using ChatGPT
# Iterate over each row in an Excel sheet, extract column data to a MD file for each row
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import yaml
import datetime

def process_excel_and_template():
    # Get the path of the Excel file
    excel_file = filedialog.askopenfilename(title="Select Excel file", filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))
    
    # Get the path of the template markdown file
    template_file = filedialog.askopenfilename(title="Select Template Markdown file", filetypes=(("Markdown files", "*.md"), ("All files", "*.*")))
    
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file)
    
    # Read the template markdown file
    with open(template_file, "r") as template:
        template_content = template.read()
    
    # Get full class (DART1140) from the text box
    class_data = class_data_text.get("1.0", "end-1c")
    # Get tutor name from the text box
    tutor_data = tutor_data_text.get("1.0", "end-1c")
    
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Extract filename from the first column
        filename = row.iloc[0]
        
        # Extract data from other columns and store in a dictionary
        data = {"filename": filename}
        for col in df.columns[1:]:
            data[col] = row[col]
        
        # Include additional data provided through the GUI
        if class_data:
            today = datetime.date.today()
            data["tags"] = class_data + "/" + today.strftime("%Y") + "/" + term_var.get()
        
        # Get the value from name column
        name_value = row.iloc[1]

        # Get the value from email column
        email_value = row.iloc[2]
        
        # Convert dictionary to YAML string with "---" at the top
        yaml_str = "---\n" + f"alias: {name_value}\nlevel: " + level_var.get() + "\n" + yaml.dump(data, default_flow_style=False) + f"email: {email_value}"
        title_str = f"# {name_value}\n" + f"## [[{class_data}]]\n" + f"Tutor:: [[{tutor_data}]]"
        
        # Replace keywords in MD
        template_content = template_content.replace("{{YAML_DATA}}", yaml_str)
        template_content = template_content.replace("{{TITLE_DATA}}", title_str)
        
        # Write markdown content to file
        with open(f"{filename}.md", "w") as file:
            file.write(template_content)

# Create the main window
root = tk.Tk()
root.title("Excel to Markdown Converter")

# Create a text box for additional data input
class_data_label = tk.Label(root, text="Enter full class:")
class_data_label.pack()
class_data_text = tk.Text(root, height=1, width=50)
class_data_text.pack()

tutor_data_label = tk.Label(root, text="Enter Tutor Name:")
tutor_data_label.pack()
tutor_data_text = tk.Text(root, height=1, width=50)
tutor_data_text.pack()

# Create radio buttons for selecting the term
term_var = tk.StringVar()
term_var.set("")  # initialize

term_label = tk.Label(root, text="Select Term:")
term_label.pack()

terms = [("T1", "T1"), ("T2", "T2"), ("T3", "T3")]
for text, term in terms:
    radio_button = tk.Radiobutton(root, text=text, variable=term_var, value=term)
    radio_button.pack()

# Create radio buttons for selecting level
level_var = tk.StringVar()
level_var.set("")  # initialize

level_label = tk.Label(root, text="Select Level:")
level_label.pack()

levels = [("UG", "UG"), ("PG", "PG")]
for text, level in levels:
    radio_button = tk.Radiobutton(root, text=text, variable=level_var, value=level)
    radio_button.pack()

# Create a button to process the Excel file and template
process_button = tk.Button(root, text="Process Excel File and Template", command=process_excel_and_template)
process_button.pack()

# Run the GUI
root.mainloop()