#!/usr/bin/env python3
"""
Script to test if the prescriptions table exists in Supabase
"""

from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

def test_table_exists():
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    
    supabase = create_client(supabase_url, supabase_key)
    
    try:
        # Try to select from the table
        result = supabase.table("prescriptions").select("*").limit(1).execute()
        print("✅ Prescriptions table exists and is accessible!")
        return True
    except Exception as e:
        print(f"❌ Prescriptions table doesn't exist or has issues: {e}")
        print("\n📋 To fix this, go to your Supabase dashboard:")
        print("1. Open your Supabase project dashboard")
        print("2. Go to 'SQL Editor'")
        print("3. Run this SQL command:")
        print("""
CREATE TABLE IF NOT EXISTS prescriptions (
    id BIGSERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    patient_name TEXT NOT NULL,
    symptoms TEXT,
    prescription TEXT
);
        """)
        return False

if __name__ == "__main__":
    test_table_exists()
