import time

# End-to-End
start_time = time.perf_counter()

# Embedding
emb_start = time.perf_counter()
embedding = embed_model.embed(text)
emb_end = time.perf_counter()
print(f"Embedding time: {emb_end - emb_start:.3f}s")

# Retrieval
retr_start = time.perf_counter()
docs = vector_db.search(embedding)
retr_end = time.perf_counter()
print(f"Retrieval time: {retr_end - retr_start:.3f}s")

# LLM Inference
llm_start = time.perf_counter()
response = llm.generate(docs)
llm_end = time.perf_counter()
print(f"Inference time: {llm_end - llm_start:.3f}s")

end_time = time.perf_counter()
print(f"End-to-end time: {end_time - start_time:.3f}s")
