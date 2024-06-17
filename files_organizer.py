#Python File organizer
import os
import shutil

# Specify the path
dossier_data = '/Users/**add your path here**'

# Create extensions dictionary  -> categories
associations = {
    'mp3': 'Music',
    'wav': 'Music',
    'flac': 'Music',
    'avi': 'Videos',
    'mp4': 'Videos',
    'gif': 'Videos',
    'bmp': 'Images',
    'png': 'Images',
    'jpg': 'Images',
    'txt': 'Documents',
    'pptx': 'Documents',
    'csv': 'Documents',
    'xls': 'Documents',
    'odp': 'Documents',
    'pages': 'Documents'
}

# Navigate thru the files of the data dossier
for racine, _, fichiers in os.walk(dossier_data):
    for fichier in fichiers:
        # Obtain extension file
        nom_fichier, extension = os.path.splitext(fichier)
        extension = extension[1:]  # Delete the point at the beginning

        # Determinate the category file with extension
        if extension in associations:
            categorie = associations[extension]
        else:
            categorie = 'Others'

        # Create the destination folder if it doesn't exist
        dossier_destination = os.path.join(dossier_data, categorie)
        os.makedirs(dossier_destination, exist_ok=True)

        # Displace the file in the destination folder
        chemin_source = os.path.join(racine, fichier)
        chemin_destination = os.path.join(dossier_destination, fichier)
        shutil.move(chemin_source, chemin_destination)

print("Organization done!")

#Xafiq
