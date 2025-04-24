import httpx

REACTOME_SEARCH_URL = "https://reactome.org/ContentService/search/query"

async def fetch_reactome_data(gene_symbol: str):
    params = {
        "query": gene_symbol,
        "species": "Homo sapiens"
    }

    headers = {
        "Accept": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(REACTOME_SEARCH_URL, params=params, headers=headers)

    if response.status_code != 200:
        return {"error": "Reactome query failed"}

    try:
        data = response.json()
    except Exception:
        return {"error": "Failed to parse Reactome response"}

    # Fix: actual entries are in data["results"][0]["entries"]
    entries = []
    for result in data.get("results", []):
        entries.extend(result.get("entries", []))

    parsed = {
        "proteins": [],
        "pathways": [],
        "reactions": [],
        "complexes": [],
        "interactors": [],
        "other": []
    }

    for entry in entries:
        species_list = entry.get("species", [])
        if "Homo sapiens" not in species_list:
            continue

        type_ = entry.get("exactType", "").lower()
        item = {
            "name": entry.get("name", "").replace("<span class=\"highlighting\" >", "").replace("</span>", ""),
            "identifier": entry.get("stId", ""),
            "compartment": ", ".join(entry.get("compartmentNames", [])),
            "uniprot": entry.get("referenceIdentifier", ""),
            "db": entry.get("databaseName", "")
        }

        if "protein" in type_ or "geneproduct" in type_:
            parsed["proteins"].append(item)
        elif "pathway" in type_:
            parsed["pathways"].append(item)
        elif "reaction" in type_:
            parsed["reactions"].append(item)
        elif "complex" in type_:
            parsed["complexes"].append(item)
        elif "interactor" in type_:
            parsed["interactors"].append(item)
        else:
            parsed["other"].append(item)

    return parsed
