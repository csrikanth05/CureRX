import requests
from utils.config import PDB_API_URL

def get_structure(protein_code):
    url = f"{PDB_API_URL}{protein_code}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if protein_code.lower() in data:
            entry = data[protein_code.lower()][0]
            return {
                "title": entry.get("title"),
                "experimental_method": entry.get("experimental_method"),
                "release_date": entry.get("release_date"),
                "organism": entry.get("organism_name"),
                "related_publication": entry.get("citation_title")
            }
        else:
            return {"error": "Structure not found"}
    else:
        return {"error": "API request failed"}
