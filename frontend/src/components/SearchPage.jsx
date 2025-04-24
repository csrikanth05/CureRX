import { useState } from 'react';
import ResultDisplay from './ResultDisplay';

function SearchPage() {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState(null);

    const handleSearch = async (e) => {
        if (e.key === 'Enter' && query.trim() !== '') {
            try {
                const response = await fetch(`http://localhost:8000/uniprot/${query}`);
                const data = await response.json();
                setResults(data);
            } catch (error) {
                setResults({ error: 'Failed to fetch data' });
            }
        }
    };

    return (
        <div className="flex flex-col items-center justify-between min-h-screen py-8">
            <h1 className="text-3xl font-semibold text-center mt-6">CureRX</h1>

            <div className="w-full max-w-xl px-4">
                {results && <ResultDisplay data={results} />}
            </div>

            <input
                type="text"
                placeholder="Search a protein (e.g. TP53)"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onKeyDown={handleSearch}
                className="mb-12 mt-8 px-4 py-3 w-4/5 sm:w-3/5 rounded-lg bg-white text-gray-800 shadow-md focus:outline-none"
            />
        </div>
    );
}

export default SearchPage;
