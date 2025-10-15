export default function TranscriptDisplay({ text }) {
  return (
    <div className="bg-white shadow-md rounded-xl p-6 border border-gray-200">
      <h2 className="text-2xl font-semibold mb-4 text-gray-800">🗣️ Transcript</h2>
      <div className="text-gray-700 leading-relaxed whitespace-pre-wrap max-h-96 overflow-y-auto">
        {text}
      </div>
    </div>
  );
}
