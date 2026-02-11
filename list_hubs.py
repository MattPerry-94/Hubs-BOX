import requests
import json
import sys
import os

sys.path.append(os.getcwd())
try:
    from update_owner_hub import ACCESS_TOKEN, BASE_URL
except ImportError:
    ACCESS_TOKEN = "VOTRE_TOKEN_ICI"
    BASE_URL = "https://api.box.com/2.0"

def list_my_hubs():
    print("--- RECHERCHE DES HUBS VISIBLES ---")
    url = f"{BASE_URL}/hubs"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "box-version": "2025.0"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            hubs = response.json()
            entries = hubs.get('entries', [])
            print(f"Nombre de Hubs trouvés : {len(entries)}")
            
            # Afficher les 5 premiers pour debug
            for i, hub in enumerate(entries[:5]):
                print(f"\n--- Hub #{i+1} ---")
                print(f"ID: {hub.get('id')}")
                print(f"Type: {hub.get('type')}")
                # Essayer différents champs pour le nom
                name = hub.get('name') or hub.get('title') or "Sans nom"
                print(f"Nom: {name}")
        else:
            print(f"Erreur lors du listing: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    list_my_hubs()
