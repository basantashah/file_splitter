import tkinter as tk
from tkinter import filedialog
import pandas as pd
import gui

def create_batches():
    input_file = input_file_entry.get()
    batch_size = int(batch_size_entry.get())
    output_dir = output_dir_entry.get()
    output_format = output_format_var.get()
    
    try:
        if file_type_var.get() == "CSV":
            data = pd.read_csv(input_file)
        elif file_type_var.get() == "Excel":
            data = pd.read_excel(input_file)
        else:
            data = pd.read_csv(input_file, sep='\t')
        
        batches = [data.iloc[i:i+batch_size] for i in range(0, len(data), batch_size)]
        
        for i, batch in enumerate(batches):
            if output_format == "CSV":
                batch.to_csv(f"{output_dir}/batch_{i+1}.csv", index=False)
            elif output_format == "Excel":
                batch.to_excel(f"{output_dir}/batch_{i+1}.xlsx", index=False)
            elif output_format == "SQL":
                # Write code to handle SQL output
                pass
            else:
                batch.to_csv(f"{output_dir}/batch_{i+1}.txt", index=False)
                
        result_label.config(text="Congratulations, File Created Successfully")
    
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

def browse_file():
    file_type = file_type_var.get()
    filetypes = [("CSV files", "*.csv"), ("Excel Files", "*.xlsx"), ("Text Files", "*.txt"), ("SQL Files", "*.sql")]
    
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, file_path)
        
def browse_output_dir():
    output_dir = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, output_dir)
    
    
# Creating GUI window
root = tk.Tk()
root.title("File Splitter")
root.geometry(gui.windows_size)
root.configure(bg=gui.background_color)

# Labels and Entry Boxes
labels = ["Input File:", "Enter Batch Size:", "Choose Output Dir:"]
for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text, bg=gui.background_color)
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    
    entry = tk.Entry(root, width=50)
    entry.grid(row=i, column=1, padx=10, pady=5)
    if i == 0:  # Browse button for input file
        browse_button = tk.Button(root, text="Browse", command=browse_file)
        browse_button.grid(row=i, column=2, padx=10, pady=5)
    elif i == 2:  # Browse button for output directory
        browse_button = tk.Button(root, text="Browse", command=browse_output_dir)
        browse_button.grid(row=i, column=2, padx=10, pady=5)

# Dropdown for File Type
file_type_var = tk.StringVar(root)
file_type_var.set("CSV")  # Default file type
file_type_label = tk.Label(root, text="File Type:", bg=gui.background_color)
file_type_label.grid(row=len(labels), column=0, padx=10, pady=5, sticky="w")
file_type_dropdown = tk.OptionMenu(root, file_type_var, "Excel", "CSV", "Text", "SQL")
file_type_dropdown.grid(row=len(labels), column=1, padx=10, pady=5, sticky="w")

# Dropdown for Output File Format
output_format_var = tk.StringVar(root)
output_format_var.set("CSV")  # Default output file format
output_format_label = tk.Label(root, text="Output File Format:", bg=gui.background_color)
output_format_label.grid(row=len(labels)+1, column=0, padx=10, pady=5, sticky="w")
output_format_dropdown = tk.OptionMenu(root, output_format_var, "CSV", "Excel", "Text", "SQL")
output_format_dropdown.grid(row=len(labels)+1, column=1, padx=10, pady=5, sticky="w")

# Create Batches Button
create_batches_button = tk.Button(root, text="Create Batches", command=create_batches, bg=gui.button_bg, fg=gui.button_fg)
create_batches_button.grid(row=len(labels)+2, column=1, padx=10, pady=10, sticky="e")

# Copyright and Developed By Labels
copyright_label = tk.Label(root, text="Copyright © Ncell", bg=gui.background_color)
copyright_label.grid(row=len(labels)+3, column=1, padx=10, pady=5, sticky="se")
developed_by_label = tk.Label(root, text="Developed By: Basant K Shah", bg=gui.background_color)
developed_by_label.grid(row=len(labels)+3, column=1, padx=10, pady=5, sticky="se")

root.mainloop()
