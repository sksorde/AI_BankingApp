# voice_output.py
"""
from gtts import gTTS
import os
import streamlit as st

def speak_text(text, filename="temp_reply.mp3"):
    # Display the text for sighted users
    st.write(text)
    # Convert text to speech for visually impaired users
    tts = gTTS(text)
    tts.save(filename)
    st.audio(filename, format="audio/mp3")
    os.remove(filename)
"""

# voice_output.py
import pyttsx3
import streamlit as st

engine = pyttsx3.init()
engine.setProperty("rate", 160)  # slower, clearer speech

def speak(text):
    st.write(text)      # visible text
    engine.say(text)    # spoken audio
    engine.runAndWait()
