import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import numpy as np

class Indexer:
    def __init__(self):
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english', token_pattern=r"(?u)\b[a-zA-Z]+\b")
        self.documents = []
        self.document_names = []
        self.tfidf_matrix = None
        self.cosine_similarity_matrix = None
        self.top_n_similar_documents = {}

    def add_document(self, document, document_name):
        self.documents.append(document)
        self.document_names.append(document_name)

    def build_index(self):
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.documents)
        self.cosine_similarity_matrix = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)
        self._calculate_top_n_similar_documents()

    def _calculate_top_n_similar_documents(self, n=10):
        self.top_n_similar_documents = {}
        num_documents = len(self.documents)
        for i in range(num_documents):
            document_similarity_scores = self.cosine_similarity_matrix[i]
            sorted_indices = np.argsort(-document_similarity_scores)
            top_n_documents = [(self.document_names[j], document_similarity_scores[j]) for j in sorted_indices[1:n+1]]
            self.top_n_similar_documents[self.document_names[i]] = top_n_documents

    def save_index(self, filepath):
        index_data = {
            'tfidf_vectorizer': self.tfidf_vectorizer,
            'document_names': self.document_names,
            'tfidf_matrix': self.tfidf_matrix,
            'cosine_similarity_matrix': self.cosine_similarity_matrix,
            'top_n_similar_documents': self.top_n_similar_documents
        }

        with open(filepath, 'wb') as f:
            pickle.dump(index_data, f)

    def load_index(self, filepath):
        with open(filepath, 'rb') as f:
            index_data = pickle.load(f)
            self.document_names = index_data['document_names']
            self.tfidf_matrix = index_data['tfidf_matrix']
            self.cosine_similarity_matrix = index_data['cosine_similarity_matrix']
            self.top_n_similar_documents = index_data['top_n_similar_documents']

    def print_indexes(self):
        feature_names = self.tfidf_vectorizer.get_feature_names_out()
        max_term_length = max(len(term) for term in feature_names)
        
        for j in range(len(feature_names)):
            term = feature_names[j]
            padding = ' ' * (max_term_length - len(term))
            print(f"Term: {term}{padding}")
            
            for i in range(len(self.documents)):
                if self.tfidf_matrix[i, j] != 0:
                    document_name = self.document_names[i]
                    score = self.tfidf_matrix[i, j]
                    print(f"\tDocument: {document_name}, TF-IDF score: {score}")

if __name__ == "__main__":
    indexer = Indexer()
    current_directory = os.path.dirname(__file__)
    documents_path = os.path.join(current_directory, "output")
    files = os.listdir(documents_path)

    for file in files:
        try:
            with open(os.path.join(documents_path, file), 'r', encoding='utf-8') as f:
                document = f.read()
            indexer.add_document(document, file)
        except UnicodeDecodeError:
            print(f"UnicodeDecodeError: Unable to decode file '{file}' as UTF-8. Skipping this file.")

    indexer.build_index()

    index_file = 'index.pickle'
    indexer.save_index(index_file)

    indexer.print_indexes()

    for document_name, similar_documents in indexer.top_n_similar_documents.items():
        print(f"\nTop-10 Similar Documents and Cosine similarity for {document_name}")
        for doc_name, similarity_score in similar_documents:
            print(f"\tDocument: {doc_name}, Cosine similarity: {similarity_score}")
