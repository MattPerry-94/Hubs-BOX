import requests

ACCESS_TOKEN = "HV0CKyR84sx2T1DoWEDF6ow1cKDwQ5Me"
BASE_URL = "https://api.box.com/2.0"

def add_hub_co_owner(hub_id, user_id):
    """
    Ajoute un utilisateur comme co-owner sur un Hub via l'endpoint Beta spécifique.
    """
    url = f"{BASE_URL}/hub_collaborations"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "box-version": "2025.0"
    }
    
    # --- METHODE VALIDÉE ---
    # 1. Endpoint: /hub_collaborations
    # 2. Clé racine: 'hub' (pas 'item')
    # 3. Type: 'hubs' (pluriel, confirmé par GET /hubs)
    payload = {
        "hub": {
            "id": hub_id,
            "type": "hubs" # Pluriel confirmé par l'API de listing
        },
        "accessible_by": {
            "type": "user",
            "id": user_id
        },
        "role": "co-owner"
    }

    print(f"Ajout User {user_id} sur Hub {hub_id}...")
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 201:
            print(f"[SUCCÈS] User {user_id} ajouté comme co-owner.")
            return response.json()
        elif response.status_code == 409:
            print(f"[INFO] User {user_id} est déjà co-owner.")
            return None
        elif response.status_code == 403:
            print(f"[ERREUR PERMISSION] Impossible d'ajouter l'utilisateur {user_id} sur le Hub {hub_id}. (403 Forbidden)")
            print("Vérifiez que vous êtes bien propriétaire ou co-propriétaire de ce Hub.")
            return None
        
        print(f"[ECHEC] Status: {response.status_code}")
        try:
            print(f"Détail erreur: {response.json()}")
        except:
            print(f"Réponse raw: {response.text}")
            
    except Exception as e:
        print(f"[EXCEPTION] {e}")

    return None

# ID mis à jour avec un ID existant trouvé (Exemple: HESS ► Nachhaltige Entwicklung 🌍)
# Remplacez par la liste complète de vos IDs si nécessaire
# hub_ids = ["750472454"]

def load_hub_ids_from_file(filename="all_hub_ids.txt"):
    """Charge les IDs de Hubs depuis un fichier texte (format: id,nom)"""
    ids = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    # On prend juste la partie avant la virgule (ID)
                    parts = line.split(',', 1)
                    if parts:
                        ids.append(parts[0].strip())
        print(f"Chargé {len(ids)} IDs de Hubs depuis {filename}")
    except FileNotFoundError:
        print(f"Erreur: Le fichier {filename} n'existe pas. Lancez d'abord get_all_hubs.py")
    return ids

user_ids = [
    "37205253320",
    "13842609282"
]  

if __name__ == "__main__":
    # Charger tous les hubs
    hub_ids = load_hub_ids_from_file()
    
    if not hub_ids:
        print("Aucun Hub à traiter.")
    else:
        print(f"Démarrage de l'ajout des co-owners pour {len(hub_ids)} hubs et {len(user_ids)} utilisateurs...")
        
        for i, hub_id in enumerate(hub_ids):
            print(f"\n--- Traitement du Hub {i+1}/{len(hub_ids)} (ID: {hub_id}) ---")
            for user_id in user_ids:
                add_hub_co_owner(hub_id, user_id)
                
        print("\n--- TRAITEMENT TERMINÉ POUR TOUS LES HUBS ---")
