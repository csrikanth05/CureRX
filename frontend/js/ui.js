import { fetchJSON } from "./api.js";

const q = document.getElementById("query"),
    go = document.getElementById("go"),
    res = document.getElementById("results");

go.onclick = async () => {
    const name = q.value.trim(); if (!name) return;
    res.classList.remove("hidden");
    document.getElementById("basic").innerHTML = "<h3>Loading...</h3>";

    const basic = await fetchJSON(`/protein/${name}`);
    document.getElementById("basic").innerHTML = `
     <h3>Basics</h3>
     <p><b>Accession:</b> ${basic.primary_accession || "–"}</p>
     <p><b>Name:</b> ${basic.protein_name}</p>
     <p><b>Organism:</b> ${basic.organism}</p>
     <p><b>Genes:</b> ${basic.gene}</p>
     <p>${basic.function}</p>`;

    const str = await fetchJSON(`/structure/${basic.primary_accession?.slice(0, 4) || name}`);
    document.getElementById("structure").innerHTML = `<h3>Structure</h3><pre>${JSON.stringify(str, null, 2)}</pre>`;

    const dis = await fetchJSON(`/diseases/${name}`);
    document.getElementById("diseases").innerHTML = `<h3>Diseases</h3><pre>${JSON.stringify(dis, null, 2)}</pre>`;

    const targets = await fetchJSON(`/chembl/targets/${basic.primary_accession}`);
    document.getElementById("targets").innerHTML = `<h3>Drug Targets</h3><pre>${JSON.stringify(targets, null, 2)}</pre>`;

    if (targets[0])
        document.getElementById("activities").innerHTML =
            `<h3>Activities</h3><pre>${JSON.stringify(await fetchJSON('/chembl/activities/' + targets[0].target_chembl_id), null, 2)}</pre>`;

    const ints = await fetchJSON(`/interactions/${name}`);
    document.getElementById("interact").innerHTML = `<h3>Interactions</h3><pre>${JSON.stringify(ints, null, 2)}</pre>`;
};
