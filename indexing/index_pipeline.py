from indexing.loader import load_documents
from indexing.splitter import split_documents
from vectorstore.pinecone_store import get_vector_store

def run_indexing():
    print("1) Loading documents...")
    docs = load_documents()

    print("2) Splitting documents...")
    splits = split_documents(docs)

    print("3) Storing in Pinecone...")
    vector_store = get_vector_store()
    vector_store.add_documents(splits)

    print("Indexing complete.")
