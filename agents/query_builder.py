from typing import Dict
from langchain_google_genai import ChatGoogleGenerativeAI
import os
os.environ["GOOGLE_API_KEY"] = "api_key"

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def build_query(state: Dict) -> Dict:
    user_input = state["query"]
    prompt = f"Rephrase this startup idea into a detailed founder pitch profile:\n{user_input}"
    enriched_query = llm.invoke(prompt).content
    return {"query": enriched_query}
