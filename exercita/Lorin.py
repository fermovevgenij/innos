from sentence_transformers import SentenceTransformer

# Initialize the SBERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Example sentences
sentences = ["This is a sentence", "This is another sentence"]

# Generate embeddings
embeddings = model.encode(sentences)
