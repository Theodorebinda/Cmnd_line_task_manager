import json

# Charger les tâches depuis un fichier
def charger_taches():
    try:
        with open("tasks.json", "r") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []

# Sauvegarder les tâches dans un fichier
def sauvegarder_taches(taches):
    with open("tasks.json", "w") as fichier:
        json.dump(taches, fichier, indent=4)

# Afficher les tâches
def afficher_taches(taches):
    if not taches:
        print("Aucune tâche pour le moment.")
    else:
        for i, tache in enumerate(taches):
            print(f"{i + 1}. {tache['titre']} - {tache['statut']}")
            print(f"   Description: {tache['description']}")

# Ajouter une tâche
def ajouter_tache(taches):
    titre = input("Entrez le titre de la tâche: ")
    description = input("Entrez la description de la tâche: ")
    tache = {"titre": titre, "description": description, "statut": "À faire"}
    taches.append(tache)
    print("Tâche ajoutée avec succès!")

# Modifier une tâche
def modifier_tache(taches):
    afficher_taches(taches)
    try:
        index = int(input("Entrez le numéro de la tâche à modifier: ")) - 1
        if 0 <= index < len(taches):
            print(f"Modification de la tâche: {taches[index]['titre']}")
            taches[index]["titre"] = input("Nouveau titre: ")
            taches[index]["description"] = input("Nouvelle description: ")
            taches[index]["statut"] = input("Nouveau statut (À faire/En cours/Terminé): ")
            print("Tâche modifiée avec succès!")
        else:
            print("Numéro de tâche invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

# Supprimer une tâche
def supprimer_tache(taches):
    afficher_taches(taches)
    try:
        index = int(input("Entrez le numéro de la tâche à supprimer: ")) - 1
        if 0 <= index < len(taches):
            tache_supprimee = taches.pop(index)
            print(f"Tâche '{tache_supprimee['titre']}' supprimée avec succès!")
        else:
            print("Numéro de tâche invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

# Menu principal
def menu():
    taches = charger_taches()
    while True:
        print("\n--- Gestionnaire de tâches ---")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Modifier une tâche")
        print("4. Supprimer une tâche")
        print("5. Quitter")
        choix = input("Choisissez une option: ")

        if choix == "1":
            afficher_taches(taches)
        elif choix == "2":
            ajouter_tache(taches)
        elif choix == "3":
            modifier_tache(taches)
        elif choix == "4":
            supprimer_tache(taches)
        elif choix == "5":
            sauvegarder_taches(taches)
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

# Lancer le programme
if __name__ == "__main__":
    menu()