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
    months_tr = {
        1: "Ocak", 2: "Şubat", 3: "Mart", 4: "Nisan", 5: "Mayıs", 6: "Haziran",
        7: "Temmuz", 8: "Ağustos", 9: "Eylül", 10: "Ekim", 11: "Kasım", 12: "Aralık"
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
            errors.append((file, "Dosya başka bir işlem tarafından kilitlenmiş"))
            continue

        date_str = mod_time.strftime("%Y-%m-%d")
        year, month, day = map(int, date_str.split('-'))
        simple_date_str = f"{day} {months_tr[month]} {year}"

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
            text_widget.insert(END, f'"{file}" adı "{new_file_name}" olarak değiştirildi\n')
        except PermissionError as e:
            errors.append((file, str(e)))
        except Exception as e:
            errors.append((file, str(e)))

    if errors:
        error_message = f"{len(errors)} dosya adı değiştirilemedi:\n\n"
        for file, error in errors:
            error_message += f"{file}: {error}\n"
        messagebox.showerror("Hata", error_message)
        text_widget.insert(END, error_message)
    else:
        messagebox.showinfo("Başarılı", "Tüm dosyaların adı başarıyla değiştirildi.")
        text_widget.insert(END, "Tüm dosyaların adı başarıyla değiştirildi.\n")

def select_directory(text_widget):
    directory = filedialog.askdirectory()
    if directory:
        text_widget.delete('1.0', END)
        rename_files(directory, text_widget)
    else:
        messagebox.showwarning("Uyarı", "Hiçbir dizin seçilmedi.")

def create_ui():
    root = Tk()
    root.title("Dosya Yeniden Adlandırıcı")

    select_button = Button(root, text="Dizin Seç", command=lambda: select_directory(output_text))
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
