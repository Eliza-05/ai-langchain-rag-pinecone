from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def split_documents(
    docs: list[Document],
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> list[Document]:
    """
    Split documents into smaller chunks for embedding + vector storage.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        add_start_index=True,
    )
    return splitter.split_documents(docs)
