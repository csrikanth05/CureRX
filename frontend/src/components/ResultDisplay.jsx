function ResultDisplay({ data }) {
    if (data.error) {
        return <p className="text-red-500">{data.error}</p>;
    }

    return (
        <div className="bg-white text-gray-900 p-4 rounded-md shadow-md mb-6">
            <h2 className="text-xl font-bold mb-2">{data.protein_name}</h2>
            <p><strong>Accession:</strong> {data.primary_accession}</p>
            <p><strong>Organism:</strong> {data.organism}</p>
            <p><strong>Gene:</strong> {data.gene?.join(', ')}</p>
            <p><strong>Function:</strong> {data.function}</p>
            {data.sequence && (
                <div className="mt-4">
                    <h3 className="font-semibold">Sequence:</h3>
                    <pre className="whitespace-pre-wrap break-words">{data.sequence}</pre>
                </div>
            )}
        </div>
    );
}

export default ResultDisplay;
