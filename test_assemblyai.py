#!/usr/bin/env python3
"""
Test script to verify AssemblyAI is working
"""

import assemblyai as aai
import os
from dotenv import load_dotenv

load_dotenv()

def test_assemblyai():
    try:
        aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
        
        # Test with a public audio URL
        transcriber = aai.Transcriber()
        audio_url = "https://assembly.ai/news.mp4"  # This is a test audio file from AssemblyAI
        
        print("Testing AssemblyAI with sample audio...")
        transcript = transcriber.transcribe(audio_url)
        
        print("✅ AssemblyAI is working!")
        print(f"Sample transcription: {transcript.text[:100]}...")
        return True
    except Exception as e:
        print(f"❌ AssemblyAI error: {e}")
        return False

if __name__ == "__main__":
    test_assemblyai()
