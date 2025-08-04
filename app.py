import streamlit as st
from transcribe import transcribe_audio
from backend import generate_prescription
from supabase_utils import save_prescription

st.set_page_config(page_title="🩺 Doctor Voice to Prescription")

st.title("🩺 Doctor Voice → Medicine Prescription")

audio_file = st.file_uploader("Upload Doctor's voice (MP3/WAV)", type=["mp3", "wav"])

if audio_file:
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_file.read())
    
    st.info("🔍 Transcribing...")
    symptoms = transcribe_audio("temp_audio.wav")
    st.success("✅ Transcription Complete!")
    st.text_area("📝 Transcribed Text", symptoms, height=150)

    if st.button("Generate Prescription"):
        with st.spinner("💊 Generating Prescription..."):
            prescription = generate_prescription(symptoms)
            st.text_area("💡 Prescription Output", prescription, height=200)

            patient_name = st.text_input("Enter Patient Name to Save", key="name_input")
            if patient_name:
                save_prescription(patient_name, symptoms, prescription)
                st.success(f"Prescription saved for {patient_name}")
