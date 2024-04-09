import tkinter as tk 
import pandas as pd 
from tkinter import filedialog
import gui

def create_batches():
    input_file = input_file_entry.get()
    batch_size = int(batch_size_entry.get())
    output_dir = output_dir_entry.get()
    output_format = output_format_var.get()
    
    try:
        if file_type_var.get() == "CVS":
            data = pd.read_csv(input_file)
        elif file_type_var.get() == "Excel":
            data = pd.read_excel(input_file)
        # elif file_type_var.get() == "sql":
        else:
            data = pd.read_csv(input_file, sep='\t')
        
        #after batch size entry, making batch of user input    
        batches = [data.iloc[i:i+batch_size] for i in range(0, len(data), batch_size)]
        
        #using loop in for loop with batch size entered earlier
        for i, batch in enumerate(batches):
            if output_format == "CSV":
                batch.to_csv(f"{output_dir}/batch_{i+1}.csv", index=False)
            elif output_format == "Excel":
                batch.to_excel(f"{output_dir}/batch_{i+1}.xlsx", index=False)
            elif output_dir == "Sql":
                batch.to_sql(f"{output_dir}/batch_{i+1}.sql", index = False)
            else:
                batch.to_csv(f"{output_dir}/batch_{i+1}.txt", index=False)
                
        result_label.config(text= "Congratulations, FIle Created Successfully")
    
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")
        
        
    # Creating GUI windows
    
    root = tk.Tk()
    root.title("Ncell File Splitter")
    root.geometry("750x250")
    root.configure(bg="grey")
    
    
    
    # closing loop
    root.mainloop()
        