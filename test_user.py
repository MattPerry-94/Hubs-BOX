import requests

# Configuration
ACCESS_TOKEN = "zIjeakEiESqCrb7WgEPLFjeC76zKuJVV"
BASE_URL = "https://api.box.com/2.0"

def get_user(user_id):
    
    url = f"{BASE_URL}/users/{user_id}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Erreur HTTP lors de la vérification de l'utilisateur : {err}")
        print(f"Statut HTTP : {err.response.status_code}")
        print(f"Réponse de l'API : {err.response.text}")
        return None


user_id = "13842609282"  
user = get_user(user_id)
if user:
    print(f"Utilisateur trouvé : {user['name']} (ID: {user['id']})")
else:
    print("Utilisateur non trouvé ou erreur d'autorisation.")
