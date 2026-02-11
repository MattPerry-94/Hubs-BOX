import requests


ACCESS_TOKEN = "zIjeakEiESqCrb7WgEPLFjeC76zKuJVV"  
BASE_URL = "https://api.box.com/2.0"

def test_token():
    
    url = f"{BASE_URL}/users/me"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "box-version": "2025.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Jeton valide. Informations de l'utilisateur :")
        print(response.json())
    else:
        print(f"Erreur lors de la validation du jeton. Statut HTTP : {response.status_code}")
        print(f"Réponse de l'API : {response.text}")


test_token()
