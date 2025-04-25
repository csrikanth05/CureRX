import React from "react";
import Viewer3D from "./Viewer3D";

function ResultDisplay({ data }) {
    if (data?.error) {
        return <p className="text-red-600 font-medium text-center">{data.error}</p>;
    }

    const protein = data?.protein || {};
    const structure = data?.structure || {};
    const diseases = data?.diseases || [];
    const pathways = data?.reactome || [];

    const is3D = structure.type === "embed";
    const hasImage = structure.type === "image";

    return (
        <div className="relative bg-white text-gray-900 p-6 rounded-lg shadow-lg max-w-4xl mx-auto mt-6 space-y-10">

            {/* 3D Viewer */}
            {is3D && structure.pdb_id && (
                <div>
                    <h3 className="text-lg font-semibold text-gray-800 mb-2">3D Structure Viewer</h3>
                    <Viewer3D pdbId={structure.pdb_id} />
                </div>
            )}

            {/* Compound Image */}
            {hasImage && structure.compound_img && (
                <div className="absolute top-4 right-4 w-40 h-40">
                    <img
                        src={structure.compound_img}
                        alt="Compound structure"
                        className="w-full h-full object-contain rounded shadow-md"
                        onError={(e) => {
                            e.target.onerror = null;
                            e.target.src = "https://via.placeholder.com/150?text=No+Image";
                        }}
                    />
                </div>
            )}

            {/* Protein Info */}
            <div>
                <h2 className="text-2xl font-bold mb-4 text-blue-800">
                    {protein.protein_name || "Protein Information"}
                </h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-base">
                    <p><strong className="text-gray-700">Accession:</strong> {protein.primary_accession}</p>
                    <p><strong className="text-gray-700">Organism:</strong> {protein.organism}</p>
                    <p><strong className="text-gray-700">Gene:</strong> {protein.gene?.join(", ")}</p>
                    <p><strong className="text-gray-700">Function:</strong> {protein.function}</p>
                </div>
            </div>

            {/* Sequence */}
            {protein.sequence && (
                <div>
                    <h3 className="text-lg font-semibold text-gray-800">Protein Sequence</h3>
                    <div className="bg-gray-100 p-4 rounded-md overflow-x-auto mt-2">
                        <pre className="whitespace-pre-wrap break-words text-sm font-mono">{protein.sequence}</pre>
                    </div>
                </div>
            )}

            {/* Structure Info */}
            <div>
                <h3 className="text-lg font-semibold text-gray-800">Structure Information</h3>
                {structure.error ? (
                    <p className="text-red-600 mt-2">{structure.error}</p>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-base mt-2">
                        {structure.title && <p><strong className="text-gray-700">Title:</strong> {structure.title}</p>}
                        {structure.experimental_method && <p><strong className="text-gray-700">Method:</strong> {structure.experimental_method}</p>}
                        {structure.release_date && <p><strong className="text-gray-700">Release Date:</strong> {structure.release_date}</p>}
                        {structure.molecular_weight && (
                            <p><strong className="text-gray-700">Molecular Weight:</strong> {structure.molecular_weight.toLocaleString()} Da</p>
                        )}
                        {structure.atom_count && (
                            <p><strong className="text-gray-700">Atom Count:</strong> {structure.atom_count.toLocaleString()}</p>
                        )}
                        {structure.polymer_entity_count && (
                            <p><strong className="text-gray-700">Protein Entity Count:</strong> {structure.polymer_entity_count}</p>
                        )}
                        {structure.organism && (
                            <p><strong className="text-gray-700">Source Organism:</strong> {structure.organism}</p>
                        )}
                        {structure.uniprot_ids?.length > 0 && (
                            <p><strong className="text-gray-700">UniProt IDs:</strong> {structure.uniprot_ids.join(", ")}</p>
                        )}
                    </div>
                )}
            </div>

            {/* Diseases */}
            {diseases.length > 0 && (
                <div>
                    <h3 className="text-lg font-semibold text-gray-800">Associated Diseases</h3>
                    <ul className="list-disc list-inside mt-2 text-base space-y-1">
                        {diseases.map((disease, index) => (
                            <li key={index}>{disease}</li>
                        ))}
                    </ul>
                </div>
            )}

            {/* Pathways */}
            {pathways.length > 0 && (
                <div>
                    <h3 className="text-lg font-semibold text-gray-800">Reactome Pathways</h3>
                    <ul className="list-disc list-inside mt-2 text-base space-y-1">
                        {pathways.map((pathway, index) => (
                            <li key={index}>{pathway}</li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}

export default ResultDisplay;
