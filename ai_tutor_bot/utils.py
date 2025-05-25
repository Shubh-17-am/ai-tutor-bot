import os
import google.generativeai as genai

def classify_intent(query: str) -> str:
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"Classify: {query}. Is it math or physics?")
        return "math" if "math" in response.text.lower() else "physics"
    except Exception as e:
        return f"Error: {str(e)}"

def query_gemini(query: str) -> str:
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"