| **Search Type**                                 | **Description**                                              | **Common Methods**                                 | **Similarity Measure**                 | **Category**   | **Example Tools**       | **When to Use (Use Case)**                                                                                                 |
| ----------------------------------------------- | ------------------------------------------------------------ | -------------------------------------------------- | -------------------------------------- | -------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Keyword Search**<br>(Sparse Retrieval)        | Matches exact or related words using frequency-based methods | TF-IDF, BM25                                       | Term frequency, inverse document freq. | Sparse         | ElasticSearch, Lucene   | When you need **fast** results with **exact keyword matches**, like searching logs or documents by terms.                  |
| **Dense Vector Search**<br>(Semantic Retrieval) | Finds meaning-based matches using vector embeddings          | Cosine Similarity, Dot Product, Euclidean Distance | Vector similarity (meaning-based)      | Dense          | FAISS, Milvus, Pinecone | When meaning matters more than exact words—like **Q\&A systems**, **chatbots**, or **semantic search**.                    |
| **Hybrid Search**                               | Combines both keyword and dense to get relevance + meaning   | BM25 + Embeddings, Re-ranking                      | Mixed: keyword + vector similarity     | Sparse + Dense | Weaviate, Vespa, Qdrant | When you want **high accuracy**, especially in **real-world applications** where users might type synonyms or exact terms. |

#### Keyword Search
- TF-IDF (Term Frequency–Inverse Document Frequency): Scores based on how often a word appears in a document vs. across documents.
- BM25: A more advanced scoring than TF-IDF; handles longer documents better.
#### Dense Vector Search
- Cosine Similarity: Measures angle between vectors; widely used in semantic search.
- Euclidean Distance: Measures straight-line distance; less common for text.
- Dot Product: Often used in deep learning models (e.g. FAISS with inner product).
#### Hybrid Search
- Weighted Scoring: Combine BM25 score and cosine similarity score (e.g., 50/50 or tuned weights).
- Re-ranking: Use BM25 to filter top results, then re-rank them using dense vector similarity.