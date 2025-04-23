import requests
from utils.config import PDB_API_URL

def get_structure(protein_code):
    url = f"{PDB_API_URL}{protein_code}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Structure not found"}
