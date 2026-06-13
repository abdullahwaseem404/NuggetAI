from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings.base import Embeddings
import numpy as np

class SimpleEmbedding(Embeddings):
    def embed_documents(self, texts):
        return [np.random.rand(384).tolist() for _ in texts]

    def embed_query(self, text):
        return np.random.rand(384).tolist()

def load_knowledge():
    with open("data/knowledge.txt", "r", encoding="utf-8") as f:
        return f.read()

def create_vectorstore():
    text = load_knowledge()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_text(text)

    embedding = SimpleEmbedding()
    db = FAISS.from_texts(docs, embedding)

    return db

def retrieve_context(query):
    db = create_vectorstore()
    docs = db.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])