import requests
from utils.config import UNIPROT_API_URL

def get_protein_details(protein_name):
    url = f"{UNIPROT_API_URL}{protein_name}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        if 'results' in results and results['results']:
            first_result = results['results'][0]
            return {
                "primary_accession": first_result.get("primaryAccession"),
                "protein_name": first_result.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value"),
                "organism": first_result.get("organism", {}).get("scientificName"),
                "gene": [g['geneName']['value'] for g in first_result.get("genes", [])],
                "function": first_result.get("comments", [{}])[0].get("texts", [{}])[0].get("value", "Function info not available.")
            }
        else:
            return {"error": "Protein not found"}
    else:
        return {"error": "API request failed"}
