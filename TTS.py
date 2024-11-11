from transformers import pipeline
import os
import pyttsx3

# Initialisiere die TTS-Pipeline mit einem unterstützten Modell
pipe = pipeline("text-to-speech", model="facebook/mms-tts-eng")

# Text, der in Sprache umgewandelt wird
text = "Mir geht es sehr gut danke der nachfrage habibi"

# Generiere die Sprache und speichere sie als WAV-Datei
output_path = 'en-default.wav'

# Erstelle die Audioausgabe ohne das 'speed' Argument
with open(output_path, "wb") as f:
    speech = pipe(text)
    f.write(speech["audio"])

# Überprüfe, ob die Datei existiert und nicht leer ist
if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
    print("Audio-Datei erfolgreich erstellt:", output_path)
else:
    print("Audio-Datei wurde nicht erstellt oder ist leer.")

# Initialisiere Text-to-Speech Engine
engine = pyttsx3.init()

# Parameter für die Sprachausgabe einstellen (optional)
engine.setProperty('rate', 150)  # Geschwindigkeit
engine.setProperty('volume', 1)  # Lautstärke (0.0 bis 1.0)

# Text direkt mit pyttsx3 vorlesen
engine.say(text)
engine.runAndWait()
