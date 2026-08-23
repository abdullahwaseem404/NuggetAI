import re
from pathlib import Path

DEFAULT_KNOWLEDGE = """
Machine learning is a field of artificial intelligence in which computers learn
patterns from data and use those patterns to make predictions or decisions.
Supervised learning uses labelled examples, while unsupervised learning finds
patterns in data without labels. A model should be evaluated on data it did not
see during training so that generalisation can be measured.

An algorithm is a finite sequence of precise steps for solving a problem. A
data structure is a way to organise data so that operations such as lookup,
insertion, and deletion can be performed efficiently. Time complexity describes
how an algorithm's running time grows as its input grows; Big O notation gives
an upper-bound description such as O(n) or O(log n).

Retrieval-augmented generation (RAG) retrieves relevant source text before
asking a language model to answer. This grounds the answer in the supplied
knowledge base and can reduce unsupported claims.

An embedding is a numerical vector that represents the meaning of text, an
image, or another object. Items with similar meanings have vectors that are
close together, which lets applications search, classify, or recommend content
by semantic similarity instead of matching exact words. In a RAG system,
document embeddings are stored in a vector database and a question embedding
is used to retrieve the most relevant documents.
""".strip()

def load_knowledge():
    knowledge_path = Path(__file__).parent / "data" / "knowledge.txt"
    if knowledge_path.exists():
        return knowledge_path.read_text(encoding="utf-8")
    return DEFAULT_KNOWLEDGE

def create_vectorstore():
    return _split_into_chunks(load_knowledge())

def retrieve_context(query):
    query_terms = set(_terms(query))
    ranked = []
    for chunk in create_vectorstore():
        chunk_terms = set(_terms(chunk))
        score = len(query_terms & chunk_terms)
        ranked.append((score, chunk))
    ranked.sort(key=lambda item: item[0], reverse=True)
    return "\n\n".join(chunk for score, chunk in ranked[:3] if score > 0) or "No matching notes found."


def _split_into_chunks(text):
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    return paragraphs or [text]


def _terms(text):
    return re.findall(r"[a-z0-9]+", text.lower())