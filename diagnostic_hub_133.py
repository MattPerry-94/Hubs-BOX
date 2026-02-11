import requests

ACCESS_TOKEN = "HV0CKyR84sx2T1DoWEDF6ow1cKDwQ5Me"
BASE_URL = "https://api.box.com/2.0"
HUB_ID = "713649203"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "box-version": "2025.0"
}

def check_hub_details():
    print(f"--- Diagnostic du Hub {HUB_ID} ---")
    
    # 1. Obtenir les infos du Hub
    url_hub = f"{BASE_URL}/hubs/{HUB_ID}"
    print(f"GET {url_hub}")
    response = requests.get(url_hub, headers=headers)
    
    if response.status_code == 200:
        hub = response.json()
        print(f"[OK] Hub trouvé: {hub.get('name')}")
        print(f"Created by: {hub.get('created_by')}")
        print(f"Owned by: {hub.get('owned_by')}")
    else:
        print(f"[ERREUR] Impossible de lire le Hub: {response.status_code}")
        print(response.text)

    # 2. Obtenir les collaborations du Hub
    url_collab = f"{BASE_URL}/hubs/{HUB_ID}/collaborations"
    print(f"\nGET {url_collab}")
    response_collab = requests.get(url_collab, headers=headers)
    
    if response_collab.status_code == 200:
        collabs = response_collab.json()
        print(f"[OK] {collabs.get('total_count')} collaborations trouvées.")
        for entry in collabs.get('entries', []):
            role = entry.get('role')
            user = entry.get('accessible_by', {})
            name = user.get('name', 'Unknown')
            email = user.get('login', 'Unknown')
            print(f"- {name} ({email}): {role}")
    else:
        print(f"[ERREUR] Impossible de lire les collaborations: {response_collab.status_code}")
        print(response_collab.text)

if __name__ == "__main__":
    check_hub_details()
