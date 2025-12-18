# app.py
import streamlit as st
import requests
from voice_input import get_voice_input
from voice_output import speak

st.title("Accessible AI Voice & Vision Banking Assistant")

# -----------------------------
# Conversational Banking
# -----------------------------
st.header("🎙️ Conversational Banking")

if st.button("Ask Banking Question"):
    question = get_voice_input(
        "Please ask your banking question after the beep."
    )

    if question:
        r = requests.get("http://localhost:8000/chat", params={"q": question})
        if r.status_code == 200:
            reply = r.json().get("reply", "No reply available")
            speak(reply)
        else:
            speak("Sorry, there was an error connecting to the bank server.")

# -----------------------------
# OTP Voice Confirmation
# -----------------------------
st.header("🔐 OTP Voice Confirmation")

if st.button("Verify OTP by Voice"):
    otp = get_voice_input(
        "Please speak your one time password digit by digit."
    )

    if otp:
        r = requests.post("http://localhost:8000/otp", params={"code": otp})
        if r.status_code == 200:
            speak(r.json().get("message", "OTP processed"))
        else:
            speak("OTP verification failed.")

# -----------------------------
# Monthly Summary
# -----------------------------
st.header("📊 Monthly Summary")

if st.button("Get Monthly Summary"):
    speak("Fetching your monthly transaction summary.")

    r = requests.get("http://localhost:8000/summary")
    if r.status_code == 200:
        summary = r.json().get("summary", "")
        speak(summary)
    else:
        speak("Unable to retrieve summary at this time.")
