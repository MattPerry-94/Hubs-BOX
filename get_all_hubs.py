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

def get_all_hubs():
    print("--- RÉCUPÉRATION DE TOUS LES HUBS DE L'ENTREPRISE ---")
    url = f"{BASE_URL}/hubs"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "box-version": "2025.0"
    }
    
    all_hubs = []
    marker = None
    limit = 100 # Maximum généralement autorisé par page
    
    while True:
        params = {"limit": limit}
        if marker:
            params["marker"] = marker
            
        print(f"Récupération d'une page... (Déjà trouvés : {len(all_hubs)})")
        
        try:
            response = requests.get(url, headers=headers, params=params)
            
            if response.status_code != 200:
                print(f"Erreur {response.status_code}: {response.text}")
                break
                
            data = response.json()
            entries = data.get('entries', [])
            all_hubs.extend(entries)
            
            # Gestion de la pagination (Marker-based)
            marker = data.get('next_marker')
            
            # Si pas de marker, on vérifie si on a tout récupéré (fallback offset)
            if not marker:
                break
                
        except Exception as e:
            print(f"Exception critique: {e}")
            break
            
    print(f"\n--- TERMINÉ ---")
    print(f"Total Hubs récupérés : {len(all_hubs)}")
    
    # Sauvegarde des IDs dans un fichier pour usage ultérieur
    output_file = "all_hub_ids.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for hub in all_hubs:
            name = hub.get('name') or hub.get('title') or "Sans nom"
            f.write(f"{hub['id']},{name}\n")
            
    print(f"Liste sauvegardée dans '{output_file}'")
    
    # Affichage des 10 premiers pour confirmation
    print("\nAperçu des 10 premiers Hubs :")
    for hub in all_hubs[:10]:
        name = hub.get('name') or hub.get('title') or "Sans nom"
        print(f"- {hub['id']} : {name}")

    return all_hubs

if __name__ == "__main__":
    get_all_hubs()
