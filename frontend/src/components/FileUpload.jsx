import React, { useState } from "react";

export default function FileUpload({ setData }) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFile = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("audio", file);

    setError("");
    setLoading(true);

    try {
      const res = await fetch("http://localhost:5000/api/process", {
        method: "POST",
        body: formData,
      });

      const result = await res.json();
      if (res.ok) {
        setData(result);
      } else {
        setError(result.error || "Failed to process file");
      }
    } catch (err) {
      setError("Server not responding. Check backend.");
    }

    setLoading(false);
  };

  return (
    <div className="bg-white shadow-md border border-gray-200 rounded-xl p-6 text-center w-full max-w-md">
      <p className="mb-4 text-lg font-medium text-gray-700">
        Upload your audio file
      </p>

      <label className="cursor-pointer inline-block bg-blue-500 hover:bg-blue-600 text-white py-2 px-5 rounded-lg font-medium transition duration-200">
        Choose File
        <input
          type="file"
          accept="audio/*"
          onChange={handleFile}
          className="hidden"
        />
      </label>

      {loading && (
        <p className="mt-4 text-blue-500 animate-pulse">
          ⏳ Processing... Please wait
        </p>
      )}
      {error && <p className="mt-4 text-red-500">{error}</p>}
    </div>
  );
}
