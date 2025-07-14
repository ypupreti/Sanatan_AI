#!/bin/bash

# Create folders
echo "📁 Creating folders..."
mkdir -p data/pdfs data/vector_store models/stt

# Download Vosk Hindi-English model
VOSK_URL="https://alphacephei.com/vosk/models/vosk-model-small-hi-en-0.22.zip"
ZIP_NAME="vosk-model-small-hi-en-0.22.zip"

if [ ! -d "models/stt/vosk-model-small-hi-en" ]; then
  echo "⬇️  Downloading Vosk Hindi-English model..."
  wget $VOSK_URL -O $ZIP_NAME

  echo "📦 Extracting model..."
  unzip -q $ZIP_NAME -d models/stt

  echo "🔁 Renaming folder..."
  mv models/stt/vosk-model-small-hi-en-0.22 models/stt/vosk-model-small-hi-en

  echo "🧹 Cleaning up..."
  rm $ZIP_NAME
else
  echo "✅ Vosk model already exists."
fi

echo "✅ Setup complete."
echo "👉 Next steps:"
echo " 1. Place your PDFs in data/pdfs/"
echo " 2. Run: python scripts/process_pdfs.py"
echo " 3. Then: python scripts/build_index.py"
echo " 4. Start the assistant: python app/ui.py"
