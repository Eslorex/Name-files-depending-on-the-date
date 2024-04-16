import os
import datetime
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files(directory):

    months_en = {
        1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
    }


    parent_folder_name = os.path.basename(directory)


    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


    modified_times = {}
    for file in files:
        mod_time = os.path.getmtime(os.path.join(directory, file))
        modified_times[file] = datetime.datetime.fromtimestamp(mod_time)


    sorted_files = sorted(modified_times.items(), key=lambda x: x[1])


    date_counts = {}


    for file, mod_time in sorted_files:
        date_str = mod_time.strftime("%Y-%m-%d")
        year, month, day = map(int, date_str.split('-'))
        simple_date_str = f"{day} {months_en[month]} {year}"

        if simple_date_str not in date_counts:
            date_counts[simple_date_str] = 1
        else:
            date_counts[simple_date_str] += 1


        new_name = f"{parent_folder_name} - {simple_date_str}"
        if date_counts[simple_date_str] > 1:
            new_name += f" - {date_counts[simple_date_str]}"


        extension = os.path.splitext(file)[1]
        new_file_name = new_name + extension

 
        os.rename(os.path.join(directory, file), os.path.join(directory, new_file_name))
    
    messagebox.showinfo("Success", "Files have been renamed successfully!")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        rename_files(directory)

def create_gui():
    root = tk.Tk()
    root.title("File Renamer")

    tk.Label(root, text="Select a directory and rename all files based on last modification time.").pack(pady=20)

    select_button = tk.Button(root, text="Select Directory and Rename Files", command=select_directory)
    select_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
