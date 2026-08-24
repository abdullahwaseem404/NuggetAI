import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

BASE_DIR = Path(__file__).parent
VECTORSTORE_PATH = BASE_DIR / "vectorstore"

_embeddings = None
_vectorstore = None

def get_embeddings():
    global _embeddings
    if _embeddings is None:
        _embeddings = GoogleGenerativeAIEmbeddings(
            model="text-embedding-004"
        )
    return _embeddings

def get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        if not VECTORSTORE_PATH.exists():
            raise FileNotFoundError(
                "FAISS vectorstore not found. Run training.ipynb first."
            )
        _vectorstore = FAISS.load_local(
            str(VECTORSTORE_PATH),
            get_embeddings(),
            allow_dangerous_deserialization=True
        )
    return _vectorstore

def retrieve_context(query, k=4):
    try:
        vectorstore = get_vectorstore()
        documents = vectorstore.similarity_search(query, k=k)
        return "\n\n".join(doc.page_content for doc in documents)
    except Exception as e:
        print(f"Retrieval warning: {e}")
        return "No retrieved context available."