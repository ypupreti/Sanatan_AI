Here is a complete `README.md` for your **Sanatan Dharma Offline AI Assistant** project:

---

### 🛕 Sanatan Dharma AI Assistant (Offline)

A fully offline, multilingual (Hindi + English) AI assistant that answers questions based on Sanatan Dharma scriptures uploaded in PDF format. It supports both text and voice input/output using local LLMs and document intelligence.

---

## 📁 Project Structure

```
sanatan-ai-assistant/
├── app/
│   ├── ui.py                # Voice+text UI (PySide6)
│   └── voice_interface.py   # Offline STT & TTS
├── scripts/
│   ├── process_pdfs.py      # Parse PDFs into chunks
│   ├── build_index.py       # Create FAISS vector store
│   └── query_engine.py      # RAG querying pipeline
├── data/
│   ├── pdfs/                # Input PDFs
│   ├── vector_store/        # FAISS index + metadata
├── models/
│   └── stt/                 # Vosk Hindi-English STT model
├── requirements.txt
└── setup.sh                 # Setup script to download models
```

---

## 🚀 Features

* 100% offline
* Hindi + English question answering
* LLM-based RAG pipeline
* Voice and text interface
* Works with any Sanatan Dharma scripture PDF

---

## 🧠 Requirements

* Python 3.8+
* Linux / macOS / Windows

---

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/sanatan-ai-assistant.git
   cd sanatan-ai-assistant
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run setup to download models**:

   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

---

## 🧾 Usage

1. **Place PDFs** into `data/pdfs/`
   (e.g., Bhagavad Gita, Ramcharitmanas, Vedas...)

2. **Preprocess and index documents**:

   ```bash
   python scripts/process_pdfs.py
   python scripts/build_index.py
   ```

3. **Launch the assistant GUI**:

   ```bash
   python app/ui.py
   ```

---

## 🗣️ Voice Commands

* Press **“Ask (Voice)”** to ask questions using your mic.
* Works offline using [Vosk](https://alphacephei.com/vosk) Hindi-English STT.

---

## 🤖 Local LLM Integration

The current pipeline simulates an LLM response using `echo`.
Replace the `query_local_llm()` function in `scripts/query_engine.py` to:

* Call a local `llama.cpp` model
* Use `GPT4All`, `Mistral`, or `Phi-2` via `ollama` or similar offline engine

---

## 🛠️ Future Ideas

* Add OCR support for scanned scriptures
* Sanskrit parsing and transliteration
* GUI for managing scripture sources
* Summarization and explanation mode

---

## 🙏 Credits

* [Vosk](https://alphacephei.com/vosk) for STT
* [Coqui TTS](https://github.com/coqui-ai/TTS) or pyttsx3 for TTS
* [SentenceTransformers](https://www.sbert.net/) for multilingual embeddings
* Sanatan Dharma texts and community

---

Let me know if you'd like me to include a sample PDF and output logs or convert this into a PDF for documentation.
