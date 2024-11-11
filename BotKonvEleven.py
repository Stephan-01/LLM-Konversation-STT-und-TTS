import speech_recognition as sr
import os
import openai
from elevenlabs import ElevenLabs, VoiceSettings
from playsound import playsound

# Setze den OpenAI API-Schlüssel hier oder als Umgebungsvariable
openai_api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai_api_key)

# Setze den ElevenLabs API-Schlüssel hier oder als Umgebungsvariable
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")

# Überprüfen, ob die API-Schlüssel vorhanden sind
if openai_api_key is None:
    raise ValueError("Der OpenAI-API-Schlüssel wurde nicht gefunden. Bitte stelle sicher, dass die Umgebungsvariable 'OPENAI_API_KEY' gesetzt ist.")

if elevenlabs_api_key is None:
    raise ValueError("Der ElevenLabs-API-Schlüssel wurde nicht gefunden. Bitte stelle sicher, dass die Umgebungsvariable 'ELEVENLABS_API_KEY' gesetzt ist.")

# Erstelle einen ElevenLabs-Client
elevenlabs_client = ElevenLabs(api_key=elevenlabs_api_key)

# Funktion zur Spracherkennung
def speech_to_text_from_microphone():
    # Erstelle ein Recognizer-Objekt
    recognizer = sr.Recognizer()

    # Verwende das Mikrofon als Quelle
    with sr.Microphone() as source:
        print("Jetzt kannst du sprechen...")
        # Reduzieren von Rauschen
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

            # Sprachausgabe der Antwort mit ElevenLabs
            speak_with_elevenlabs(response_text)

        except sr.WaitTimeoutError:
            print("Keine Sprache erkannt. Die Zeit ist abgelaufen.")
        except sr.UnknownValueError:
            print("Google Speech Recognition konnte die Sprache nicht verstehen.")
        except sr.RequestError as e:
            print(f"Fehler beim Abrufen der Ergebnisse von Google Speech Recognition: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

# Funktion zur Sprachausgabe mit ElevenLabs und pyttsx3
def speak_with_elevenlabs(text):
    voice_id = "JBFqnCBsd6RMkjVDRZzb"  # bestimmte ID welche gesetzt wird um Stimme zu ändern

    # Konvertiere Text in Sprache mit ElevenLabs
    audio_data = elevenlabs_client.text_to_speech.convert(
        voice_id=voice_id,
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        voice_settings=VoiceSettings(
            stability=0.4,
            similarity_boost=0.3,
            style=0.5,
        ),
    )

    # Speichere die Audiodatei
    output_path = 'response.mp3'
    with open(output_path, "wb") as f:
        # Iteriere über die Chunks des Audio-Generators und schreibe sie in die Datei
        for chunk in audio_data:
            f.write(chunk)
    print(f"Audio-Datei erfolgreich erstellt: {output_path}")

    # Spiele die Audiodatei mit einem externen Audioplayer (z. B. playsound)
    playsound(output_path)

# Hauptfunktion
if __name__ == "__main__":
    speech_to_text_from_microphone()
