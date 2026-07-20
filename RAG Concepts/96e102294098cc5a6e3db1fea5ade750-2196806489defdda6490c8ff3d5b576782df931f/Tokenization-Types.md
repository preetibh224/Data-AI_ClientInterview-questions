# Types of Tokenization in LLM

In the context of Large Language Models (LLMs), tokenization is the process of breaking down text into smaller units (tokens) that the model can understand and process. There are several types of tokenization used in LLMs, depending on the model architecture and training strategy. Here are the main types:

## 1. Word-Level Tokenization
- Description: Splits text into individual words.
- Example: "I love cats" → ["I", "love", "cats"]
- Pros: Simple and intuitive.
- Cons: Large vocabulary size; struggles with rare or unknown words (out-of-vocabulary problem).

## 2. Character-Level Tokenization
- Description: Splits text into individual characters.
- Example: "I love cats" → ["I", " ", "l", "o", "v", "e", " ", "c", "a", "t", "s"]
- Pros: Handles any input (no unknown tokens).
- Cons: Long sequence lengths, making training slower and less efficient.

## 3. Subword Tokenization
Used in most modern LLMs. It strikes a balance between word and character-level tokenization.

### a. Byte Pair Encoding (BPE)
- Used in: GPT-2, GPT-3
- Description: Starts with characters, merges most frequent adjacent pairs iteratively.
- Example: "unhappiness" → ["un", "happiness"] → ["un", "happi", "ness"]
- Pros: Reduces vocabulary size, handles rare and compound words well.

### b. WordPiece
- Used in: BERT
- Description: Similar to BPE but uses a different algorithm for selecting merges based on likelihood.
- Example: "playing" → ["play", "##ing"]
- Pros: Balances vocabulary size and efficiency; keeps common roots intact.

### c. Unigram Language Model
- Used in: XLNet, T5
- Description: Starts with a large set of subword units and selects a subset that best compresses the data using a probabilistic model.
- Pros: Flexible; supports multiple segmentations of the same word.

## 4. Byte-Level Tokenization
- Used in: GPT-2, GPT-3 (with byte-level BPE)
- Description: Operates directly on UTF-8 bytes before applying subword techniques like BPE.
- Pros: Can handle any Unicode text without normalization issues.