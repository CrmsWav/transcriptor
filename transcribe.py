import sys
import whisper

if len(sys.argv) < 2:
    print("Usage: python transcribe.py <audio_file_path>")
    sys.exit(1)

audio_file = sys.argv[1]

# Charger le modèle Whisper (ici "small" pour un bon compromis)
model = whisper.load_model("small")

# Transcrire l'audio
result = model.transcribe(audio_file)
print(result["text"])
