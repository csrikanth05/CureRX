from fastapi import FastAPI
from services import uniprot_service, rcsb, ncbi, reactome_service
from services.rcsb import get_structure_info
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/protein/{name}")
async def get_protein(name: str):
    return await uniprot_service.fetch_protein_info(name)

@app.get("/diseases/{gene}")
async def get_diseases(gene: str):
    return await ncbi.fetch_gene_diseases(gene)

@app.get("/reactome/{gene}")
async def get_reactome_info(gene: str):
    return await reactome_service.fetch_reactome_data(gene)

@app.get("/all/{query}")
async def get_all_data(query: str):
    try:
        protein = await uniprot_service.fetch_protein_info(query)
        gene = protein.get("gene", [None])[0]

        structure = await rcsb.get_structure_info(query)

        diseases = await ncbi.fetch_gene_diseases(gene) if gene else {}
        reactome = await reactome_service.fetch_reactome_data(gene) if gene else {}

        # Flatten or format data for frontend display
        disease_list = [diseases["summary"]] if "summary" in diseases else []
        pathway_names = [p["name"] for p in reactome.get("pathways", [])]

        return {
            "protein": protein,
            "structure": structure,
            "diseases": disease_list,
            "reactome": pathway_names
        }
    except Exception as e:
        return {"error": str(e)}
