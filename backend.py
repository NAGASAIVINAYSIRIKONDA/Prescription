from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

def generate_prescription(symptoms_text):
    chat = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=os.getenv("GOOGLE_API_KEY"))

    prompt = f"""
    You are a professional medical assistant.
    Based on the following symptoms or spoken notes from a doctor, generate a complete prescription including:
    - Diagnosis
    - Medications (with dosage)
    - Any important instructions

    Symptoms/Notes:
    {symptoms_text}
    """

    messages = [HumanMessage(content=prompt)]
    result = chat.invoke(messages)
    return result.content
