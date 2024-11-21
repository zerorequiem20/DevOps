import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET

def clean_xml_content(xml_content):
    try:
        # Parse the XML content
        tree = ET.ElementTree(ET.fromstring(xml_content))
        root = tree.getroot()

        # Remove elements with empty tags
        for elem in root.findall('.//*'):
            if not elem.attrib:  # if the element has no attributes, it's empty
                root.remove(elem)

        # Return cleaned XML as a string
        return ET.tostring(root, encoding='unicode')

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return None

def upload_and_process_file():
    # Open a file dialog to select the XML file
    file_path = filedialog.askopenfilename(
        title="Select XML File",
        filetypes=(("XML files", "*.xml"), ("All files", "*.*"))
    )
    
    if not file_path:
        print("No file selected.")
        return

    print(f"File selected: {file_path}")
    
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()

    # Process the XML to clean empty elements
    cleaned_xml = clean_xml_content(xml_content)
    
    if cleaned_xml:
        # Open a save file dialog to choose the save location and filename
        cleaned_file_path = filedialog.asksaveasfilename(
            title="Save Cleaned XML File",
            defaultextension=".xml",  # Default file extension
            filetypes=(("XML files", "*.xml"), ("All files", "*.*"))
        )
        
        if cleaned_file_path:  # Check if the user provided a filename
            with open(cleaned_file_path, 'w', encoding='utf-8') as cleaned_file:
                cleaned_file.write(cleaned_xml)
            print(f"Cleaned XML saved as {cleaned_file_path}")

# Create the upload button and UI elements
def create_upload_button():
    root = tk.Tk()
    root.title("XML File Uploader")

    # Add logo and description
    logo_label = tk.Label(root, text="Data Manager", font=("Helvetica", 24, "bold"), pady=20)
    logo_label.pack()

    description_label = tk.Label(root, text="You can upload the file you want to clean.\n"
                                             "This program will remove empty table lists from the file you upload.", 
                                  font=("Helvetica", 12), pady=10, padx=10)
    description_label.pack()

    upload_button = tk.Button(root, text="Upload XML File", command=upload_and_process_file)
    upload_button.pack(pady=20)

    root.mainloop()

# Start the program with the upload button
create_upload_button()
