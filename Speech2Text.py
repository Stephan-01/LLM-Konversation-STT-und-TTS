import speech_recognition as sr

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
        except sr.WaitTimeoutError:
            print("Keine Sprache erkannt. Die Zeit ist abgelaufen.")
        except sr.UnknownValueError:
            print("Google Speech Recognition konnte die Sprache nicht verstehen.")
        except sr.RequestError as e:
            print(f"Fehler beim Abrufen der Ergebnisse von Google Speech Recognition: {e}")

# Hauptfunktion
if __name__ == "__main__":
    speech_to_text_from_microphone()
