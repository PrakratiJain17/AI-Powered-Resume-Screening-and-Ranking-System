import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(job_description, resumes, filenames):
    """Ranks resumes based on similarity to the job description using TF-IDF & Cosine Similarity."""
    if not resumes:
        return []

    # Preprocess: Remove empty resumes
    valid_resumes = [(text, name) for text, name in zip(resumes, filenames) if text.strip()]
    if not valid_resumes:
        return []

    resumes, filenames = zip(*valid_resumes)

    # Vectorization: Removes stopwords, limits features for efficiency
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    tfidf_matrix = vectorizer.fit_transform([job_description] + list(resumes))

    # Compute Cosine Similarity
    job_vector = tfidf_matrix[0]  # Job description vector
    resume_vectors = tfidf_matrix[1:]  # Resume vectors
    scores = cosine_similarity(job_vector, resume_vectors).flatten()

    # Assign ranking based on scores
    ranked_resumes = sorted(zip(filenames, scores), key=lambda x: x[1], reverse=True)
    return [{"rank": i+1, "resume": name, "score": round(score, 2)} for i, (name, score) in enumerate(ranked_resumes)]
from datetime import datetime

def save_results_to_csv(ranked_resumes, filename=None):
    """Saves ranking results as a CSV file with a timestamped filename."""
    if not ranked_resumes:
        return "No valid resumes to save."

    # Default filename with timestamp
    if not filename:
        filename = f"resume_ranking_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    df = pd.DataFrame(ranked_resumes)
    df.to_csv(filename, index=False)
    return filename
