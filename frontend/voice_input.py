# voice_input.py
import speech_recognition as sr
import streamlit as st
from voice_output import speak

def get_voice_input(prompt_text):
    r = sr.Recognizer()

    # Speak the prompt
    speak(prompt_text)

    with sr.Microphone() as source:
        st.info("Listening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            st.success(f"You said: {text}")
            return text

        except sr.UnknownValueError:
            speak("Sorry, I could not understand. Please try again.")
            return None

        except sr.RequestError:
            speak("Speech service is unavailable.")
            return None
