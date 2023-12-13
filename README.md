[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/wTBA-Etm)

# Cloud File Manager

This program is a simple cloud file manager implemented using PySimpleGUI for the user interface and Python for the business logic. It allows you to upload, delete, and read files in a local cloud directory.

## Features

1. **File Upload:**
   - You can select a local file to upload to the cloud.

2. **File Deletion:**
   - Delete an existing file in the cloud.

3. **File Reading:**
   - Display the content of a specified file.

## Handled Error Types

The program manages several types of errors to ensure a robust user experience:

- **DuplicatedFileError (Code: 100):**
  - Indicates an attempt to upload a file already present in the cloud.

- **FileTooLargeError (Code: 423):**
  - Indicates that a file exceeds the maximum allowed size for uploading.

- **BadFileTypeError (Code: 400):**
  - Signals an attempt to upload an unsupported file type.

- **FileNotFoundError404 (Code: 404):**
  - Indicates that a specified file for deletion or reading was not found in the cloud.

- **FilenameInvalidError (Code: 400):**
  - Signals that the specified file name is poorly written or invalid.

- **FilenameTooLongError (Code: 414):**
  - Indicates that the specified file name is too long.

## Prerequisites

- Python 3.x installed.
- PySimpleGUI library installed (`pip install PySimpleGUI`).

## Usage

1. Clone this repository to your local machine.
git clone https://github.com/YourName/cloud-manager.git

2. Navigate to the project directory.
cd cloud-manager

3. Run the program
python cloud_file_manager.py










