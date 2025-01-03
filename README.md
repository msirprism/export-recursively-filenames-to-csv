# File Lister - Script Python de listage récursif de fichiers

## Description
Ce script Python permet de lister récursivement tous les fichiers d'un répertoire et de ses sous-répertoires, puis de sauvegarder les informations dans un fichier CSV. Il est particulièrement utile pour créer un inventaire de fichiers tout en préservant la structure des dossiers.

## Fonctionnalités
- Parcours récursif des répertoires
- Gestion des caractères spéciaux et des accents
- Export au format CSV avec séparateur point-virgule (;)
- Horodatage automatique des fichiers de sortie
- Support des chemins avec le caractère tilde (~)
- Gestion des erreurs robuste

## Prérequis
- Python 3.6 ou supérieur
- Aucune dépendance externe requise (utilise uniquement la bibliothèque standard Python)

## Installation
1. Clonez ou téléchargez le fichier `list_files.py`
2. Assurez-vous que vous avez les permissions nécessaires sur le répertoire à scanner

## Configuration
Modifiez la variable `root_directory` dans la fonction `main()` du script pour pointer vers le répertoire que vous souhaitez analyser :

```python
root_directory = "~/votre/chemin/vers/le/dossier"
```

## Utilisation
1. Ouvrez un terminal
2. Naviguez vers le dossier contenant le script
3. Exécutez le script :
```bash
python list_files.py
```

## Format de sortie
Le script génère un fichier CSV avec le format suivant :
- Nom : `liste_fichiers_YYYYMMDD_HHMMSS.csv`
- Colonnes :
  - `chemin_complet` : Chemin absolu du fichier
  - `nom_fichier` : Nom du fichier avec extension
  - `dossier_parent` : Chemin relatif du dossier parent

## Messages de sortie
Le script affiche les informations suivantes pendant son exécution :
- Confirmation du début du scan
- Fichiers trouvés
- Nombre total de fichiers traités
- Statut de la création du fichier CSV
- Messages d'erreur éventuels

## Gestion des erreurs
Le script gère les cas suivants :
- Répertoire inexistant
- Problèmes de permissions
- Erreurs de lecture des fichiers
- Erreurs d'écriture du CSV

## Exemple d'utilisation
```python
# Exemple de structure de répertoire
~/Documents/
  └── Projets/
      ├── Projet1/
      │   ├── fichier1.txt
      │   └── fichier2.docx
      └── Projet2/
          └── fichier3.pdf

# Résultat dans le CSV
chemin_complet;nom_fichier;dossier_parent
/Users/user/Documents/Projets/Projet1/fichier1.txt;fichier1.txt;Projet1
/Users/user/Documents/Projets/Projet1/fichier2.docx;fichier2.docx;Projet1
/Users/user/Documents/Projets/Projet2/fichier3.pdf;fichier3.pdf;Projet2
```

## Contribution
N'hésitez pas à proposer des améliorations ou à signaler des bugs.

## Licence
Ce script est fourni tel quel, libre d'utilisation.