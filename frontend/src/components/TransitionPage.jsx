// src/components/TransitionPage.jsx
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";


const TransitionPage = () => {
  const navigate = useNavigate();
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    setVisible(true);

    const timer = setTimeout(() => {
      navigate("/search");
    }, 2000);

    return () => clearTimeout(timer);
  }, [navigate]);

  return (
    <div className="w-screen h-screen flex items-center justify-center">
      <div className={`flex flex-col items-center justify-center transition-opacity duration-1000 ${visible ? "opacity-100" : "opacity-0"
        } bg-gradient-to-br from-black via-blue-900 to-black w-full h-full`}>
        <h1 className="text-white text-6xl font-extrabold tracking-wide">GENE HOLMES</h1>
        <p className="text-gray-300 text-xl mt-4 tracking-widest">BY CURERX</p>
      </div>
    </div>

  );
};

export default TransitionPage;
