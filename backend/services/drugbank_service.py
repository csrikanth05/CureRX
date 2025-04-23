import requests
from utils.config import DRUGBANK_API_KEY

def get_drug_associations(gene_name):
    url = f"https://api.drugbank.com/v1/targets/{gene_name}"
    headers = {"Authorization": f"Bearer {DRUGBANK_API_KEY}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "No drug associations found"}
