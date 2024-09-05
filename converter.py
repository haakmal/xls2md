import pandas as pd
import os
from datetime import datetime

def convert_to_md(xls_file, template_file, class_name, selected_radio, selected_filename):
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
            value = row.get(column, "")
            if value:
                if column == "aliases":
                    # Add correct syntax for Obsidian
                    yaml_front_matter += f"{column}:\n  - {value}\n"
                else:
                    yaml_front_matter += f"{column}: {value}\n"
        current_year = datetime.now().year
        yaml_front_matter += f"tags: {class_name}/{current_year}/{selected_radio}"
        # Add additional data for TITLE_DATA
        title_m = f"# {row[columns[1]]}\n## [[{class_name}]]\nTutor:: [[{selected_filename}]]"

        # Read template file
        with open(template_file, 'r') as f:
            template_content = f.read()

        # Insert YAML data into template file
        md_content = template_content.replace("{{YAML_DATA}}", yaml_front_matter)
        md_content = md_content.replace("{{TITLE_DATA}}", title_m)

        # Write to MD file
        md_filename = os.path.join(md_dir, f"{row[columns[0]]}.md")
        with open(md_filename, 'w') as md_file:
            md_file.write(md_content)

    print("Conversion completed successfully.")
