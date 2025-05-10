import nltk
import speech_recognition as sr
from gtts import gTTS
import os
import platform

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Function to convert audio file to text
def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text_output = recognizer.recognize_google(audio_data)
            return text_output
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results; {e}"

# Function to convert text to audio and play it
def play_audio(output_file):
    system = platform.system()
    if system == "Windows":
        os.system(f"start {output_file}")
    elif system == "Darwin":
        os.system(f"afplay {output_file}")
    elif system == "Linux":
        os.system(f"xdg-open {output_file}")

def text_to_audio(text, output_file):
    tts = gTTS(text)
    tts.save(output_file)
    play_audio(output_file)

audio_text = audio_to_text("input.wav")
print("Converted Audio to Text:", audio_text)

sample_text = "Hello, this is a conversion from text to audio using NLTK and gTTS."
output_audio_file = "output_audio.mp3"
text_to_audio(sample_text, output_audio_file)


# Output
# [nltk_data] Downloading package punkt to
# [nltk_data]     C:\Users\harsh\AppData\Roaming\nltk_data...
# [nltk_data]   Package punkt is already up-to-date!
# [nltk_data] Downloading package wordnet to
# [nltk_data]     C:\Users\harsh\AppData\Roaming\nltk_data...
# [nltk_data]   Package wordnet is already up-to-date!
# result2:
# {   'alternative': [   {   'transcript': 'the still smell of old bearings it '
#                                          'takes heat to bring out the order a '
#                                          'cold storage find with him tacos '
#                                          'Alpha store are my favourite is just '
#                                          'for food is the hard cross bun'},
#                        {   'transcript': 'the still smell of old buildings it '
#                                          'takes heat to bring out the order a '
#                                          'cold storage find with him tacos '
#                                          'Alpha store are my favourite is just '
#                                          'for food is the hard cross bun'},
#                        {   'transcript': 'the still smell of old buildings it '
#                                          'takes heat to bring out the order a '
#                                          'cold storage find with him tacos '
#                                          'Alpha store are my favourite is just '
#                                          'for food is the heart cross bun'}],
#     'final': True}
# Converted Audio to Text: the still smell of old bearings it takes heat to bring out the order a cold storage find with him tacos Alpha store are my favourite is just for food is the hard cross bun