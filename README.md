# File Renamer Tool

This tool allows you to rename files in a selected directory based on their modification dates. The tool is built with a simple graphical user interface (GUI) using `tkinter`.

## Features

- Select a directory using a graphical file dialog.
- Rename files based on their modification dates.
- Display results in a text area within the application.
- Handle and display errors for files that cannot be renamed.

## Requirements

- Python 3.x
- tkinter library (usually included with Python)

## Usage

1. **Run the script:**
    ```bash
    python file_renamer.py
    ```

2. **Select a directory:**
    - Click on the `Dizin Seç` button.
    - A file dialog will appear.
    - Select the directory containing the files you want to rename.
    - The files will be renamed based on their modification dates.
    - The results will be displayed in the text area within the application.
    - If there are any errors, they will be shown in a message box and also in the text area.
