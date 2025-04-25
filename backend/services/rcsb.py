import httpx

RCSB_GRAPHQL_URL = "https://data.rcsb.org/graphql"

# Fetch relevant PDB ID for a given gene or UniProt ID
async def get_pdb_id_for_gene(gene_name: str) -> str | None:
    url = f"https://search.rcsb.org/rcsbsearch/v2/query"
    query = {
        "query": {
            "type": "terminal",
            "service": "text",
            "parameters": {
                "value": gene_name
            }
        },
        "return_type": "entry",
        "request_options": {
            "results_verbosity": "minimal",
            "paginate": {
                "start": 0,
                "rows": 1
            }
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=query)
        data = response.json()
        if data.get("result_set"):
            return data["result_set"][0]["identifier"]  # e.g., "1GZH"
    return None

# GraphQL query to fetch detailed structure data
GRAPHQL_QUERY = """
query structure($id: String!) {
  entry(entry_id: $id) {
    rcsb_id
    struct {
      title
    }
    exptl {
      method
    }
    rcsb_accession_info {
      deposit_date
      initial_release_date
    }
    rcsb_entry_info {
      molecular_weight
      deposited_atom_count
      polymer_entity_count_protein
    }
    polymer_entities {
      rcsb_polymer_entity_container_identifiers {
        uniprot_ids
      }
      rcsb_entity_source_organism {
        scientific_name
        rcsb_gene_name {
          value
        }
      }
    }
  }
}
"""

async def get_structure_info(query: str):
    # Determine if input is PDB ID or gene name
    pdb_id = query.upper() if len(query) == 4 and query[0].isdigit() else await get_pdb_id_for_gene(query)
    if not pdb_id:
        return {"error": "PDB structure not found."}

    async with httpx.AsyncClient() as client:
        response = await client.post(
            RCSB_GRAPHQL_URL,
            json={"query": GRAPHQL_QUERY, "variables": {"id": pdb_id}},
            headers={"Content-Type": "application/json"},
        )
    if response.status_code == 200:
         entry = response.json()["data"]["entry"]
         return {
 "type": "embed",
    "pdb_id": pdb_id,
    "title": entry["struct"]["title"] if entry.get("struct") else None,
    "experimental_method": entry["exptl"][0]["method"] if entry.get("exptl") else None,
    "release_date": entry.get("rcsb_accession_info", {}).get("initial_release_date"),
    "molecular_weight": entry.get("rcsb_entry_info", {}).get("molecular_weight"),
    "atom_count": entry.get("rcsb_entry_info", {}).get("deposited_atom_count"),
    "polymer_entity_count": entry.get("rcsb_entry_info", {}).get("polymer_entity_count_protein"),
    "organism": (
        entry.get("polymer_entities", [{}])[0]
        .get("rcsb_entity_source_organism", [{}])[0]
        .get("scientific_name")
    ),
    "uniprot_ids": (
        entry.get("polymer_entities", [{}])[0]
        .get("rcsb_polymer_entity_container_identifiers", {})
        .get("uniprot_ids", [])
    )
                 }

         return {"error": "Structure data fetch failed."}
