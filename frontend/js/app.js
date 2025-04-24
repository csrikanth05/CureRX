const API = "http://127.0.0.1:8000";

/* helper that never throws */
async function safe(path) {
    try {
        const r = await fetch(API + path);
        return await r.json();
    } catch (err) {
        return { error: err.message };
    }
}

const q = document.getElementById("query");
const go = document.getElementById("go");
const res = document.getElementById("results");

go.addEventListener("click", runSearch);
q.addEventListener("keypress", e => e.key === "Enter" && runSearch());

function render(id, title, data) {
    document.getElementById(id).innerHTML =
        `<h3>${title}</h3><pre>${JSON.stringify(data, null, 2)}</pre>`;
}

async function runSearch() {
    const name = q.value.trim(); if (!name) return;
    res.classList.remove("hidden");

    const basic = await safe(`/protein/${name}`);
    render("basic", "Basics", basic);

    /* try first PDB hit from UniProt cross‑refs instead */
    let pdb = basic?.xrefs?.PDB?.[0] || "";   // if you store those later
    if (!pdb) pdb = name.slice(0, 4);           // fallback
    render("structure", "Structure", await safe(`/structure/${pdb}`));

    render("diseases", "Diseases", await safe(`/diseases/${name}`));

    const targets = await safe(`/chembl/targets/${basic.primary_accession}`);
    render("targets", "Drug Targets", targets);

    if (Array.isArray(targets) && targets.length) {
        render("activities", "Activities",
            await safe(`/chembl/activities/${targets[0].target_chembl_id}`));
    } else render("activities", "Activities", "—");

    render("interact", "Interactions", await safe(`/interactions/${name}`));
}