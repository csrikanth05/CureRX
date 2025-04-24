from fastapi import FastAPI
from services import uniprot_service, pdb_service, disgenet_service, chembl_service, interaction_service

app = FastAPI()

@app.get("/")
def root():
    return {"message": "BioAI Backend is live!"}

@app.get("/protein/{protein_name}")
def get_protein(protein_name: str):
    return uniprot_service.get_protein_details(protein_name)

@app.get("/structure/{protein_code}")
def get_structure(protein_code: str):
    return pdb_service.get_structure(protein_code)

@app.get("/diseases/{gene_name}")
def get_diseases(gene_name: str):
    return disgenet_service.get_disease_links(gene_name)

@app.get("/chembl/targets/{uniprot_accession}")
def get_chembl_targets(uniprot_accession: str):
    return chembl_service.get_chembl_target(uniprot_accession)

# 2. get bio‑activities (drug associations) for a specific ChEMBL target
@app.get("/chembl/activities/{target_chembl_id}")
def get_chembl_activities(target_chembl_id: str):
    return chembl_service.get_chembl_activities(target_chembl_id)


@app.get("/interactions/{protein_name}")
def get_interactions(protein_name: str):
    return interaction_service.get_protein_interactions(protein_name)

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
