# Tests — RAG pipeline

# test_embed_text_returns_vector: embed_text("test") → list of 1536 floats
# test_retriever_returns_chunks: given query → list of chunks with score > threshold
# test_reranker_improves_order: reranked results have higher relevance than raw retrieval
# test_rag_chunks_inserted: after ingestion run → rag_chunks count increases
