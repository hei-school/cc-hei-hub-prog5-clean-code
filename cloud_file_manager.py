import PySimpleGUI as sg
import shutil
import os

CLOUD_DIR = "cloud_files"
SUPPORTED_FILE_EXTENSIONS = {".txt", ".mp4", ".avi", ".pdf", ".jpg", ".jpeg", ".docx"}


class DuplicatedFileError(Exception):
    pass

class FilenameInvalidError(Exception):
    pass

class FileTooLargeError(Exception):
    def __init__(self, message="Le fichier est trop volumineux.", code=423):
        self.message = message
        self.code = code
        super().__init__(self.message)

class BadFileTypeError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

def upload_file(source_path):
    try:
        filename = os.path.basename(source_path)
        
        _, file_extension = os.path.splitext(os.path.basename(source_path))

        if file_extension.lower() not in SUPPORTED_FILE_EXTENSIONS:
            raise BadFileTypeError(f"Le type {file_extension} n'est pas autorisé", 400)
        
        file_size = os.path.getsize(source_path)
        max_file_size_mb = 10
        if file_size > max_file_size_mb * 1024 * 1024:
            raise FileTooLargeError(f"Le fichier dépasse la taille maximale autorisée de {max_file_size_mb} Mo.", code=423)

        destination_path = os.path.join(os.getcwd(), CLOUD_DIR, filename)

        if os.path.exists(destination_path):
            raise DuplicatedFileError(100, f"Le fichier '{filename}' existe déjà dans le cloud.")

        shutil.copy(source_path, destination_path)
        
        print(f"Fichier '{filename}' uploadé avec succès.")
    except FileNotFoundError:
        print("Fichier source non trouvé.")
    except DuplicatedFileError as e:
        print(f"Erreur lors de l'upload : {e}")
    except FileTooLargeError as e:
        print(f"Erreur lors de l'upload : {e}")
    except Exception as e:
        print(f"Erreur lors de l'upload : {e}")

def delete_file(file_name):
    try:
        file_path = os.path.join(os.getcwd(), CLOUD_DIR, file_name)
        os.remove(file_path)
        print(f"Fichier '{file_name}' supprimé avec succès.")
    except FileNotFoundError:
        print(f"Fichier '{file_name}' non trouvé.")
    except Exception as e:
        print(f"Erreur lors de la suppression : {e}")

def read_file(file_name):
    try:
        if not file_name.isalnum():  
            raise FilenameInvalidError(400, "Le nom de fichier est mal écrit.")
        
        file_path = os.path.join(os.getcwd(), CLOUD_DIR, file_name)
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Contenu du fichier '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"Fichier '{file_name}' non trouvé.")
    except FilenameInvalidError as e:
        print(f"Erreur lors de la lecture : {e}")
    except Exception as e:
        print(f"Erreur inattendue lors de la lecture : {e}")

def main():
    sg.theme('DarkGrey2')

    layout = [
        [sg.Text("Sélectionnez un fichier à uploader")],
        [sg.InputText(key='file_path', size=(40, 1), disabled=True), sg.FileBrowse()],
        [sg.Button("Upload"), sg.Button("Delete"), sg.Button("Read"), sg.Button("Quitter")]
    ]

    window = sg.Window("Uploader de fichiers", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Quitter':
            break
        elif event == 'Upload':
            file_path = values['file_path']
            if file_path:
                upload_file(file_path)
            else:
                sg.popup_error("Aucun fichier sélectionné.")
        elif event == 'Delete':
            file_name = sg.popup_get_text("Entrez le nom du fichier à supprimer")
            if file_name:
                delete_file(file_name)
            else:
                sg.popup_error("Veuillez entrer un nom de fichier.")
        elif event == 'Read':
            file_name = sg.popup_get_text("Entrez le nom du fichier à lire")
            if file_name:
                read_file(file_name)
            else:
                sg.popup_error("Veuillez entrer un nom de fichier.")

    window.close()

if __name__ == "__main__":
    if not os.path.exists(CLOUD_DIR):
        os.makedirs(CLOUD_DIR)

    main()
