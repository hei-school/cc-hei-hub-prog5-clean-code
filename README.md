# Cloud File Manager with Electron

This Electron app serves as a simple cloud file manager allowing users to upload, delete, and read files in a local cloud directory.

## Features

- **Upload Files:**
  - Select a local file to upload to the cloud directory.

- **Delete Files:**
  - Remove an existing file from the cloud directory.

- **Read Files:**
  - Display the content of a specified file in the cloud directory.

## Project Structure

The project consists of the following key files and directories:

- `main.js`: The main Electron script responsible for window creation and app functionality.
- `index.html`: The HTML file for the Electron app window.
- `cloud_files/`: The directory where uploaded files are stored.

## Prerequisites

Before running the application, ensure you have [Node.js](https://nodejs.org/) installed.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/YourUsername/electron-cloud-manager.git
    ```

2. Navigate to the project directory:

    ```bash
    cd electron-cloud-manager
    ```

3. Install dependencies:

    ```bash
    npm install
    ```

## Usage

Run the application with the following command:

```bash
npm start
