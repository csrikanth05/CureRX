import React from 'react';

function Viewer3D({ pdbId }) {
    if (!pdbId) return null;

    return (
        <div className="mt-4">
            <h3 className="text-lg font-semibold text-gray-800 mb-2">3D Structure Viewer</h3>
            <iframe
                src={`https://www.rcsb.org/3d-view/${pdbId}`}
                title="3D Structure Viewer"
                width="100%"
                height="500"
                frameBorder="0"
                allowFullScreen
            />
        </div>
    );
}

export default Viewer3D;
