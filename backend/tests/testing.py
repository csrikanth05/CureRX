from services import uniprot_service, pdb_service

def test_uniprot_service():
    result = uniprot_service.get_protein_details("P53")
    assert "primary_accession" in result

def test_pdb_service():
    result = pdb_service.get_structure("1TUP")
    assert "title" in result
