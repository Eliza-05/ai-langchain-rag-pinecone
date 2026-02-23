from langchain_google_genai import ChatGoogleGenerativeAI

def get_chat_model(temperature: float = 0.2):
    
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=temperature)
