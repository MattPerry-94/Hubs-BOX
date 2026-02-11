import requests

ACCESS_TOKEN = "lDHXfTNiMzuGRXfZehqtZd2sdGIrsGXZ"
BASE_URL = "https://api.box.com/2.0"

hub_ids_and_descriptions = [
    {"id": "ID_DU_HUB_1", "description": "Description pour le Hub 1"},
    
]

def update_hub(hub_id, description):
    """Met à jour un hub avec une description."""
    url = f"{BASE_URL}/hubs/{hub_id}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "box-version": "2025.0"
    }
    
    payload = {
        "description": description
    }
    response = requests.put(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()

def update_hubs_with_descriptions():
    """Met à jour les hubs avec les descriptions spécifiées."""
    for hub in hub_ids_and_descriptions:
        hub_id = hub["id"]
        description = hub["description"]
        try:
            result = update_hub(hub_id, description)
            print(f"Hub avec ID '{hub_id}' mis à jour avec succès.")
        except requests.exceptions.HTTPError as err:
            print(f"Erreur lors de la mise à jour du Hub avec ID '{hub_id}'. Statut HTTP : {err.response.status_code}")
            print(f"Réponse de l'API : {err.response.text}")


update_hubs_with_descriptions()
