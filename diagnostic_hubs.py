import requests
import json
import sys
import os

# Ajouter le chemin courant au path pour importer les variables
sys.path.append(os.getcwd())

try:
    from update_owner_hub import ACCESS_TOKEN, BASE_URL
except ImportError:
    print("Erreur: Impossible d'importer ACCESS_TOKEN depuis update_owner_hub.py")
    # Valeur de repli si l'import échoue (à remplacer manuellement si besoin)
    ACCESS_TOKEN = "VOTRE_TOKEN_ICI" 
    BASE_URL = "https://api.box.com/2.0"

HUB_ID = "749913527"

def diagnose_hub():
    print(f"--- DIAGNOSTIC DU HUB {HUB_ID} ---")
    url = f"{BASE_URL}/hubs/{HUB_ID}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "box-version": "2025.0"
    }
    
    print(f"GET {url}")
    try:
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("\n[SUCCÈS] Le Hub est visible.")
            print(f"Type officiel retourné par l'API: '{data.get('type')}'")
            print("Voici la structure partielle du Hub:")
            print(json.dumps(data, indent=2)[:500]) # Affiche le début du JSON
        else:
            print("\n[ECHEC] Le Hub n'est pas accessible.")
            print(f"Réponse: {response.text}")
            print("\nCauses possibles :")
            print("1. Le Hub ID est incorrect.")
            print("2. Ce Token n'appartient pas au créateur du Hub (ou admin).")
            print("3. Le scope du Token ne permet pas de voir les Hubs.")

    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    diagnose_hub()
