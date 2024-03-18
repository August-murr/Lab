# Mistral Self-Alignment

The goal of this project was to experiment with a self-improvement concept, utilizing red teaming to evaluate and enhance the model's responses for harmlessness and safety. This concept has potential applications beyond self-improvement, extending to various environments and tools.

## Prompt Evaluation and Data Generation

- For initial evaluation, different prompts were compared in terms of accuracy and speed using a manually labeled dataset. Check out the [self-evaluation prompt tuning notebook](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/%20self-evaluator_prompt_tuning.ipynb).
- Synthetic data generation was performed using the [preference data generation notebook](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/preference-dataset-generation.ipynb), available [here](https://huggingface.co/datasets/August4293/Preference-Dataset).

## Model Training

- Responses generated from the red team prompt dataset were labeled using a self-evaluation template to filter out harmful ones. The remaining non-harmful responses were used to create a preference dataset.
- Two adapters were trained using supervised fine-tuning and direct preference optimization methods. Explore the training process in the following notebooks:
  - [SFT training notebook](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/SFT_mistral_on_preference_data.ipynb)
  - [DPO training notebook](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/DPO_mistral_on_preference_dataset.ipynb)

## Model Availability

The trained models are available on Hugging Face:
- [SFT model](https://huggingface.co/August4293/mistral_self_alignment_SFT)
- [DPO model](https://huggingface.co/August4293/mistral_self_alignment_DPO)

## Evaluation

A new red team prompt dataset was created to evaluate the fine-tuned models' performance. The results indicated that the models rejected the red teaming prompts at a rate of approximately 98%, with the DPO model slightly outperforming the SFT model. Explore the evaluation notebooks:
- [Red teaming SFT adapter](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/red-teaming-sft-model-on-test-data.ipynb)
- [Red teaming DPO adapter](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/red-teaming-dpo-model-on-test-data.ipynb)

## Further Considerations

However, the success of the fine-tuned models came at a cost of reduced helpfulness, making them overly cautious. Even a slight potential for harm led to refusal to respond. This reduction in helpfulness could be addressed by diversifying the dataset to include helpful answers to questions.

While this project was undertaken for personal self-improvement purposes, all the code and notebooks are available for anyone interested in exploring or utilizing them.
