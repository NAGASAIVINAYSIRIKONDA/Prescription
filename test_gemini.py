#!/usr/bin/env python3
"""
Test script to verify Gemini API is working
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

def test_gemini():
    try:
        chat = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))
        
        messages = [HumanMessage(content="Say hello and confirm you're working")]
        result = chat.invoke(messages)
        
        print("✅ Gemini API is working!")
        print(f"Response: {result.content}")
        return True
    except Exception as e:
        print(f"❌ Gemini API error: {e}")
        return False

if __name__ == "__main__":
    test_gemini()
