# File: app/voice_interface.py
import sounddevice as sd
import queue
import vosk
import json
import pyttsx3

model = vosk.Model("models/stt/vosk-model-small-hi-en")
q = queue.Queue()

engine = pyttsx3.init()
engine.setProperty('rate', 140)

def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    q.put(bytes(indata))

def listen():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, 16000)
        print("Listening...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                return result.get("text", "")

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    text = listen()
    print("You said:", text)
    speak("You said " + text)


# File: app/ui.py
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel
from scripts.query_engine import search_and_answer
from app.voice_interface import listen, speak
import sys

class ChatUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sanatan Dharma AI Assistant")
        self.resize(600, 400)
        layout = QVBoxLayout()

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.input = QTextEdit()
        layout.addWidget(self.input)

        btn_text = QPushButton("Ask (Text)")
        btn_text.clicked.connect(self.handle_text_query)
        layout.addWidget(btn_text)

        btn_voice = QPushButton("Ask (Voice)")
        btn_voice.clicked.connect(self.handle_voice_query)
        layout.addWidget(btn_voice)

        self.setLayout(layout)

    def handle_text_query(self):
        query = self.input.toPlainText()
        if query:
            answer = search_and_answer(query)
            self.output.append(f"You: {query}\nAI: {answer}\n")
            speak(answer)

    def handle_voice_query(self):
        query = listen()
        self.output.append(f"You (voice): {query}")
        answer = search_and_answer(query)
        self.output.append(f"AI: {answer}\n")
        speak(answer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatUI()
    window.show()
    sys.exit(app.exec())