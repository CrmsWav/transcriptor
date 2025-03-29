from flask import Flask, request, jsonify
import whisper
import os

app = Flask(__name__)

# Charger le modèle Whisper à l'initialisation (cela peut prendre un peu de temps)
model = whisper.load_model("small")

@app.route('/transcribe', methods=['POST'])
def transcribe():
    # Vérifier que le fichier a bien été envoyé dans la requête
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    temp_path = "temp_audio.ogg"
    file.save(temp_path)

    # Transcrire l'audio
    result = model.transcribe(temp_path)
    os.remove(temp_path)  # Supprimer le fichier temporaire

    return jsonify({'text': result["text"]})

if __name__ == '__main__':
    # Railway définit la variable d'environnement PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
