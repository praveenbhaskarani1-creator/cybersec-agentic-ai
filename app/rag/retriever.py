# RAG Retriever — pgvector cosine similarity search

# Step 1: Accept query string as input
# Step 2: Generate embedding for query using embeddings.py (AWS Bedrock Titan)
# Step 3: Run pgvector cosine similarity search against rag_chunks table
# Step 4: Filter results by similarity threshold (configurable in config.py)
# Step 5: Return top-K chunks with metadata (source, chunk_id, score)
# Step 6: Pass results to reranker.py for cross-encoder re-ranking
