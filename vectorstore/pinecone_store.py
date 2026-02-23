from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from config.settings import PINECONE_API_KEY, PINECONE_INDEX
from llm.gemini_embeddings import get_embeddings

def get_vector_store():
    embeddings = get_embeddings()
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(PINECONE_INDEX)
    return PineconeVectorStore(index=index, embedding=embeddings)
