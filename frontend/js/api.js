const API = "http://127.0.0.1:8000";

export async function fetchJSON(path) {
    const r = await fetch(API + path); return r.json();
}
