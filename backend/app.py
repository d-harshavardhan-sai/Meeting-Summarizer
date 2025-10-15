import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import tempfile
import json
import requests
import time
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

ALLOWED_EXTENSIONS = {'mp3', 'wav', 'm4a', 'webm', 'mp4', 'mpeg'}
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024  # 25MB limit

# AssemblyAI API
ASSEMBLYAI_API_KEY = os.getenv('ASSEMBLYAI_API_KEY')
ASSEMBLYAI_UPLOAD_URL = "https://api.assemblyai.com/v2/upload"
ASSEMBLYAI_TRANSCRIPT_URL = "https://api.assemblyai.com/v2/transcript"


# ✅ Utility: Check allowed files
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ✅ Step 1: Transcribe with AssemblyAI + Speaker Labels
def transcribe_with_assemblyai(audio_file_path):
    try:
        print("Uploading file to AssemblyAI...")
        headers = {'authorization': ASSEMBLYAI_API_KEY}

        # Upload audio file
        with open(audio_file_path, 'rb') as f:
            upload_response = requests.post(
                ASSEMBLYAI_UPLOAD_URL,
                headers=headers,
                files={'file': f}
            )
        if upload_response.status_code != 200:
            raise Exception(f"Upload failed: {upload_response.text}")

        upload_url = upload_response.json()['upload_url']
        print(f"Uploaded successfully: {upload_url}")

        # Start transcription
        print("Requesting transcription...")
        transcript_request = {
            'audio_url': upload_url,
            'speaker_labels': True
        }

        response = requests.post(
            ASSEMBLYAI_TRANSCRIPT_URL,
            json=transcript_request,
            headers=headers
        )

        if response.status_code != 200:
            raise Exception(f"Transcription request failed: {response.text}")

        transcript_id = response.json()['id']
        polling_url = f"{ASSEMBLYAI_TRANSCRIPT_URL}/{transcript_id}"
        print(f"Transcription started (ID: {transcript_id})")

        # Poll until completed
        while True:
            poll_res = requests.get(polling_url, headers=headers)
            result = poll_res.json()
            status = result['status']
            print(f"Status: {status}")

            if status == 'completed':
                print("Transcription completed!")

                # ✅ Format transcript with speaker names
                speakers = result.get("utterances", [])
                if speakers:
                    transcript_text = ""
                    for s in speakers:
                        speaker_name = f"Speaker {s.get('speaker', '1')}"
                        text = s.get("text", "")
                        transcript_text += f"{speaker_name}: {text}\n"
                    return transcript_text.strip()

                # fallback
                return result.get("text", "Transcription completed but text missing.")

            elif status == 'error':
                raise Exception(f"Transcription failed: {result.get('error', 'Unknown error')}")

            time.sleep(3)

    except Exception as e:
        print(f"AssemblyAI error: {str(e)}")
        raise Exception(f"Transcription failed: {str(e)}")


# ✅ Step 2: Generate simple structured summary
def generate_summary_free(transcript):
    try:
        print("Generating summary...")

        summary = {
            "overview": extract_summary_simple(transcript),
            "keyDecisions": extract_decisions(transcript),
            "actionItems": extract_action_items(transcript),
            "participants": extract_participants(transcript),
            "duration": estimate_duration(transcript),
            "nextSteps": extract_next_steps(transcript)
        }

        return summary

    except Exception as e:
        print(f"Summary generation error: {str(e)}")
        return {
            "overview": "Meeting summary unavailable.",
            "keyDecisions": ["Unable to extract decisions."],
            "actionItems": [],
            "participants": ["Unknown"],
            "duration": "Unknown",
            "nextSteps": "Review transcript manually."
        }


# ✅ Helper functions
def extract_summary_simple(transcript):
    sentences = transcript.split('.')
    return '. '.join(sentences[:3]) + '.' if sentences else "No summary available."


def extract_decisions(transcript):
    keywords = ['decided', 'agreed', 'concluded', 'approved', 'will']
    sentences = transcript.split('.')
    decisions = [s.strip() for s in sentences if any(k in s.lower() for k in keywords)]
    return decisions[:3] if decisions else ["No clear decisions identified."]


def extract_action_items(transcript):
    keywords = ['need to', 'should', 'will', 'must', 'task', 'action']
    sentences = transcript.split('.')
    actions = []
    for s in sentences:
        if any(k in s.lower() for k in keywords):
            actions.append({
                "task": s.strip(),
                "owner": "Unassigned",
                "deadline": "TBD"
            })
            if len(actions) >= 3:
                break
    return actions


def extract_participants(transcript):
    import re
    names = re.findall(r'\b[A-Z][a-z]+\b', transcript)
    unique = list(set(names))[:5]
    return unique or ["Participant 1", "Participant 2"]


def estimate_duration(transcript):
    words = len(transcript.split())
    minutes = words / 150
    if minutes < 1:
        return "Less than 1 minute"
    elif minutes < 60:
        return f"Approximately {int(minutes)} minutes"
    else:
        return f"Approximately {minutes / 60:.1f} hours"


def extract_next_steps(transcript):
    keywords = ['next', 'follow up', 'later', 'upcoming']
    sentences = transcript.split('.')
    for s in sentences[-5:]:
        if any(k in s.lower() for k in keywords):
            return s.strip()
    return "Continue with assigned action items and schedule follow-up."


# ✅ Routes
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "assemblyai_configured": bool(ASSEMBLYAI_API_KEY)
    })


@app.route('/api/process', methods=['POST'])
def process_audio():
    print("\n=== New request received ===")

    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    file = request.files['audio']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type"}), 400

    temp_dir = tempfile.mkdtemp()
    temp_path = os.path.join(temp_dir, file.filename)

    try:
        file.save(temp_path)
        print(f"File saved to {temp_path}")

        transcript = transcribe_with_assemblyai(temp_path)
        summary = generate_summary_free(transcript)

        os.remove(temp_path)
        os.rmdir(temp_dir)

        print("=== Processing Complete ===")
        return jsonify({
            "transcript": transcript,
            "summary": summary
        })

    except Exception as e:
        print(f"Error: {str(e)}")
        try:
            if os.path.exists(temp_path):
                os.remove(temp_path)
            if os.path.exists(temp_dir):
                os.rmdir(temp_dir)
        except:
            pass
        return jsonify({"error": str(e)}), 500


# ✅ Run server
if __name__ == '__main__':
    if not ASSEMBLYAI_API_KEY:
        print("\n⚠️  Missing AssemblyAI API key! Get one free at https://www.assemblyai.com/")
    else:
        print("\n✅ AssemblyAI API Key detected.")
    print("🚀 Starting Flask server on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
