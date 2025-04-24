import { useState, useEffect } from 'react';
import TransitionPage from './components/TransitionPage';
import SearchPage from './components/SearchPage';

function App() {
  const [showTransition, setShowTransition] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => setShowTransition(false), 2000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="min-h-screen bg-gray-900 text-white font-sans">
      {showTransition ? <TransitionPage /> : <SearchPage />}
    </div>
  );
}

export default App;
