# Vector Store Index Types

There are several types of indexes used to build vector stores for storing and retrieving embeddings efficiently, especially in high-dimensional spaces. These indexes are optimized for Approximate Nearest Neighbor (ANN) search or exact search, depending on use cases. Here are the main types:

### 1. Flat (Brute-Force) Index
- Library: FAISS (IndexFlatL2, IndexFlatIP)
- Method: Performs exact search by computing distances to all vectors.
- Use Case: Small datasets or high accuracy needs.
- Pros: Accurate, simple.
- Cons: Slow for large datasets.

### 2. Inverted File (IVF) Index
- Library: FAISS (IndexIVFFlat, IndexIVFPQ)
- Method: Clusters the dataset and searches only within relevant clusters.
- Use Case: Medium to large datasets.
- Pros: Much faster than flat; tunable trade-off between speed and accuracy.
- Cons: Slight drop in recall.

### 3. Product Quantization (PQ)
- Library: FAISS (IndexIVFPQ, IndexPQ)
- Method: Compresses vectors into compact codes to reduce memory and improve search speed.
- Use Case: Large datasets, limited memory.
- Pros: Compact, efficient.
- Cons: Less accurate than exact search.

### 4. Hierarchical Navigable Small World (HNSW)
- Library: FAISS (IndexHNSW), hnswlib, Milvus, Weaviate
- Method: Graph-based ANN; builds a navigable small-world graph.
- Use Case: High-speed, scalable vector search.
- Pros: Very fast, good accuracy, good scalability.
- Cons: High memory usage.

It's important to validate that indexing is working and providing benefit over brute-force search. Build a ground truth by retrieving results using a Flat index (brute force).

| Metric                 | Purpose                                             |
| ---------------------- | --------------------------------------------------- |
| **Latency**            | Indexing should reduce query time                   |
| **Recall**             | How many correct docs are returned vs. ground truth |
| **Accuracy/Precision** | Particularly if using ranking or RAG                |
| **Memory Usage**       | Some indexes trade off memory for speed             |
| **Index build time**   | For large datasets, may become relevant             |
