from supabase import create_client
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv(dotenv_path="./.env")

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    raise ValueError("Supabase credentials are missing from .env")

supabase = create_client(supabase_url, supabase_key)

def save_prescription(patient_name, symptoms, prescription_text):
    try:
        result = supabase.table("prescriptions").insert({
            "patient_name": patient_name,
            "symptoms": symptoms,
            "prescription": prescription_text
        }).execute()
        return result
    except Exception as e:
        st.error(f"Error saving to database: {str(e)}")
        print(f"Supabase error: {e}")
        return None
