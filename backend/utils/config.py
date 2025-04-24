from dotenv import load_dotenv
import os

load_dotenv()

UNIPROT_API_URL = os.getenv("UNIPROT_API_URL")
PDB_API_URL = os.getenv("PDB_API_URL")

