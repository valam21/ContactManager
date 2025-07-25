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

def ajouter_contact(contacts):
    """Permet à l'utilisateur d'ajouter un nouveau contact."""
    print("\n--- Ajouter un Contact ---")
    nom = input("Nom : ").strip()
    telephone = input("Numéro de téléphone : ").strip()
    email = input("Adresse e-mail : ").strip()

    # Vérifier si le contact existe déjà par son nom
    if any(c['Nom'].lower() == nom.lower() for c in contacts):
        print("Erreur : Un contact avec ce nom existe déjà.")
        return

    nouveau_contact = {'Nom': nom, 'Telephone': telephone, 'Email': email}
    contacts.append(nouveau_contact)
    sauvegarder_contacts(contacts)
    print(f"Contact '{nom}' ajouté avec succès.")

def afficher_tous_contacts(contacts):
    """Affiche tous les contacts enregistrés."""
    print("\n--- Tous les Contacts ---")
    if not contacts:
        print("Aucun contact enregistré pour le moment.")
        return

    for i, contact in enumerate(contacts, 1):
        print(f"{i}. Nom: {contact['Nom']}, Tel: {contact['Telephone']}, Email: {contact['Email']}")

def rechercher_contact(contacts):
    """Recherche un contact par nom et affiche ses détails."""
    print("\n--- Rechercher un Contact ---")
    nom_recherche = input("Entrez le nom du contact à rechercher : ").strip()

    resultats = [c for c in contacts if nom_recherche.lower() in c['Nom'].lower()]

    if not resultats:
        print(f"Aucun contact trouvé pour '{nom_recherche}'.")
        return

    print("\n--- Résultats de la Recherche ---")
    for i, contact in enumerate(resultats, 1):
        print(f"{i}. Nom: {contact['Nom']}, Tel: {contact['Telephone']}, Email: {contact['Email']}")
    return resultats  # Retourne les résultats pour faciliter la modification/suppression

def modifier_contact(contacts):
    """Modifie les informations d'un contact existant."""
    print("\n--- Modifier un Contact ---")
    nom_a_modifier = input("Entrez le nom du contact à modifier : ").strip()

    index_a_modifier = -1
    for i, contact in enumerate(contacts):
        if contact['Nom'].lower() == nom_a_modifier.lower():
            index_a_modifier = i
            break

    if index_a_modifier == -1:
        print(f"Contact '{nom_a_modifier}' non trouvé.")
        return

    contact_original = contacts[index_a_modifier]
    print(f"Contact actuel : Nom: {contact_original['Nom']}, Tel: {contact_original['Telephone']}, Email: {contact_original['Email']}")

    nouveau_nom = input(f"Nouveau nom (laissez vide pour garder '{contact_original['Nom']}') : ").strip()
    nouveau_telephone = input(f"Nouveau numéro de téléphone (laissez vide pour garder '{contact_original['Telephone']}') : ").strip()
    nouvel_email = input(f"Nouvelle adresse e-mail (laissez vide pour garder '{contact_original['Email']}') : ").strip()

    if nouveau_nom:
        # Vérifier si le nouveau nom existe déjà pour un autre contact
        if any(c['Nom'].lower() == nouveau_nom.lower() and c != contact_original for c in contacts):
            print("Erreur : Un autre contact avec ce nouveau nom existe déjà.")
            return
        contacts[index_a_modifier]['Nom'] = nouveau_nom
    if nouveau_telephone:
        contacts[index_a_modifier]['Telephone'] = nouveau_telephone
    if nouvel_email:
        contacts[index_a_modifier]['Email'] = nouvel_email

    sauvegarder_contacts(contacts)
    print(f"Contact '{nom_a_modifier}' modifié avec succès.")

def supprimer_contact(contacts):
    """Supprime un contact existant."""
    print("\n--- Supprimer un Contact ---")
    nom_a_supprimer = input("Entrez le nom du contact à supprimer : ").strip()

    index_a_supprimer = -1
    for i, contact in enumerate(contacts):
        if contact['Nom'].lower() == nom_a_supprimer.lower():
            index_a_supprimer = i
            break

    if index_a_supprimer == -1:
        print(f"Contact '{nom_a_supprimer}' non trouvé.")
        return

    confirmation = input(f"Êtes-vous sûr de vouloir supprimer '{contacts[index_a_supprimer]['Nom']}' ? (oui/non) : ").lower().strip()
    if confirmation == 'oui':
        del contacts[index_a_supprimer]
        sauvegarder_contacts(contacts)
        print(f"Contact '{nom_a_supprimer}' supprimé avec succès.")
    else:
        print("Suppression annulée.")

def main():
    """Fonction principale de l'application."""
    contacts = charger_contacts()

    while True:
        afficher_menu()
        choix = input("Choisissez une option : ").strip()

        if choix == '1':
            ajouter_contact(contacts)
        elif choix == '2':
            afficher_tous_contacts(contacts)
        elif choix == '3':
            rechercher_contact(contacts)
        elif choix == '4':
            modifier_contact(contacts)
        elif choix == '5':
            supprimer_contact(contacts)
        elif choix == '6':
            print("Merci d'avoir utilisé le Gestionnaire de Contacts. Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
