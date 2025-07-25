Gestionnaire de Contacts Simple

Ce projet est une application console simple pour gérer une liste de contacts. Il vous permet d'ajouter, d'afficher, de rechercher, de modifier et de supprimer des contacts, avec une persistance des données dans un fichier CSV.

Fonctionnalités

Ajouter un contact : Enregistrez de nouveaux contacts avec leur nom, numéro de téléphone et adresse e-mail.
    
Afficher tous les contacts : Affichez la liste complète de tous les contacts enregistrés.

Rechercher un contact : Trouvez un contact spécifique par son nom (recherche partielle et insensible à la casse).

Modifier un contact : Mettez à jour les informations d'un contact existant.

Supprimer un contact : Supprimez définitivement un contact de la liste.

Persistance des données : Toutes les données de contact sont stockées dans un fichier CSV, assurant qu'elles ne sont pas perdues lorsque l'application est fermée.

Technologies Utilisées

Python 3

Module csv : Pour la lecture et l'écriture de fichiers CSV.

Module os : Pour les opérations de système de fichiers (vérification de l'existence du fichier).

Comment Utiliser

Prérequis

Assurez-vous d'avoir Python 3 installé sur votre système.

Installation

Clonez le dépôt (ou copiez le code dans un fichier) :

Si vous avez cloné le dépôt :

Bash

    git clone <URL_DU_DEPOT>
    
    cd gestionnaire-contacts-simple

Si vous avez copié le code, enregistrez-le dans un fichier nommé contact_manager.py.

Exécution

Ouvrez votre terminal ou invite de commande.

Naviguez jusqu'au répertoire où se trouve le fichier contact_manager.py.

Exécutez l'application en utilisant la commande suivante :

Bash

    python contact_manager.py

Utilisation de l'Application

Une fois l'application lancée, un menu s'affichera dans la console. Suivez les instructions pour interagir avec le gestionnaire de contacts :

    --- Gestionnaire de Contacts ---
    1. Ajouter un contact
    2. Afficher tous les contacts
    3. Rechercher un contact
    4. Modifier un contact
    5. Supprimer un contact
    6. Quitter
    -------------------------------
    Choisissez une option :

Entrez le numéro correspondant à l'option que vous souhaitez exécuter et appuyez sur Entrée.

Le fichier contacts.csv sera créé automatiquement dans le même répertoire que le script la première fois que vous ajoutez un contact.

Structure du Projet

Le projet est contenu dans un seul fichier Python :

contact_manager.py : Contient toute la logique de l'application, y compris la gestion des contacts et l'interaction avec le fichier CSV.

contacts.csv : (Généré automatiquement) Le fichier où les données de contact sont stockées.

Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, n'hésitez pas à :

"Fork" le dépôt.

Créer une nouvelle branche (git checkout -b feature/nouvelle-fonctionnalite).

Effectuer vos modifications.

"Commit" vos modifications (git commit -m 'Ajouter une nouvelle fonctionnalité').

"Push" vers la branche (git push origin feature/nouvelle-fonctionnalite).

Ouvrir une "Pull Request".

Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails (si applicable).

