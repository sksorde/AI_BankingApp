
import streamlit as st
import requests

st.title("Accessible AI Banking Assistant")

st.header("🎙️ Conversational Banking")
q = st.text_input("Ask about your bank account")
if st.button("Ask"):
    r = requests.get("http://localhost:8000/chat", params={"q": q})
    #st.write(r.json()["reply"])
    if r.status_code == 200:
        try:
            st.write(r.json().get("reply", "No reply returned"))
        except Exception:
            st.error("Backend returned invalid JSON")
            st.text(r.text)
    else:
        st.error(f"Backend error {r.status_code}")
        st.text(r.text)

st.header("🔐 OTP Voice Confirmation")
otp = st.text_input("Enter OTP (spoken or typed)")
if st.button("Verify OTP"):
    r = requests.post("http://localhost:8000/otp", params={"code": otp})
    st.write(r.json()["message"])

st.header("📊 Monthly Summary")
if st.button("Get Summary"):
    r = requests.get("http://localhost:8000/summary")
    st.write(r.json()["summary"])
