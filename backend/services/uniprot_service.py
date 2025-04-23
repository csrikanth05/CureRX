import requests
from utils.config import UNIPROT_API_URL

def get_protein_details(protein_name):
    url = f"{UNIPROT_API_URL}{protein_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Protein not found"}
