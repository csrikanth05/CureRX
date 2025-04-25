// src/App.jsx
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import TransitionPage from "./components/TransitionPage";
import SearchPage from "./components/SearchPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<TransitionPage />} />
        <Route path="/search" element={<SearchPage />} />
      </Routes>
    </Router>
  );
}

export default App;
