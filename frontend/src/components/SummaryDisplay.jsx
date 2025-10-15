export default function SummaryDisplay({ summary }) {
  if (!summary) return null;

  return (
    <div className="bg-white shadow-md rounded-xl p-6 border border-gray-200 space-y-6">
      <h2 className="text-2xl font-semibold text-gray-800 mb-2">📝 Meeting Summary</h2>

      {/* Overview */}
      <section>
        <h3 className="text-lg font-medium text-blue-600 mb-1">Overview:</h3>
        <p className="text-gray-700">{summary.overview}</p>
      </section>

      {/* Key Decisions */}
      <section>
        <h3 className="text-lg font-medium text-blue-600 mb-1">Key Decisions:</h3>
        <ul className="list-disc list-inside text-gray-700">
          {summary.keyDecisions.map((d, i) => (
            <li key={i}>{d}</li>
          ))}
        </ul>
      </section>

      {/* Action Items */}
      <section>
        <h3 className="text-lg font-medium text-blue-600 mb-1">Action Items:</h3>
        {summary.actionItems.length ? (
          <ul className="list-disc list-inside text-gray-700">
            {summary.actionItems.map((a, i) => (
              <li key={i}>
                <strong>{a.task}</strong> — {a.owner} ({a.deadline})
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-gray-700">No action items found.</p>
        )}
      </section>

      {/* Participants */}
      <section>
        <h3 className="text-lg font-medium text-blue-600 mb-1">Participants:</h3>
        <p className="text-gray-700">{summary.participants.join(", ")}</p>
      </section>

      {/* Duration */}
      <section>
        <h3 className="text-lg font-medium text-blue-600 mb-1">Duration:</h3>
        <p className="text-gray-700">{summary.duration}</p>
      </section>

      {/* Next Steps */}
      <section>
        <h3 className="text-lg font-medium text-blue-600 mb-1">Next Steps:</h3>
        <p className="text-gray-700">{summary.nextSteps}</p>
      </section>
    </div>
  );
}
