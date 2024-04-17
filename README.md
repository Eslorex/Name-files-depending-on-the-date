# Mass-Rename-Files-with-Date
This tool renames all files based on the last changed date within the selected path. 

**Warning:** Be careful with non-UI version to prevent renaming wrong files.

## Info
- **Language Support:** TR for Turkish, EN for English months.
- **UI Version:** Simply select the path using the button, and the files will be automatically renamed.

## Questions

### How does renaming work?
- Files are renamed based on the parent folder's name. 
- **Naming Format:** "Parent Folder Name - DD Month YYYY".
- If multiple folders have the same last changed date, the file in the most recently modified folder gets an incremented number (e.g., "Parent Folder Name - 13 April 2024 - 2").

### How does the non-UI version work?
- This version is faster and renames files located in the same directory as the script.

### Why use a .pyw file? 
- The .pyw extension prevents the console window from appearing when using the UI version.

### Why use the parent folder's name?
- This helps to display the project name directly in the file name.

### What are the use cases?
- This tool is ideal for basic version control.
- For instance, if you typically name your project files non-descriptively (like "asdgj", "project1", "untitled"), this tool allows you to assign meaningful names based on their creation date and parent folder.
- Example Use Case: If you're working on a music project titled "MISTED", create a folder named "MISTED". As you save various versions of the project files, use this tool to mass rename them. This ensures your files are organized and labeled with both the project name and the date.
