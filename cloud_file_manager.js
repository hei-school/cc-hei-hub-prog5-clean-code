const { app, BrowserWindow, ipcMain, dialog } = require('electron');
const fs = require('fs');
const path = require('path');

const CLOUD_DIR = "cloud_files";

function createWindow() {
  const win = new BrowserWindow({
    width: 600,
    height: 400,
    webPreferences: {
      nodeIntegration: true
    }
  });

  win.loadFile('index.html');

  win.on('closed', () => {
    app.quit();
  });
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

function uploadFile(sourcePath) {
  try {
    const filename = path.basename(sourcePath);
    const destinationPath = path.join(__dirname, CLOUD_DIR, filename);

    if (fs.existsSync(destinationPath)) {
      throw new Error(`Le fichier '${filename}' existe déjà dans le cloud.`);
    }

    fs.copyFileSync(sourcePath, destinationPath);
    console.log(`Fichier '${filename}' uploadé avec succès.`);
  } catch (error) {
    console.error(`Erreur lors de l'upload : ${error.message}`);
  }
}

function deleteFile(fileName) {
  try {
    const filePath = path.join(__dirname, CLOUD_DIR, fileName);
    fs.unlinkSync(filePath);
    console.log(`Fichier '${fileName}' supprimé avec succès.`);
  } catch (error) {
    console.error(`Erreur lors de la suppression : ${error.message}`);
  }
}

function readFile(fileName) {
  try {
    if (!fileName.match(/^[a-zA-Z0-9]+$/)) {
      throw new Error("Le nom de fichier est mal écrit.");
    }

    const filePath = path.join(__dirname, CLOUD_DIR, fileName);
    const content = fs.readFileSync(filePath, 'utf-8');
    console.log(`Contenu du fichier '${fileName}':\n${content}`);
  } catch (error) {
    console.error(`Erreur lors de la lecture : ${error.message}`);
  }
}

ipcMain.on('upload-file', (event, sourcePath) => {
  uploadFile(sourcePath);
});

ipcMain.on('delete-file', (event, fileName) => {
  deleteFile(fileName);
});

ipcMain.on('read-file', (event, fileName) => {
  readFile(fileName);
});
