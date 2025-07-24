
# 🎙️ AI Interview Assistant

An AI-powered assistant designed to **listen to interview questions**, **analyze your screen**, and **generate accurate responses** during technical interviews in real-time.

---

## 🚀 Features

- **Voice Transcription**  
  Continuously listens to your microphone (or virtual audio cable) and transcribes questions.

- **Screen Question Detection**  
  Automatically captures visible text on the screen, cleans up OCR noise, and detects coding problems.

- **AI-Powered Responses**  
  Uses OpenAI's GPT models to generate **concise, high-quality answers** in real time.

- **Hotkeys for Full Control**  
  - `Ctrl + Alt + A` → Toggle **audio listening** ON/OFF.  
  - `Ctrl + Alt + S` → Toggle **screen reader** ON/OFF.

- **Two-Step Prompting Pipeline**  
  Cleans raw screen text using GPT before passing it to the AI responder for better accuracy.

- **Readable Console Output**  
  Logs answers clearly for easy reference.

---

## 🛠️ Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/ai-interview-assistant.git
cd ai-interview-assistant
```

### **2. Create Virtual Environment**
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Edit the **`config.py`** file:

```python
POLLING_INTERVAL = 5  # seconds between screen checks
```

Add your **OpenAI API key** in the appropriate module (e.g., `ai_responder.py`).

---

## ▶️ Usage

Run the assistant:

```bash
python main.py
```

- Press **`Ctrl + Alt + A`** to enable/disable audio transcription.  
- Press **`Ctrl + Alt + S`** to enable/disable screen question detection.

---

## 📂 Project Structure

```
ai_interview_assistant/
│
├── main.py                      # Entry point
├── ai_responder.py              # AI logic (GPT)
├── screen_reader.py             # Single monitor capture
├── screen_reader_multi.py       # Multi-monitor capture
├── listen_and_transcribe_from_vb_audio.py  # Audio listener
├── speak_output.py              # (Optional) TTS module
├── config.py                    # Configurations
├── requirements.txt             # Dependencies
└── README.md                    # Documentation
```

---

## 🧠 How It Works

1. **Audio Pipeline:**  
   - Listens to microphone input.
   - Detects questions using AI.
   - Sends them to GPT for answers.

2. **Screen Pipeline:**  
   - Captures your screen periodically.
   - Cleans up noisy OCR text using GPT.
   - Checks if the text is a coding question.
   - Generates a JavaScript solution (or other relevant answers).

---

## ⚡ Hotkeys

| Hotkey            | Action                 |
|-------------------|------------------------|
| **Ctrl + Alt + A**| Toggle Audio Listening |
| **Ctrl + Alt + S**| Toggle Screen Reader   |

---

## 📝 TODO / Improvements
- Add system tray notifications for AI responses.
- Log AI responses to a **timestamped file**.
- Provide GUI for toggling features.

---

## 📜 License

MIT License © 2025 [Your Name]


## Project Flow

The system operates in the following steps:

1. **Audio Listening & Transcription**  
   - Uses `listen_and_transcribe_from_vb_audio.py` to continuously capture system audio or microphone input.
   - The transcribed text is passed to `handle_transcribed_text()` in `main.py`.

2. **Question Detection**  
   - The `is_question()` function (from `ai_responder.py`) checks if the transcribed text is a question.
   - If true, the question is passed to the AI response generator.

3. **Screen Reading**  
   - `screen_reader_multi.py` (or `screen_reader.py` for single monitor) captures text from the screen.
   - The captured OCR text is cleaned via `extract_clean_problem()` to remove formatting noise.

4. **AI Response Generation**  
   - `get_ai_response()` or `get_screen_only_response()` uses OpenAI's GPT models to generate precise answers or code solutions.
   - The response is printed to the console (or can be spoken via `speak_output.py`).

5. **Hotkeys for Control**  
   - Press `Ctrl+Alt+A` to toggle audio listening on/off.
   - Press `Ctrl+Alt+S` to toggle screen reading on/off.

6. **Logging**  
   - All interactions (questions, answers, and errors) are logged for debugging and review.



1. Open command prompt and navigate to the project directory.
2. Run command python -m venv venv, this will create the Cirtual Environment and a folder called venv containing a clean python environment.
3. Actiavet the Virtual Environment by running command venv\Scripts\activate 
 Activate the Virtual Environment
🪟 On Windows (Command Prompt):
venv\Scripts\activate
🪟 On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
If PowerShell gives a permissions error, run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
4. Install dependencies, pip install -r requirements.txt
5. pip freeze > requirements.txt (If no requirements file found)
6. Deactivate when done. Run command deactivate
