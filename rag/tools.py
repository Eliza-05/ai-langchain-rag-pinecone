from langchain.tools import tool
from vectorstore.pinecone_store import get_vector_store

vector_store = get_vector_store()

@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """Retrieve information to help answer a query."""
    retrieved_docs = vector_store.similarity_search(query, k=4)

    unique = []
    seen = set()
    for d in retrieved_docs:
        key = (d.metadata.get("source"), d.metadata.get("start_index"), d.page_content[:200])
        if key not in seen:
            seen.add(key)
            unique.append(d)

    serialized = "\n\n".join(
        f"Source: {doc.metadata}\nContent: {doc.page_content}"
        for doc in unique[:2]   # muestra 2 pero no duplicadas
    )

    return serialized, unique[:2]
