import os
from tkinter import Tk, ttk, Label, Button, Text, filedialog, Radiobutton, StringVar, OptionMenu
from converter import convert_to_md  # Import the conversion function from converter.py

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("XLS to MD Converter")
        self.root.geometry("460x290")
        self.root.resizable(False, False)
        self.root.configure(padx=20, pady=20)

        # Description label
        description_label = Label(self.root, text="Hello! I made this program for converting entries in an XLS file\nto individual MD files using a template provided and is meant for\nmy internal teaching database. Feel free to clone the repo and tinker!")
        description_label.grid(row=0, column=0, columnspan=3)

        # GitHub link
        github_link_label = Label(self.root, text="GitHub Repo", fg="blue", cursor="hand2")
        github_link_label.grid(row=1, column=0, columnspan=1)
        github_link_label.bind("<Button-1>", lambda event: self.open_github_link())

        # Personal link
        personal_link_label = Label(self.root, text="Dr Haider Akmal", fg="blue", cursor="hand2")
        personal_link_label.grid(row=1, column=1, columnspan=1)
        personal_link_label.bind("<Button-1>", lambda event: self.open_personal_link())

        # Horizontal line separator
        separator = ttk.Separator(self.root, orient="horizontal")
        separator.grid(row=2, column=0, columnspan=3, sticky="ew", pady=(10))

        # Select XLS file
        self.xls_label = Label(self.root, text="Select XLS file:")
        self.xls_label.grid(row=3, column=0)
        self.xls_button = Button(self.root, text="Browse", command=self.select_file_xls)
        self.xls_button.grid(row=3, column=1)

        # Select template file
        self.template_label = Label(self.root, text="Select MD template:")
        self.template_label.grid(row=4, column=0)
        self.template_button = Button(self.root, text="Browse", command=self.select_file_template)
        self.template_button.grid(row=4, column=1)

        # Additional data
        self.class_name_label = Label(self.root, text="Class Name (e.g. DDES1150):")
        self.class_name_label.grid(row=5, column=0)
        self.class_name_text = Text(self.root, height=1, width=20)
        self.class_name_text.grid(row=5, column=1)

        # Radio buttons for T1, T2, T3
        self.radio_var = StringVar()
        self.radio_var.set("T1")  # Default selection
        radio_label = Label(self.root, text="Select Term:")
        radio_label.grid(row=6, column=0)
        radio_t1 = Radiobutton(self.root, text="T1", variable=self.radio_var, value="T1")
        radio_t1.grid(row=6, column=1, sticky="w")
        radio_t2 = Radiobutton(self.root, text="T2", variable=self.radio_var, value="T2")
        radio_t2.grid(row=6, column=1, sticky="n")
        radio_t3 = Radiobutton(self.root, text="T3", variable=self.radio_var, value="T3")
        radio_t3.grid(row=6, column=1, sticky="e")

        # Select folder for filenames
        select_folder_button = Button(self.root, text="Select tutor database", command=self.select_folder)
        select_folder_button.grid(row=7, column=0)
        self.selected_filename = StringVar(self.root)
        self.selected_filename.set("Select Tutor")
        self.filename_dropdown = OptionMenu(self.root, self.selected_filename, "Select Tutor")
        self.filename_dropdown.grid(row=7, column=1)

        # Process button
        process_button = Button(self.root, text="Convert to MD", command=self.process_files)
        process_button.grid(row=8, column=0, columnspan=2)
    
    def open_github_link(self):
        import webbrowser
        webbrowser.open("https://github.com/your_username/your_repository")
    
    def open_personal_link(self):
        import webbrowser
        webbrowser.open("https://links.hakmal.com/")

    def select_file_xls(self):
        filename = filedialog.askopenfilename()
        if filename:
            foldername, selected_file = os.path.split(filename)
            self.xls_label.config(text=f".../{os.path.basename(foldername)}/{selected_file}")
            self.xls_file_path = filename


    def select_file_template(self):
        filename = filedialog.askopenfilename()
        if filename:
            foldername, selected_file = os.path.split(filename)
            self.template_label.config(text=f".../{os.path.basename(foldername)}/{selected_file}")
            self.template_file_path = filename

    def select_folder(self):
        foldername = filedialog.askdirectory()
        filenames = [os.path.splitext(file)[0] for file in os.listdir(foldername)]
        self.filename_dropdown['menu'].delete(0, 'end')
        for name in filenames:
            self.filename_dropdown['menu'].add_command(label=name, command=lambda value=name: self.selected_filename.set(value))
    
    def process_files(self):
        xls_file = self.xls_file_path
        template_file = self.template_file_path
        class_name = self.class_name_text.get("1.0", "end-1c")
        selected_radio = self.radio_var.get()
        selected_filename = self.selected_filename.get()

        if xls_file and template_file:
            convert_to_md(xls_file, template_file, class_name, selected_radio, selected_filename)
        else:
            print("Please select both XLS and template files.")
