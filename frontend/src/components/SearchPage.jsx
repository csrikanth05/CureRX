import React, { useState } from "react";
import ResultDisplay from "./ResultDisplay";

const SearchPage = () => {
    const [query, setQuery] = useState("");
    const [results, setResults] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!query.trim()) return;

        try {
            const response = await fetch(`http://localhost:8000/all/${query}`);
            const data = await response.json();
            setResults(data);
        } catch (error) {
            console.error("Search failed", error);
        }
    };

    return (
        <div className="h-screen w-screen flex flex-col items-center justify-center bg-black text-white px-4">
            <h1 className="text-4xl font-bold mb-8 tracking-wide">Gene Holmes</h1>

            <form
                onSubmit={handleSubmit}
                className="w-full max-w-xl flex items-center justify-center gap-0 px-4"
            >
                <input
                    type="text"
                    placeholder="Enter protein/gene or PDB ID..."
                    className="flex-1 min-w-0 rounded-l-lg px-4 py-3 text-black focus:outline-none"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                />
                <button
                    type="submit"
                    className="rounded-r-lg px-6 py-3 bg-blue-600 hover:bg-blue-500 transition-colors"
                >
                    Search
                </button>
            </form>

            <div className="w-full max-w-4xl mt-12 px-4">
                {results && <ResultDisplay data={results} />}
            </div>
        </div>
    );
};

export default SearchPage;