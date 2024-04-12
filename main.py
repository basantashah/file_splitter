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
        
    # taking different file type
    def browse_file():
        file_type = file_type_var.get()
        filetypes = [("CSV files","*.csv"), ("Excel Files","*.xlsx"), ("Text Files","*.txt"), ("SQL Files","*.sql")]
        
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        input_file_entry.delete(0, tk.END)
        input_file_entry.insert(0, file_path)
        
    def browse_output_dir():
        output_dir = filedialog.askdirectory()
        output_dir_entry.delete(0, tk.END)
        output_dir_entry.insert(0, output_dir)
        
        
    # Creating GUI windows
    root = tk.Tk()
    root.title("Ncell File Splitter")
    root.geometry("750x250")
    root.configure(bg="grey")
    
    #dropdown for fileTypes
    file_type_var = tk.StringVar(root)
    file_type_var.set("CSV") #I am choosing CSV as default for now
    file_type_label = tk.Label(root, text="File Type:", bg="red")
    file_type_label.grid(row=1, column=0, padx=10, pady=5)
    file_type_dropdown = tk.OptionMenu(root, file_type_var, "CSV", "Excel","Text","SQL")
    file_type_dropdown.grid(row=1, column=1, padx=10, pady=5)
    
    # selecting input files
    input_file_lable = tk.Label(root, text="Input File=",bg="red") #need to change this color as per company branding
    input_file_lable.grid(row=2, column=0, padx=10, pady=5)
    input_file_entry = tk.Entry(root, width=50) #need to change this later for symmetry, I will do this in end
    input_file_entry.grid(row=2, column=1, padx=10, pady=5)
    browse_input_button = tk.Button(root, text="Browse", command=browse_file)
    browse_input_button.grid(row=2, column=2, padx=10, pady=5)
    
    # textbox to choose batchsize
    batch_size_label = tk.Label(root, text="Enter Batch Size", bg="Red") # I will change color later
    batch_size_label.grid(row=3, column=0, padx=10, pady=5)
    batch_size_entry = tk.Entry(root)
    batch_size_entry.grid(row=3, column=1, padx=10, pady=5)
    
    # button to choose output dir
    output_dir_label = tk.Label(root, text="Choose output Dir", bg="red") # I will change this color later
    output_dir_labl.grid(row=4, colomn=0, padx=10, pady=5)
    output_dir_entry = tk.Entry(root, width=50) #need to beautify this later
    output_dir_entry.grid(row=4, column=1, padx=10, pady=5)
    browse_output_button = tk.Button(root, text="Browse:", bg="Pink") # will change this later for color profile
    browse_output_button.grid(row=5, column=2, padx=10, pady=5)
    
    # creating batches button
    create_batches_button = tk.Button(root, text="Create Batches", command=create_batches, bg="blue") #I will change color family later
    create_batches_button.grid(row=6, column=1, padx=10, pady=10)    
    
    # display result
    result_label = tk.Label(root, text="Batches Created Successfully", bg="Black")
    result_label.grid(row=7, column=1, padx=10, pady=5)
    
    
    
    
    # closing loop
    root.mainloop()
        