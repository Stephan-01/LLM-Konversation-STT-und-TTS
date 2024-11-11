Speech-to-Text & ChatGPT Integration with Two TTS Models (Local & ElevenLabs)
This project enables voice-controlled conversations with a Large Language Model (LLM) such as OpenAI's GPT. Spoken language is converted into text, which is then sent to the LLM, and the LLM's response is read aloud using two different Text-to-Speech (TTS) models. There are two modes:

Local TTS Model (facebook/mms-tts): An open-source model that runs locally on your computer.
ElevenLabs TTS Model: A cloud-based advanced TTS model provided by the ElevenLabs API.
The project provides the flexibility to use either the local model or the cloud-based solution, depending on your requirements and preferences.

How It Works
Speech Recognition (Speech-to-Text): The user speaks into a microphone, and the spoken language is converted into text.
Communication with GPT: The recognized text is sent to OpenAI's GPT API, which generates a response.
Text-to-Speech (TTS): The response from GPT is converted into spoken language and read aloud using either a local model (facebook/mms-tts) or the ElevenLabs API.
Requirements
Ensure you have the following Python libraries installed:

speech_recognition (for speech recognition)
openai (for communication with OpenAI's GPT)
transformers (for the local TTS model facebook/mms-tts)
elevenlabs (for speech synthesis with ElevenLabs)
playsound (for playing the generated audio files)
You can install the required libraries with pip:

bash
Code kopieren
pip install speechrecognition openai transformers elevenlabs playsound
API Keys
OpenAI API: You need to provide your OpenAI API key to use GPT. You can set the key directly in the code or save it as an environment variable OPENAI_API_KEY.
ElevenLabs API: You also need an API key for ElevenLabs. Save this key as the environment variable ELEVENLABS_API_KEY.
Usage
Ensure that the API keys for OpenAI and ElevenLabs are correctly set.

Choose the desired TTS mode:

Local TTS Model: Uses facebook/mms-tts from the transformers library. The response from GPT is generated locally on your computer.
ElevenLabs TTS Model: Uses the ElevenLabs API to generate a more advanced speech output.
You can switch between TTS modes by modifying the code. By default, the local model is used.

Run the script to start the process:

The program will wait for you to speak into the microphone.
Your spoken words will be converted into text.
The text will be sent to the OpenAI API to generate a response.
The response will be converted into speech by the chosen TTS model and read aloud.
bash
Code kopieren
python your_script.py
Workflow
Speech Recognition: When you speak, your speech will be converted into text using the Google Speech API (via speech_recognition).
GPT Interaction: The text will be sent to the OpenAI API, which will generate a response.
Text-to-Speech (Local or ElevenLabs): The response will be converted into an audio file and played using either the local facebook/mms-tts model or the ElevenLabs API, depending on the selected TTS mode.
Local TTS Model (facebook/mms-tts)
The local model facebook/mms-tts uses the transformers library and runs on your local machine. It provides a simple and fast way to convert text into speech, but with less advanced voices compared to cloud-based solutions.

Cloud-based TTS Model (ElevenLabs)
The response from GPT can also be converted into speech using the ElevenLabs API. This allows for more natural-sounding voices with advanced features.

Example Output
After you speak, the output in the terminal might look like this:

mathematica
Code kopieren
Now you can speak...
You said: How are you?
Response from ChatGPT: I'm doing well, thank you for asking!
Audio file successfully created: response.mp3
The response will then be read aloud, depending on the chosen TTS model.

Error Handling
If no speech is detected, a message like this will appear: No speech detected. Time's up.
If the speech is not recognized, the error message will be: Google Speech Recognition could not understand the speech.
Network or API issues will result in a message like: Error fetching results from Google Speech Recognition.
License
This project is licensed under the MIT License.

Notes:
The Voice ID for ElevenLabs (here JBFqnCBsd6RMkjVDRZzb) can be changed to use a different voice. You can find more voices and their settings on the ElevenLabs platform.
You can adjust the stability and similarity boost of the voice using the parameters in VoiceSettings.
The facebook/mms-tts model is an open-source model and does not require API keys, but it runs locally and offers basic voice options.
