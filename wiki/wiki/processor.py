from flask import Flask, request, jsonify
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)

# Load the pre-built index, including the TF-IDF vectorizer
with open("index.pickle", "rb") as f:
    index_data = pickle.load(f)

tfidf_vectorizer = index_data["tfidf_vectorizer"]  # Load the TF-IDF vectorizer
tfidf_matrix = index_data["tfidf_matrix"]
document_names = index_data["document_names"]

# Function to validate the incoming query
def validate_query(query):
    if not isinstance(query, str):
        return False, "Query must be a string."
    if len(query.strip()) == 0:
        return False, "Query cannot be empty."
    if not re.match(r"^[\w\s.,'!?-]+$", query):
        return False, "Query contains invalid characters."
    return True, ""

# Route to process text-based queries
@app.route("/query", methods=["POST"])
def process_query():
    data = request.get_json()

    # Check if the query is provided in the expected format
    if "query" not in data:
        return jsonify({"error": "Missing 'query' field in request."}), 400

    query = data["query"]
    is_valid, error_msg = validate_query(query)

    if not is_valid:
        return jsonify({"error": error_msg}), 400

    # Convert query into TF-IDF vector using the saved vectorizer
    tfidf_vector = tfidf_vectorizer.transform([query])  # Transform the incoming query

    # Calculate cosine similarity with the indexed documents
    cosine_scores = cosine_similarity(tfidf_vector, tfidf_matrix)[0]

    # Get the Top-K documents based on cosine similarity
    K = 5  # You can change this to any number for the Top-K results
    top_k_indices = np.argsort(-cosine_scores)[:K]
    top_k_results = [{"Document Name": document_names[i], "similarity": cosine_scores[i]} for i in top_k_indices]

    return jsonify({"Top 5 results": top_k_results}), 200


if __name__ == "__main__":
    app.run(debug=True)  # Running the Flask app in debug mode
