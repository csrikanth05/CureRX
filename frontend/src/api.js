const BASE_URL = "http://localhost:8000";

async function handleFetch(url, label) {
    try {
        const res = await fetch(url);
        if (!res.ok) {
            throw new Error(`Failed to fetch ${label}`);
        }
        return await res.json();
    } catch (error) {
        return { error: error.message };
    }
}

// src/api.js
export async function fetchProteinData(query) {
    try {
        const res = await fetch(`http://localhost:8000/all/${query}`);
        const data = await res.json();
        return data;
    } catch (error) {
        return { error: 'Failed to fetch data. Please try again.' };
    }
}

