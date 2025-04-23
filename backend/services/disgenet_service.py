import requests
from utils.config import DISGENET_API_KEY

def get_disease_links(gene_name):
    url = f"https://www.disgenet.org/api/gda/gene/{gene_name}?source=ALL"
    headers = {"Authorization": f"Bearer {DISGENET_API_KEY}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "No disease associations found"}
