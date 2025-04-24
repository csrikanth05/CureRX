import httpx

async def fetch_structure_info(pdb_id: str):
    url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id}"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        r.raise_for_status()
        data = r.json()

    return {
        "title": data.get("struct", {}).get("title"),
        "experimental_method": data.get("exptl", [{}])[0].get("method"),
        "release_date": data.get("rcsb_accession_info", {}).get("initial_release_date"),
        "viewer_embed_url": f"https://www.rcsb.org/3d-view/{pdb_id}"
    }
