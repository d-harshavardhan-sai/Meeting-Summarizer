import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import TranscriptDisplay from "./components/TranscriptDisplay";
import SummaryDisplay from "./components/SummaryDisplay";

export default function App() {
  const [data, setData] = useState({ transcript: "", summary: null });

  return (
    <div className="min-h-screen flex flex-col items-center px-6 py-10">
      {/* Header / Title */}
      <h1 className="text-4xl font-bold mb-6 text-gray-800 tracking-tight">
        🎙️ AI Meeting Summarizer
      </h1>
      <p className="text-gray-500 mb-10">
        Upload your meeting audio and get instant transcript & summary
      </p>

      {/* File Upload Section */}
      <FileUpload setData={setData} />

      {/* Transcript & Summary */}
      {data.transcript && (
        <div className="mt-10 w-full max-w-4xl space-y-8">
          <TranscriptDisplay text={data.transcript} />
          <SummaryDisplay summary={data.summary} />
        </div>
      )}
    </div>
  );
}
