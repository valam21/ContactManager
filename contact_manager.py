import csv
import os

# Nom du fichier CSV où les contacts seront stockés
CONTACT_FILE = 'contacts.csv'
# En-têtes pour le fichier CSV
HEADERS = ['Nom', 'Telephone', 'Email']

def charger_contacts():
    """Charge les contacts depuis le fichier CSV."""
    contacts = []
    if not os.path.exists(CONTACT_FILE):
        # Crée le fichier avec les en-têtes si inexistant
        with open(CONTACT_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)
        return contacts

    with open(CONTACT_FILE, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # Vérifie si le fichier est vide ou si les en-têtes ne correspondent pas
        if not reader.fieldnames or reader.fieldnames != HEADERS:
            print("Attention : Le fichier CSV est vide ou ses en-têtes ne correspondent pas. Création d'un nouveau fichier.")
            # Efface le contenu du fichier et ajoute les en-têtes
            with open(CONTACT_FILE, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(HEADERS)
            return contacts
        for row in reader:
            contacts.append(row)
    return contacts

def sauvegarder_contacts(contacts):
    """Sauvegarde les contacts dans le fichier CSV."""
    with open(CONTACT_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(contacts)

def afficher_menu():
    """Affiche le menu principal de l'application."""
    print("\n--- Gestionnaire de Contacts ---")
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Rechercher un contact")
    print("4. Modifier un contact")
    print("5. Supprimer un contact")
    print("6. Quitter")
    print("-------------------------------")
