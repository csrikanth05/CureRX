from fastapi import FastAPI
from services import uniprot_service, pdb_service, disgenet_service, drugbank_service, interaction_service

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

@app.get("/drugs/{gene_name}")
def get_drugs(gene_name: str):
    return drugbank_service.get_drug_associations(gene_name)

@app.get("/interactions/{protein_name}")
def get_interactions(protein_name: str):
    return interaction_service.get_protein_interactions(protein_name)
