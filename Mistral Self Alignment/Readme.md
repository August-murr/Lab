# Mistral Self-Alignment

The goal of this project was to experiment with a self-improvement concept. We used red teaming to evaluate and improve the model's responses for harmlessness and safety. The idea can be extended to other self-improvement concepts for different purposes, such as using tools in various environments.

## Project Components

### Prompt Evaluation and Comparison
- Initial comparison of prompt accuracy and speed using a manually labeled dataset: [Self-Evaluation Prompt Tuning Notebook](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/%20self-evaluator_prompt_tuning.ipynb)

### Synthetic Data Generation
- Synthetic data generation using the preference data generation notebook: [Preference Data Generation Notebook](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/preference-dataset-generation.ipynb)
- Synthetic data available at: [Hugging Face - Preference Dataset](https://huggingface.co/datasets/August4293/Preference-Dataset)

### Model Training
- Two adapters trained using supervised fine-tuning and direct preference optimization:
  - [SFT Training Notebook](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/SFT_mistral_on_preference_data.ipynb)
  - [DPO Training Notebook](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/DPO_mistral_on_preference_dataset.ipynb)

### Model Deployment
- Models available on Hugging Face:
  - [SFT Model](https://huggingface.co/August4293/mistral_self_alignment_SFT)
  - [DPO Model](https://huggingface.co/August4293/mistral_self_alignment_DPO)

### Evaluation
- Evaluation of fine-tuned models using a new red team prompt dataset:
  - [Red Teaming SFT Adapter](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/red-teaming-sft-model-on-test-data.ipynb)
  - [Red Teaming DPO Adapter](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/red-teaming-dpo-model-on-test-data.ipynb)

### Analysis
- Comparison of base Mistral model to fine-tuned model:
  - [Mistral vs Self-Aligned Notebook](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/mistral-vs-self-aligned.ipynb)

## Conclusion

While the fine-tuned models showed a high success rate in rejecting harmful prompts, they demonstrated a reduction in helpfulness and overly cautious behavior. Further improvements could involve diversifying the dataset to include helpful answers to questions.

## Disclaimer

This was a personal project undertaken to implement a basic form of self-improvement. Feel free to use all the code and notebooks for your own purposes.

