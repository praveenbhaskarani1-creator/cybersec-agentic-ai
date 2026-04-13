# Cross-Encoder Re-ranker — improve retrieval precision

# Step 1: Accept query + list of retrieved chunks from retriever.py
# Step 2: Load cross-encoder model (e.g. cross-encoder/ms-marco-MiniLM-L-6-v2)
# Step 3: Score each (query, chunk) pair with cross-encoder
# Step 4: Sort chunks by re-rank score descending
# Step 5: Return top-N re-ranked chunks for prompt injection
