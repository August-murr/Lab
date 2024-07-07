# Example Scripts for ScalableGen

For the full explanation, visit the [article](link_to_article).

These example scripts demonstrate how to use [ScalableGen](https://github.com/August-murr/ScalableGen) for various tasks such as benchmarking a base model (Mistral) on the GSM8K benchmark, tuning models with adapters, generating responses, creating preference datasets, and training low-rank adapters.

## Scripts Overview

### Benchmarking and Response Generation

- **`mistral_gsm8k_benchmarking.py`**
  - **Purpose:** Uses ScalableGen with the GSM8K test set to generate responses to math questions and extracts their answers into the database.
  - **Usage:** Can also be applied to the train set of the GSM8K dataset to generate responses.

- **`calculating_benchmark.py`**
  - **Purpose:** Calculates the number of correct answers to benchmark the models performance.

### Preference Dataset Creation

- **`retry_generation.py`**
  - **Purpose:** Utilizes responses generated in the previous steps and prompts the model to answer them again using different approaches.
  - **Outcome:** Results can be used to create a [preference dataset](https://huggingface.co/datasets/August4293/gsm8k_preference_dataset_it_1).

### Model Training

- **`sft-on-gsm8k-preference_dataset.ipynb`**
  - **Purpose:** Uses the preference dataset to train the low-rank adapter with supervised fine-tuning.

- **`dpo-on-gsm8k-preference_dataset.ipynb`**
  - **Purpose:** Uses the preference dataset to train the low-rank adapter with a direct preference optimization algorithm.

### Fine-Tuned Model Generation

- **`tuned_model_generation.py`**
  - **Purpose:** Generates responses with ScalableGen using the fine-tuned model (PEFT model) for generation, retry generation, or benchmarking.

