import streamlit as st
from transcribe import transcribe_audio
from backend import generate_prescription
from supabase_utils import save_prescription
import os

st.set_page_config(page_title="🩺 Doctor Voice to Prescription")

st.title("🩺 Doctor Voice → Medicine Prescription")

audio_file = st.file_uploader("Upload Doctor's voice (MP3/WAV)", type=["mp3", "wav"])

if audio_file:
    # Save uploaded file temporarily
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_file.read())
    
    st.info("🔍 Transcribing...")
    try:
        symptoms = transcribe_audio("temp_audio.wav")
        st.success("✅ Transcription Complete!")
        st.text_area("📝 Transcribed Text", symptoms, height=150)

        if st.button("Generate Prescription"):
            with st.spinner("💊 Generating Prescription..."):
                prescription = generate_prescription(symptoms)
                st.text_area("💡 Prescription Output", prescription, height=200)
                
                # Store prescription in session state
                st.session_state.prescription = prescription
                st.session_state.symptoms = symptoms

        # Show save option if prescription exists
        if 'prescription' in st.session_state:
            patient_name = st.text_input("Enter Patient Name to Save", key="name_input")
            if st.button("Save Prescription") and patient_name:
                result = save_prescription(patient_name, st.session_state.symptoms, st.session_state.prescription)
                if result:
                    st.success(f"✅ Prescription saved for {patient_name}")
                else:
                    st.error("❌ Failed to save prescription")
    
    except Exception as e:
        st.error(f"Error processing audio: {str(e)}")
    
    finally:
        # Clean up temp file
        if os.path.exists("temp_audio.wav"):
            os.remove("temp_audio.wav")
