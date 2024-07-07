# Example Scripts for ScalableGen

For the full explanation, visit the [article](link_to_article).

These example scripts demonstrate how to use [ScalableGen](https://github.com/August-murr/ScalableGen) for various tasks such as benchmarking a base model (Mistral), tuning models with adapters, generating responses, creating preference datasets, and training low-rank adapters.

## Scripts Overview

### Benchmarking and Response Generation

- **`mistral_gsm8k_benchmarking.py`**
  - **Purpose:** Uses ScalableGen with the GSM8K test set to generate responses to math questions and extracts their answers into a database.
  - **Usage:** Can also be applied to the train set of the GSM8K dataset to generate responses.

- **`calculating_benchmark.py`**
  - **Purpose:** Calculates the number of correct answers to benchmark the model's performance.

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

## Usage Instructions

1. **Benchmarking and Response Generation:**
   - Run `mistral_gsm8k_benchmarking.py` to generate responses for GSM8K datasets.
   - Use `calculating_benchmark.py` to calculate correct answers and benchmark the model.

2. **Creating Preference Datasets:**
   - Execute `retry_generation.py` to create a diverse set of responses, forming a preference dataset.

3. **Training Low-Rank Adapters:**
   - Utilize the notebooks `sft-on-gsm8k-preference_dataset.ipynb` and `dpo-on-gsm8k-preference_dataset.ipynb` for training the model with the generated preference datasets.

4. **Generating Responses with Fine-Tuned Models:**
   - Use `tuned_model_generation.py` to generate responses using the fine-tuned (PEFT) model for various tasks, including benchmarking and retry generation.

By following these steps and utilizing the provided scripts, you can efficiently benchmark models, create preference datasets, and train low-rank adapters using ScalableGen.
