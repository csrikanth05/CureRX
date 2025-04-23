def get_protein_interactions(protein_name):
    return {
        "interactions": [
            {"partner": "ProteinA", "interaction_type": "binding"},
            {"partner": "ProteinB", "interaction_type": "activation"},
            {"partner": "ProteinC", "interaction_type": "inhibition"}
        ]
    }
