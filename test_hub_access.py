import requests
import json

ACCESS_TOKEN = "nzP9qNoXyiJa2tbof5OtfqMLzPIXKyAm"
BASE_URL = "https://api.box.com/2.0"
HUB_ID = "749913527"

def test_get_hub_collaborations():
    print(f"--- Test GET /hub_collaborations pour Hub {HUB_ID} ---")
    url = f"{BASE_URL}/hub_collaborations"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "box-version": "2025.0"
    }
    params = {
        "hub_id": HUB_ID
    }
    
    try:
        print(f"GET {url} avec params {params}")
        response = requests.get(url, headers=headers, params=params)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print("Réponse (premiers 500 chars):")
            print(json.dumps(response.json(), indent=2)[:500])
        else:
            print(f"Erreur: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

def test_get_hub_direct():
    print(f"\n--- Test GET /hubs/{HUB_ID} ---")
    url = f"{BASE_URL}/hubs/{HUB_ID}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "box-version": "2025.0"
    }
    
    try:
        print(f"GET {url}")
        response = requests.get(url, headers=headers)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print("Réponse (premiers 500 chars):")
            print(json.dumps(response.json(), indent=2)[:500])
        else:
            print(f"Erreur: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_get_hub_direct()
    test_get_hub_collaborations()
