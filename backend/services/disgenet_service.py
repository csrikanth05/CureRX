import requests
from utils.config import DISGENET_API_KEY

def get_disease_links(gene_name):
    url = f"https://www.disgenet.org/api/gda/gene/{gene_name}?source=ALL"
    headers = {"Authorization": f"Bearer {DISGENET_API_KEY}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        diseases = [{"disease_name": d["disease_name"], "score": d["score"]} for d in response.json()]
        return {"associated_diseases": diseases}
    else:
        return {"error": "Disease associations not found"}
