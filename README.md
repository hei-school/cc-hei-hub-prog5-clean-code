# Cloud File Manager

This application allows users to upload/delete/read files to a cloud-like storage. It features additional error handling for various scenarios.

## Table of Contents

- [Introduction](#introduction)
- [Functionality](#functionality)
- [Branches](#branches)
- [Error Handling](#error-handling)


## Introduction

The Cloud File Manager is a user-friendly application designed to facilitate file management. It provides a simple interface for uploading, deleting, and reading files in a cloud-like storage system.
## Functionality

- **Upload Files:** Users can easily upload files to the cloud storage.
- **Delete Files:** Remove files from the cloud storage.
- **Read Files:** View the content of files stored in the cloud.

## Branches

- **[feature/python](https://github.com/hei-school/cc-hei-hub-prog5-clean-code/tree/feature/python):** Includes enhancements related to Python features.
- **[feature/js](https://github.com/hei-school/cc-hei-hub-prog5-clean-code/tree/feature/js):** Includes enhancements related to JavaScript features.


## Error Handling

The application incorporates error handling to enhance robustness:

- **DuplicatedFileError:** Handles the case when a file with the same name already exists during an upload.
- **FilenameInvalidError:** Manages errors when an invalid filename is encountered during file operations.
- **FileTooLargeError:** Ensures that files exceeding a specified size limit are not uploaded.
- **BadFileTypeError:** Handles errors when attempting to upload files with unsupported file types.
- **FileNotFoundError:** Handles errors when attempting to delete or read a file that is not found.

