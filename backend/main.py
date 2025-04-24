from fastapi import FastAPI
from services import uniprot_service, rcsb, ncbi, reactome_service

app = FastAPI()

@app.get("/protein/{name}")
async def get_protein(name: str):
    return await uniprot_service.fetch_protein_info(name)

@app.get("/structure/{pdb_id}")
async def get_structure(pdb_id: str):
    return await rcsb.fetch_structure_info(pdb_id)

@app.get("/diseases/{gene}")
async def get_diseases(gene: str):
    return await ncbi.fetch_gene_diseases(gene)

@app.get("/reactome/{gene}")
async def get_reactome_info(gene: str):
    return await reactome_service.fetch_reactome_data(gene)



