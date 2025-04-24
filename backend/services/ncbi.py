import httpx

async def fetch_gene_diseases(gene: str):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

    # Step 1: Search for Gene ID
    esearch_url = f"{base_url}/esearch.fcgi"
    params = {
        "db": "gene",
        "term": f"{gene}[gene] AND human[orgn]",
        "retmode": "json"
    }

    async with httpx.AsyncClient() as client:
        search_res = await client.get(esearch_url, params=params)
        if search_res.status_code != 200:
            return {"error": "NCBI search failed"}
        
        search_json = search_res.json()
        id_list = search_json.get("esearchresult", {}).get("idlist", [])
        if not id_list:
            return {"error": "Gene not found in NCBI"}

        gene_id = id_list[0]

        # Step 2: Get Gene Summary
        esummary_url = f"{base_url}/esummary.fcgi"
        summary_params = {
            "db": "gene",
            "id": gene_id,
            "retmode": "json"
        }

        summary_res = await client.get(esummary_url, params=summary_params)
        if summary_res.status_code != 200:
            return {"error": "NCBI summary fetch failed"}

        summary_json = summary_res.json()
        doc = summary_json.get("result", {}).get(gene_id, {})

        return {
            "gene": gene,
            "gene_id": gene_id,
            "summary": doc.get("summary", "No summary found."),
            "description": doc.get("description", "No description found."),
            "name": doc.get("name"),
            "organism": doc.get("organism", {}).get("scientificname")
        }
