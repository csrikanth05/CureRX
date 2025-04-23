import requests
from utils.config import DISGENET_API_KEY

def get_disease_links(gene_name):
    """
    Fetches disease associations for a given gene using DisGeNET API.
    """
    url = f"https://www.disgenet.org/api/gda/gene/{gene_name}?source=ALL"
    headers = {
        "Authorization": f"Bearer {DISGENET_API_KEY}",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": f"Failed to fetch disease associations — Status code {response.status_code}",
            "details": response.text
        }
