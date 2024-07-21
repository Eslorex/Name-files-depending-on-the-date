import os
import datetime
import sys
from tkinter import Tk, filedialog, messagebox, Button, Text, END, Scrollbar, VERTICAL, RIGHT, Y

def is_file_locked(filepath):
    """ Check if the file is locked by attempting to open it """
    try:
        with open(filepath, 'a'):
            return False
    except IOError:
        return True

def rename_files(directory, text_widget):
    months_en = {
        1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
    }

    parent_folder_name = os.path.basename(directory)
    script_name = os.path.basename(sys.argv[0])
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f != script_name]

    modified_times = {}
    for file in files:
        mod_time = os.path.getmtime(os.path.join(directory, file))
        modified_times[file] = datetime.datetime.fromtimestamp(mod_time)

    sorted_files = sorted(modified_times.items(), key=lambda x: x[1])

    date_counts = {}
    errors = []

    for file, mod_time in sorted_files:
        if is_file_locked(os.path.join(directory, file)):
            errors.append((file, "File is locked by another process"))
            continue

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

        try:
            os.rename(os.path.join(directory, file), os.path.join(directory, new_file_name))
            text_widget.insert(END, f'Renamed "{file}" to "{new_file_name}"\n')
        except PermissionError as e:
            errors.append((file, str(e)))
        except Exception as e:
            errors.append((file, str(e)))

    if errors:
        error_message = f"{len(errors)} files couldn't be renamed:\n\n"
        for file, error in errors:
            error_message += f"{file}: {error}\n"
        messagebox.showerror("Error", error_message)
        text_widget.insert(END, error_message)
    else:
        messagebox.showinfo("Success", "All files were renamed successfully.")
        text_widget.insert(END, "All files were renamed successfully.\n")

def select_directory(text_widget):
    directory = filedialog.askdirectory()
    if directory:
        text_widget.delete('1.0', END)
        rename_files(directory, text_widget)
    else:
        messagebox.showwarning("Warning", "No directory selected.")

def create_ui():
    root = Tk()
    root.title("File Renamer")

    select_button = Button(root, text="Select Directory", command=lambda: select_directory(output_text))
    select_button.pack(pady=10)

    scrollbar = Scrollbar(root, orient=VERTICAL)
    output_text = Text(root, wrap='word', yscrollcommand=scrollbar.set)
    scrollbar.config(command=output_text.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    output_text.pack(padx=10, pady=10, fill='both', expand=True)

    root.geometry("600x400")
    root.mainloop()

if __name__ == "__main__":
    create_ui()
