import httpx
from utils.config import UNIPROT_API_URL

async def fetch_protein_info(protein_name):
    # Compose search query
    query = f"gene:{protein_name}+AND+organism_id:9606"
    url = f"{UNIPROT_API_URL}{query}&format=json&size=1"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        results = response.json()
        if 'results' in results and results['results']:
            first_result = results['results'][0]
            return {
                "primary_accession": first_result.get("primaryAccession"),
                "protein_name": first_result.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value"),
                "organism": first_result.get("organism", {}).get("scientificName"),
                "gene": [g['geneName']['value'] for g in first_result.get("genes", [])],
                "function": next((c.get("texts", [{}])[0].get("value") for c in first_result.get("comments", []) if c.get("commentType") == "FUNCTION"), "Function info not available."),
                "sequence": first_result.get("sequence", {}).get("value", "Sequence not available")
            }
        else:
            return {"error": "Protein not found"}
    else:
        return {"error": f"API request failed: {response.status_code}"}
