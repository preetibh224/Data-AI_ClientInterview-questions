# 1. Static Embeddings

**Definition**: 
Each word or token has a fixed vector, regardless of the sentence or context it's used in.

**Examples**: Word2Vec, GloVe, FastText.

**How it works**: 
These embeddings are learned by analyzing large corpora and capturing co-occurrence or context window statistics. Once learned, a word like "bank" will always map to the same vector, no matter where it appears.

#### Example:
**Sentences**:
- "I deposited money in the bank."
- "We sat by the river bank."

**Static Embedding Output**:
Both instances of the word "bank" will have the same embedding vector, even though the meaning is different in each sentence.

**Result**:
Cannot distinguish between different meanings of polysemous words (words with multiple meanings).

# 2. Contextual Embeddings

**Definition**:
Each token's vector is generated based on the surrounding words, so the same word gets different vectors in different contexts.

**Examples**: BERT, GPT, RoBERTa, ELMo.

**How it works**: 
The model looks at the entire sentence (or surrounding tokens) and creates a vector that captures the meaning of the word in that specific context.

#### Example:
**Sentences**:
- "I deposited money in the bank."
- "We sat by the river bank."

**Contextual Embedding Output**:
- In the first sentence, "bank" will have an embedding vector similar to "ATM", "finance", etc.
- In the second sentence, "bank" will be closer in vector space to "river", "shore", etc.

**Result**:
Contextual models can disambiguate meaning and produce more nuanced embeddings.