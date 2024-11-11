import speech_recognition as sr
import os
from openai import OpenAI
from transformers import pipeline
import pyttsx3

# Setze deinen OpenAI API-Schlüssel hier oder als Umgebungsvariable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Überprüfen, ob der API-Schlüssel vorhanden ist
if openai_api_key is None:
    raise ValueError("Der API-Schlüssel wurde nicht gefunden. Bitte stelle sicher, dass die Umgebungsvariable 'OPENAI_API_KEY' gesetzt ist.")

# Erstelle einen OpenAI-Client
client = OpenAI(api_key=openai_api_key)

# Initialisiere die TTS-Pipeline mit einem unterstützten Modell
pipe = pipeline("text-to-speech", model="facebook/mms-tts-eng")

# Funktion zur Spracherkennung
def speech_to_text_from_microphone():
    # Erstelle ein Recognizer-Objekt
    recognizer = sr.Recognizer()

    # Verwende das Mikrofon als Quelle
    with sr.Microphone() as source:
        print("Jetzt kannst du sprechen...")
        # Reduziere das Rauschen
        recognizer.adjust_for_ambient_noise(source)

        try:
            # Höre auf das Mikrofon und setze eine Zeitbeschränkung von 7 Sekunden
            audio = recognizer.listen(source, timeout=7)

            # Versuche, die Sprache in Text umzuwandeln
            text = recognizer.recognize_google(audio, language='de-DE')
            print("Du hast gesagt: " + text)

            # Sende den transkribierten Text an die OpenAI API
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": text}
                ]
            )

            # Ausgabe der Antwort von OpenAI
            response_text = response.choices[0].message.content
            print("Antwort von ChatGPT: " + response_text)

            # Sprachausgabe der Antwort von ChatGPT
            output_path = 'response.wav'

            # Generiere die Sprache und speichere sie als WAV-Datei
            with open(output_path, "wb") as f:
                speech = pipe(response_text)
                f.write(speech["audio"])

            # Überprüfe, ob die Datei existiert und nicht leer ist
            if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                print("Audio-Datei erfolgreich erstellt:", output_path)
            else:
                print("Audio-Datei wurde nicht erstellt oder ist leer.")

            # Initialisiere Text-to-Speech Engine für direkte Ausgabe
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)  # Geschwindigkeit
            engine.setProperty('volume', 1)  # Lautstärke (0.0 bis 1.0)
            engine.say(response_text)
            engine.runAndWait()

        except sr.WaitTimeoutError:
            print("Keine Sprache erkannt. Die Zeit ist abgelaufen.")
        except sr.UnknownValueError:
            print("Google Speech Recognition konnte die Sprache nicht verstehen.")
        except sr.RequestError as e:
            print(f"Fehler beim Abrufen der Ergebnisse von Google Speech Recognition: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

# Hauptfunktion
if __name__ == "__main__":
    speech_to_text_from_microphone()
