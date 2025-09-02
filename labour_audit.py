import os
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

def audit_labour_policy(user_file, reference_dir="dataset/labour"):
    user_text = extract_text_from_pdf(user_file)
    user_chunks = chunk_text(user_text)
    user_emb = embed_chunks(user_chunks)

    results = []
    for ref_file in os.listdir(reference_dir):
        if ref_file.endswith(".pdf"):
            ref_text = extract_text_from_pdf(os.path.join(reference_dir, ref_file))
            ref_chunks = chunk_text(ref_text)
            ref_emb = embed_chunks(ref_chunks)

            sim_matrix = cosine_similarity(user_emb, ref_emb)
            avg_score = np.mean(sim_matrix)

            results.append({
                "reference": ref_file,
                "similarity_score": round(float(avg_score) * 100, 2)
            })

    return results
