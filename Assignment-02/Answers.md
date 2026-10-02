Assignment-02

Understanding How LLMs Work



\--------------------------------------------------

1\. What happens when you give a sentence to an LLM?



Example sentence: “The cat is sleeping.”



Here is the full journey of the sentence inside the model:



Text

&#x20; ↓

Tokens

&#x20; ↓

Token IDs

&#x20; ↓

Embeddings

&#x20; ↓

Transformer

&#x20; ↓

Next-token Prediction





Step-by-step with diagram:



1\. Text is split into tokens

&#x20;  “The cat is sleeping.”  

&#x20;  →  \[The] \[cat] \[is] \[sleeping] \[.]



2\. Tokens become Token IDs (numbers)

&#x20;  \[The]     →  464

&#x20;  \[cat]     →  3797

&#x20;  \[is]      →  318

&#x20;  \[sleeping]→  11245

&#x20;  \[.]       →  13



3\. Token IDs become Embeddings (vectors)

&#x20;  3797 (“cat”)  →  \[0.12, -0.45, 0.88, 0.33, ...]



4\. Embeddings go into the Transformer

&#x20;  The Transformer looks at all words together and understands context.



5\. Model predicts the next token

&#x20;  It keeps generating one word at a time until the answer is complete.





\--------------------------------------------------

2\. What is tokenization and why do LLMs need it?



Tokenization = breaking text into small pieces called tokens.



Example:



Common word:

hello        →  1 token



Long / uncommon word:

tokenization →  token + iza + tion   (3 tokens)



Why LLMs need it?

Computers only understand numbers. So we first convert words into tokens, then into numbers.



Why number of tokens is important:

\- More tokens = more cost

\- Models have a maximum limit (context length)

\- Longer prompts use more tokens





\--------------------------------------------------

3\. Difference between Token ID and Embedding



Suppose “cat” becomes Token ID = 1234



Token ID 1234 is just a label (like a student roll number).

It has no meaning by itself.



Embedding is a long list of numbers that actually carries the meaning of the word.



Diagram:



Word “cat”

&#x20;  ↓

Token ID → 1234          (just a number/label)

&#x20;  ↓

Embedding → \[0.21, -0.67, 0.45, 0.12, ...]   (this has meaning)



We cannot use Token ID alone because the number 1234 is not similar to 1235 in meaning. But embeddings of “cat” and “dog” will be close to each other.





\--------------------------------------------------

4\. How does an LLM generate an answer using next-token prediction?



Example prompt: “The capital of India is”



Process:



Step 1: Model sees → “The capital of India is”

Step 2: Predicts most likely next token → “New”

Step 3: Now the text becomes → “The capital of India is New”

Step 4: Predicts next token → “Delhi”

Step 5: Text becomes → “The capital of India is New Delhi”

Step 6: Continues until it finishes



Diagram of the process:



Input: The capital of India is

&#x20;         ↓

&#x20;    Predict → New

&#x20;         ↓

Input: The capital of India is New

&#x20;         ↓

&#x20;    Predict → Delhi

&#x20;         ↓

Input: The capital of India is New Delhi

&#x20;         ↓

&#x20;    Predict → (end)





The model writes the answer one token at a time, not the full sentence at once.





\--------------------------------------------------

5\. How do embeddings help an LLM understand relationships between words?



Embeddings place words in a space based on meaning.



\- Similar words stay close

\- Different words stay far



Example:



“cat” and “dog”  → close to each other (both animals)

“cat” and “car”  → far from each other (different concepts)



Simple idea of Cosine Similarity:



Imagine two arrows.

If both arrows point in almost the same direction → high similarity

If they point in different directions → low similarity



This is how the model understands that “king” is related to “queen” or “happy” is related to “joy”.

