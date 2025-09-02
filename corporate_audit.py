import pdfplumber
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()

def chunk_text(text, chunk_size=500):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def embed_chunks(chunks):
    return embedding_model.encode(chunks, convert_to_tensor=True)

def audit_corporate_policies(file_a, file_b):
    text_a = extract_text_from_pdf(file_a)
    text_b = extract_text_from_pdf(file_b)

    chunks_a = chunk_text(text_a)
    chunks_b = chunk_text(text_b)

    emb_a = embed_chunks(chunks_a)
    emb_b = embed_chunks(chunks_b)

    sim_matrix = cosine_similarity(emb_a, emb_b)
    avg_score = np.mean(sim_matrix)

    conflicts = []
    for i, chunk_a in enumerate(chunks_a):
        sim_row = sim_matrix[i]
        max_sim = np.max(sim_row)
        if max_sim < 0.5:  # low similarity → possible conflict
            conflicts.append(chunk_a[:200])  # preview conflicting section

    return {
        "similarity_score": round(float(avg_score) * 100, 2),
        "conflicts": conflicts[:5]  # show top 5 conflicts
    }
