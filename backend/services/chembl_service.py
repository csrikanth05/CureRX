import requests
from urllib.parse import quote
from utils.config import CHEMBL_API_URL

import requests, urllib.parse
from utils.config import CHEMBL_API_URL


def get_chembl_target(acc: str):
    q = urllib.parse.quote(f'"{acc}"')          # "%22P04637%22"
    url = f"{CHEMBL_API_URL}/target.json?target_components.accession__exact={q}"
    r = requests.get(url, timeout=20)
    if r.status_code != 200:
        return {"error": r.status_code}
    data = r.json()
    if data["page_meta"]["total_count"] == 0:
        return {"error": "no targets"}
    return [
        {
            "target_chembl_id": t["target_chembl_id"],
            "pref_name": t.get("pref_name"),
            "organism": t.get("organism"),
            "target_type": t.get("target_type"),
        }
        for t in data["targets"]
    ]


def get_chembl_activities(target_chembl_id):
    url = f"{CHEMBL_API_URL}/activity?target_chembl_id={target_chembl_id}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        activities = []
        for activity in data.get('activities', []):
            activities.append({
                "molecule_chembl_id": activity.get('molecule_chembl_id'),
                "standard_type": activity.get('standard_type'),
                "standard_value": activity.get('standard_value'),
                "standard_units": activity.get('standard_units'),
                "activity_comment": activity.get('activity_comment')
            })
        return activities
    else:
        return {"error": "Failed to retrieve activities"}
