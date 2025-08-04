# 🩺 Doctor Voice to Prescription App

A Streamlit application that converts doctor's audio recordings into structured medical prescriptions using AI.

## Features

- 📤 Upload audio files (MP3/WAV)
- 🎙️ Transcribe audio using AssemblyAI
- 🤖 Generate prescriptions using Google's Gemini AI
- 💾 Store prescriptions in Supabase database

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**
   Update the `.env` file with your API keys:
   ```
   ASSEMBLYAI_API_KEY=your_assemblyai_key
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   GOOGLE_API_KEY=your_google_api_key
   ```

3. **Set up Supabase table:**
   In your Supabase SQL editor, run:
   ```sql
   CREATE TABLE IF NOT EXISTS prescriptions (
       id BIGSERIAL PRIMARY KEY,
       created_at TIMESTAMPTZ DEFAULT NOW(),
       patient_name TEXT NOT NULL,
       symptoms TEXT,
       prescription TEXT
   );
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Usage

1. Upload an audio file containing the doctor's notes
2. Wait for transcription to complete
3. Click "Generate Prescription" to create the prescription
4. Enter patient name and click "Save Prescription" to store in database

## Testing

- Test Gemini API: `python test_gemini.py`
- Test AssemblyAI: `python test_assemblyai.py`
- Test Supabase: `python test_database.py`

## API Keys

### Free APIs Used:
- **Gemini 1.5 Flash**: Free tier available at [Google AI Studio](https://aistudio.google.com/app/apikey)
- **AssemblyAI**: Free tier available at [AssemblyAI](https://www.assemblyai.com/)
- **Supabase**: Free tier available at [Supabase](https://supabase.com/)

## Files

- `app.py` - Main Streamlit application
- `backend.py` - Gemini AI integration for prescription generation
- `transcribe.py` - AssemblyAI integration for audio transcription
- `supabase_utils.py` - Supabase database operations
- `test_*.py` - Test scripts for each service
