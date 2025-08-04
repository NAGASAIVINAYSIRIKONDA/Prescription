from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

def generate_prescription(symptoms_text):
    chat = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

    prompt = f"""
    I am a doctor, i will give some notes, now just identfy the medicine names and list them.

    Notes:
    {symptoms_text}
    """

    messages = [HumanMessage(content=prompt)]
    result = chat.invoke(messages)
    return result.content
