from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt, ModelRequest

from llm.gemini_chat import get_chat_model
from vectorstore.pinecone_store import get_vector_store


def build_rag_chain():
    """
    Single-call RAG chain (no tools): always retrieves context and injects it
    into the system prompt for one model call.
    """
    model = get_chat_model()
    vector_store = get_vector_store()

    @dynamic_prompt
    def prompt_with_context(request: ModelRequest) -> str:
        last_query = request.state["messages"][-1].text
        retrieved_docs = vector_store.similarity_search(last_query, k=3)

        docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

        system_message = (
            "You are a helpful assistant. Use the following context to answer.\n\n"
            f"{docs_content}"
        )
        return system_message

    agent = create_agent(model, tools=[], middleware=[prompt_with_context])
    return agent
