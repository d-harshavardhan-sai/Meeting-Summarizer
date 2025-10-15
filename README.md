# 🎙️ AI Meeting Summarizer – Instant Meeting Transcripts & Summaries

<div align="center">

<!-- 🌐 Animated Architecture Diagram -->
<img width="225" height="225" alt="Image" src="https://github.com/user-attachments/assets/3a8356a9-6be8-478c-b937-f899294bd9dc" />

---

<!-- ✨ Overview Description -->
<p align="center" style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 1.2rem; color: #10B981; max-width: 600px; line-height: 1.6;">
  Convert your meeting audio into clean transcripts and concise summaries using <strong>Flask</strong>, <strong>React</strong>, and <strong>AssemblyAI</strong>. Upload audio files, get real-time transcription with speaker labels, and view structured summaries including key decisions, action items, participants, and next steps.
</p>


</div>

---







### 🚀 Features

* 🔊 Audio Upload Support: mp3, wav, m4a, webm, mp4, mpeg (≤ 25MB)
* 🧠 AI Transcription: Powered by AssemblyAI
* 🗣️ Speaker Identification included in transcripts
### 📝 Structured Summaries with:
* Overview
* Key Decisions
* Action Items
* Participants
* Meeting Duration
### Next Steps
* ⚡ Fast Processing with progress polling
* 💻 React Frontend with responsive design
* 🛡️ CORS Enabled for safe cross-origin requests
* 🔧 Lightweight Flask Backend with environment variable support



## 🛠️ Tech Stack

### 🖥️ Frontend
- ⚛️ React.js
- 🎨 Tailwind CSS
- 📦 Vite
- 🔗 Fetch API for backend requests

### 🛢️ Backend
- 🐍 Python 3
- 🍃 Flask
- 🌐 Flask-CORS
- 📦 Requests
- 🔐 Environment variables via python-dotenv
- 🔊 AssemblyAI API for transcription

### 📝 Usage
- Open the frontend in your browser.
- Upload a supported meeting audio file.
- Wait while the file is processed.
### View:
- Full transcript with speaker labels
- Structured meeting summary with key points


 
## 📸 Screenshots
### Upload Audio File
<img src="https://github.com/user-attachments/assets/d201584d-0691-4f25-9378-f6d6599457cd" width="400"/>

---

### Transcript Display
<img src="https://github.com/user-attachments/assets/a85aa21f-57ea-417c-b2ff-85f30edd4a61" width="400"/>

---

### Summary Display
<img src="https://github.com/user-attachments/assets/bbe95fef-fff2-44ad-86d4-ac4d0260d400" width="400"/>

---

### Running At Backend
<img src="https://github.com/user-attachments/assets/d073177c-2478-4248-b51b-264d9e8b4584" width="400"/>

---

### Used Assembly API Key
<img src="https://github.com/user-attachments/assets/525d9c2e-e433-4608-9198-7c36f87146d2" width="400"/>

---
### Video Demo
https://github.com/user-attachments/assets/78959836-45ec-40f8-b0dc-5bd946615d1c

---


## ⚡ Quick Start

Follow these steps to run the project locally:

```bash
# 1. Create virtual environment (recommended)
python -m venv venv
# 2. Activate environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
# 3. Install dependencies
pip install -r backend/requirements.txt
# 4. Add .env with your AssemblyAI API key
echo "ASSEMBLYAI_API_KEY=your_api_key_here" > backend/.env
# 5. Run Flask server
python backend/app.py

cd frontend
npm install
npm run dev
# Open http://localhost:5173 in your browser
```


---

## 📁 Folder Structure (Basic Overview)
``` 
MEETING_SUMMARIZER/
├── 📂 backend/                  # Flask backend
│   ├── app.py                   # Main server & API endpoints
│   ├── requirements.txt         # Python dependencies
│   └── .env                     # Environment variables (ASSEMBLYAI_API_KEY, FLASK_ENV)
│
├── 📂 frontend/                 # React frontend
│   ├── src/
│   │   ├── components/          # UI Components: FileUpload, TranscriptDisplay, SummaryDisplay
│   │   ├── App.jsx              # Root React component
│   │   ├── main.jsx             # React entry point
│   │   └── index.css / App.css  # Styles
│   ├── public/                  # Static files
│   ├── package.json             # JS dependencies
│   └── tailwind.config.js       # Tailwind configuration
│
├── README.md                    # Project documentation
└── .gitignore                   # Git ignore files

son               # 📦 Backend dependencies
└── 📄 README.md                  # 📝 Project documentation
```

---

## 📄 License
This project is currently unlicensed.  
Feel free to contact me for any questions regarding usage or contributions.

---

## 🤝 Contributing
Contributions are welcome! Please open issues or pull requests for improvements or bug fixes.

---

## 📬 Contact

<p align="center">
  Created by <strong>Harshavardhan Sai Divvala</strong> — <br/><br/>
  <a href="https://portfolio-harsha-three.vercel.app/">
    <img src="https://img.shields.io/badge/-Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" />
  </a>
  <a href="https://www.linkedin.com/in/d-harshavardhan-sai" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn" width="30" style="margin-right:10px;" />
  </a>
  <a href="https://www.instagram.com/ha_darling_ha?igsh=djhlbWp4Y2p2aTU5" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram" width="30" />
  </a>
</p>

<p align="center">
  — feel free to reach out!
</p>

 ---
