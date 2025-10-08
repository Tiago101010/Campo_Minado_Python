import requests

def fetch_data(endpoint, filters = {}):
    url = f"https://rickandmortyapi.com/api/{endpoint}"
    response = requests.get(url, params = filters)
    
    return response.json() if response.status_code == 200 else None

character = fetch_data("character", {"name":"Morty"})
    
if character:
    print(character)
else:
    print("failed to fetch data")