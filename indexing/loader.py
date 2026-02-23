import os
import bs4
from langchain_community.document_loaders import WebBaseLoader

DATA_PATH = os.path.join("data", "source_urls.txt")


def load_documents():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError("source_urls.txt not found in data/")


    with open(DATA_PATH, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    if not urls:
        raise ValueError("No URLs found in source_urls.txt")


    bs4_strainer = bs4.SoupStrainer(
        class_=("post-title", "post-header", "post-content")
    )

    loader = WebBaseLoader(
        web_paths=urls,
        bs_kwargs={"parse_only": bs4_strainer},
    )

    docs = loader.load()
    print(f"Loaded {len(docs)} document(s) from URLs.")

    return docs

