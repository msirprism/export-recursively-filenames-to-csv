import os
import csv
from pathlib import Path
from typing import List, Dict
from datetime import datetime

def expand_path(path: str) -> Path:
    """
    Convertit un chemin avec ~ en chemin absolu.
    
    Args:
        path (str): Chemin potentiellement avec ~
    
    Returns:
        Path: Chemin absolu
    """
    return Path(os.path.expanduser(path)).resolve()

def list_files_recursively(root_dir: str) -> List[Dict[str, str]]:
    """
    Parcourt récursivement un répertoire et collecte les informations sur les fichiers.
    
    Args:
        root_dir (str): Chemin du répertoire racine à explorer
    
    Returns:
        List[Dict[str, str]]: Liste des informations de fichiers
    """
    files_info = []
    root_path = expand_path(root_dir)
    
    if not root_path.exists():
        print(f"Le répertoire {root_path} n'existe pas.")
        return []

    print(f"Scanning du répertoire: {root_path}")

    try:
        # Parcours récursif du répertoire
        for file_path in root_path.rglob('*'):
            if file_path.is_file():  # On ne prend que les fichiers, pas les dossiers
                try:
                    relative_parent = file_path.parent.relative_to(root_path)
                except ValueError:
                    relative_parent = file_path.parent
                
                # Remove .docx extension from the file name
                file_name = file_path.name
                if file_name.endswith('.docx'):
                    file_name = file_name[:-5]  # Remove the last 5 characters (.docx)
                
                files_info.append({
                    'chemin_complet': str(file_path),
                    'nom_fichier': file_name,
                    'dossier_parent': str(relative_parent)
                })
                print(f"Fichier trouvé: {file_name}")
    except Exception as e:
        print(f"Erreur lors du parcours du répertoire: {e}")
        return []

    return files_info

def save_to_csv(files_info: List[Dict[str, str]], output_file: str) -> bool:
    """
    Sauvegarde les informations des fichiers dans un CSV.
    
    Args:
        files_info (List[Dict[str, str]]): Liste des informations de fichiers
        output_file (str): Nom du fichier CSV de sortie
    
    Returns:
        bool: True si succès, False si échec
    """
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['chemin_complet', 'nom_fichier', 'dossier_parent']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            
            writer.writeheader()
            writer.writerows(files_info)
        return True
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du CSV: {e}")
        return False

def main():
    # Configuration
    root_directory = "~/Documents/Partenaires/Ouali-Avocat.fr/Articles"  # Chemin avec ~
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"liste_fichiers_{timestamp}.csv"

    # Collecte des fichiers
    files_info = list_files_recursively(root_directory)
    
    if not files_info:
        print("Aucun fichier trouvé ou une erreur s'est produite")
        return

    # Sauvegarde dans le CSV
    if save_to_csv(files_info, output_file):
        print(f"Fichier CSV créé avec succès: {output_file}")
        print(f"Nombre de fichiers traités: {len(files_info)}")
    else:
        print("Erreur lors de la création du fichier CSV")

if __name__ == "__main__":
    main()
