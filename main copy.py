import time
from listen_and_transcribe_from_vb_audio import start_continuous_listening
from screen_reader import read_screen_text
from screen_reader_multi import capture_screen_text
from ai_responder import is_screen_question, is_question, get_ai_response, get_screen_only_response, extract_clean_problem
from speak_output import speak
import threading
from config import POLLING_INTERVAL

conversation_context = []
MAX_CONTEXT_LINES = 5  # Tweak as needed
last_screen = ""

def handle_transcribed_text(text):
    global conversation_context
    try:
        # text = recognizer.recognize_google(audio)
        # print(f"\n🗣️ Heard: {text}")

        if not text.strip():
            return

        # 🧠 Add to rolling context buffer
        conversation_context.append(text.strip())
        conversation_context = conversation_context[-MAX_CONTEXT_LINES:]  # Keep last N

        full_context = "\n".join(conversation_context)

        # ❓ Use full context to decide if it's a question
        if is_question(full_context):
            print("❓ Detected as question.")
            screen_text = read_screen_text()
            screen_text = ""  # optionally keep this blank for now
            answer = get_ai_response(full_context, screen_text)
            # speak(answer)
        else:
            print("💬 Not a question. Ignoring.")

    except Exception as e:
        print(f"⚠️ Error: {e}")


def poll_screen_for_questions(): # Two-Step Prompting Pipeline
    global last_screen
    while True:
        # screen_text = read_screen_text() # Use this for Primary Monitor
        screen_text = capture_screen_text()  # Use the multi-monitor capture function
        if screen_text and screen_text != last_screen:
            cleaned_text = extract_clean_problem(screen_text) # preprocessing step using GPT itself, to remove noise

            if is_screen_question(cleaned_text):
                answer = get_screen_only_response(cleaned_text)
                # speak(answer)  # or print it
                print(f"🖥️ Screen Question Detected: {cleaned_text}")
                print(f"🤖 AI Response: {answer}")
            last_screen = cleaned_text
        time.sleep(POLLING_INTERVAL)  # Check every 5 minutes

if __name__ == "__main__":
    # Start audio listener
    stop = start_continuous_listening(handle_transcribed_text)

    # Start screen polling in background thread
    screen_thread = threading.Thread(target=poll_screen_for_questions, daemon=True)
    screen_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stop()
        print("👋 Stopped listening.")

