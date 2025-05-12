# app/agents/retriever_agent.py

import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class RetrieverAgent:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = faiss.IndexFlatL2(384)  # 384 dims for MiniLM
        self.docs = []
        self.embeddings = None

    def ingest(self, texts):
        self.docs = texts
        self.embeddings = self.model.encode(texts)
        self.index.add(np.array(self.embeddings))

    def retrieve(self, query, top_k=3):
        query_vec = self.model.encode([query])
        D, I = self.index.search(np.array(query_vec), top_k)
        results = [self.docs[i] for i in I[0]]
        return results

# Singleton instance
retriever_agent = RetrieverAgent()

# Dummy corpus
sample_docs = [
    "TSMC beat earnings expectations with strong AI chip demand.",
    "Samsung reported a decline due to weak memory chip sales.",
    "Asian markets are mixed amid concerns over U.S. yields.",
    "China tech stocks see slight recovery after government support."
]
retriever_agent.ingest(sample_docs)
