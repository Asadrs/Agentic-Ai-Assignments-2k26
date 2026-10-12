"""
Assignment-03 Question 1
Few-Shot Prompting - Sentiment Classification
"""

from openai import OpenAI

# ======================
# SETUP
# ======================
# Replace with your own API key
client = OpenAI(
    api_key="YOUR_API_KEY_HERE",          # put your key here
    # base_url="https://api.groq.com/openai/v1"   # uncomment if using Groq
)

# ======================
# FEW-SHOT PROMPT
# ======================
prompt = """
You are a sentiment classifier. Classify the customer message as Positive, Negative, or Neutral.

Here are some examples:

Message: "I love this product, it works perfectly!"
Sentiment: Positive

Message: "The delivery was late and the item was damaged."
Sentiment: Negative

Message: "The product is okay, nothing special."
Sentiment: Neutral

Message: "Customer support was very helpful and resolved my issue quickly."
Sentiment: Positive

Now classify this message:
Message: "The app keeps crashing every time I try to login."
Sentiment:
"""

# ======================
# CALL THE LLM
# ======================
response = client.chat.completions.create(
    model="gpt-4o-mini",          # or "llama-3.1-8b-instant" if using Groq
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0
)

print("Predicted Sentiment:", response.choices[0].message.content.strip())