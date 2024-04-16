import os
import datetime
import sys

def main():

    months_tr = {
        1: "Ocak", 2: "Şubat", 3: "Mart", 4: "Nisan", 5: "Mayıs", 6: "Haziran",
        7: "Temmuz", 8: "Ağustos", 9: "Eylül", 10: "Ekim", 11: "Kasım", 12: "Aralık"
    }


    directory = os.getcwd()

    parent_folder_name = os.path.basename(directory)

    script_name = os.path.basename(sys.argv[0])
    

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f != script_name]
    

    modified_times = {}
    for file in files:
        mod_time = os.path.getmtime(os.path.join(directory, file))
        modified_times[file] = datetime.datetime.fromtimestamp(mod_time)


    sorted_files = sorted(modified_times.items(), key=lambda x: x[1])
    

    date_counts = {}
    

    for file, mod_time in sorted_files:
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
        

        os.rename(os.path.join(directory, file), os.path.join(directory, new_file_name))
        print(f'Renamed "{file}" to "{new_file_name}"')

if __name__ == "__main__":
    main()
