from langchain.agents import create_agent
from llm.gemini_chat import get_chat_model
from rag.tools import retrieve_context

def build_rag_agent():
    model = get_chat_model()
    prompt = (
        "You have access to a tool that retrieves context from a blog post. "
        "Use the tool to help answer user queries."
    )
    return create_agent(model, tools=[retrieve_context], system_prompt=prompt)
