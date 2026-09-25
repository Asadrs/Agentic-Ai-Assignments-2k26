\# Assignment-01 – Descriptive Questions



\### 1. Difference between "training" a model and "inference"



\*\*Training\*\* is the process of teaching a machine learning model by showing it many examples with correct answers. During training, the model adjusts its internal parameters (weights) to learn patterns from the data.



\*\*Inference\*\* is the process of using an already trained model to make predictions on new, unseen data.



\*\*Everyday examples:\*\*

\- \*\*Training\*\*: A student studies many past exam papers with solutions to learn how to solve questions.

\- \*\*Inference\*\*: The same student sits in the actual exam and answers new questions using what they learned.



\---



\### 2. What does the "weight" in a neural network control?



A \*\*weight\*\* controls how important a particular input (feature) is when the neural network makes a decision.  

Higher weight = stronger influence of that feature on the final output.



\*\*Decision-making analogy (Choosing an apartment):\*\*



Imagine you are choosing an apartment. Possible features:

\- Distance to office

\- Rent price

\- Size of the apartment

\- Noise level



\- If the weight for “distance to office” is high, it means you care a lot about commute time.

\- If the weight for “rent” is high (or negative), expensive rent will strongly push you away from choosing that apartment.



The neural network multiplies each feature by its weight and combines the results to decide whether the apartment is good or not.



\---



\### 3. Difference between Open-source and Closed models



| Aspect              | Open-source (Llama, Qwen)                          | Closed (GPT, Claude)                              |

|---------------------|----------------------------------------------------|---------------------------------------------------|

| Model weights       | Fully downloadable                                 | Not available                                     |

| What you can do     | Run locally, fine-tune, modify, deploy anywhere    | Only use via API or website                       |

| Transparency        | High (you can inspect the model)                   | Low (black-box)                                   |

| Cost                | Free to download (you pay only for compute)        | Usually pay per token / subscription              |



\---



\### 4. Why does a free model still cost money to run?



Even if the model is free to download, running it requires:

\- Powerful hardware (especially GPU)

\- Electricity

\- Cloud servers (if you don’t have a strong computer)



Large language models need expensive computing power, so most people rent cloud GPUs, which costs money.



\---



\### 5. What does the slope (m) tell you in the equation y = mx + b?



The slope \*\*m\*\* tells you \*\*how much the output (y) changes when the input (x) increases by 1\*\*.



\- Positive m → as input increases, output increases

\- Negative m → as input increases, output decreases

\- Larger absolute value of m → stronger relationship between input and output

