#!/usr/bin/env python3
"""
Script to create the prescriptions table in Supabase if it doesn't exist
"""

from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

def create_prescriptions_table():
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    
    supabase = create_client(supabase_url, supabase_key)
    
    # SQL to create the prescriptions table
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS prescriptions (
        id BIGSERIAL PRIMARY KEY,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        patient_name TEXT NOT NULL,
        symptoms TEXT,
        prescription TEXT
    );
    """
    
    try:
        result = supabase.rpc('execute_sql', {'sql': create_table_sql}).execute()
        print("✅ Prescriptions table created successfully!")
        return True
    except Exception as e:
        print(f"❌ Error creating table: {e}")
        print("Please create the table manually in your Supabase SQL editor:")
        print(create_table_sql)
        return False

if __name__ == "__main__":
    create_prescriptions_table()
