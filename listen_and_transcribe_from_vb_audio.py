import speech_recognition as sr
import threading
import queue
import time

r = sr.Recognizer()
r.energy_threshold = 400
# r.pause_threshold = 1.3  # Handles short pauses better

audio_queue = queue.Queue()

def find_vb_audio_device():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if "VB-Audio" in name or "Cable Input" in name:
            return index
    return None

def listen_loop(mic):
    print("🎧 [Recorder] Started")
    while True:
        with mic as source:
            try:
                audio = r.listen(source, timeout=None)
                audio_queue.put(audio)
            except Exception as e:
                print(f"🎧 [Recorder Error]: {e}")

def process_audio_queue(callback):
    print("🧠 [Transcriber] Started")
    while True:
        audio = audio_queue.get()
        if audio is None:
            continue
        try:
            text = r.recognize_google(audio)
            print(f"🗣️ Transcribed: {text}")
            callback(text)
        except sr.UnknownValueError:
            print("🤐 Could not understand audio.")
        except Exception as e:
            print(f"⚠️ Transcriber error: {e}")

def start_continuous_listening(callback):
    device_index = find_vb_audio_device()
    if device_index is None:
        print("❌ VB-Audio Cable not found.")
        return

    mic = sr.Microphone(device_index=device_index)
    with mic as source:
        r.adjust_for_ambient_noise(source)

    # Start threads
    threading.Thread(target=listen_loop, args=(mic,), daemon=True).start()
    threading.Thread(target=process_audio_queue, args=(callback,), daemon=True).start()
