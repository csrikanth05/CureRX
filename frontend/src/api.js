const BASE_URL = "http://localhost:8000";

export async function fetchProteinData(query) {
    const res = await fetch(`${BASE_URL}/protein/?query=${query}`);
    if (!res.ok) throw new Error("Failed to fetch protein data");
    return await res.json();
}

export async function fetchStructureData(query) {
    const res = await fetch(`${BASE_URL}/structure/?query=${query}`);
    if (!res.ok) throw new Error("Failed to fetch structure data");
    return await res.json();
}

export async function fetchDiseaseData(query) {
    const res = await fetch(`${BASE_URL}/diseases/?query=${query}`);
    if (!res.ok) throw new Error("Failed to fetch disease data");
    return await res.json();
}

export async function fetchReactomeData(query) {
    const res = await fetch(`${BASE_URL}/reactome/?query=${query}`);
    if (!res.ok) throw new Error("Failed to fetch pathway data");
    return await res.json();
}
