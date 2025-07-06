import streamlit as st
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
from QASystem.output import generate_response
from QASystem.tts import TextToSpeech
import tempfile

st.title("🎙️💬 Voice + Text Medical Chatbot")

# 1. Text input
text_query = st.text_input("💬 Type your medical query:")

# 2. Audio recorder input
st.markdown("🎤 Or record your voice:")
audio_bytes = audio_recorder()

query = None

# 3. If audio is recorded, transcribe it
if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        audio_path = f.name

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        query = recognizer.recognize_google(audio)
        st.markdown(f"**Recognized Voice Query:** `{query}`")
    except Exception as e:
        st.error(f"❌ Failed to process audio: {e}")

# 4. If text input exists, use it (prioritize over voice)
if text_query:
    query = text_query

# 5. If a query is found, generate and speak the response
if query:
    response = generate_response(query)
    st.success(f"💡 Response: {response}")

    # Speak the response
    tts = TextToSpeech()
    tts.speak(response)
