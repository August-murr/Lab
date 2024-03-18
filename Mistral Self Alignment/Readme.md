# Mistral Self-Alignment

The **Mistral Self-Alignment** project explores a self-improvement concept utilizing red teaming to evaluate and enhance model responses for harmlessness and safety. The methodology employed here can be extended to various self-improvement concepts tailored for different purposes, including the utilization of tools across diverse environments.

## Overview

Initially, the project involved:

- Comparison of accuracy and speed of different prompts using a manually labeled dataset with the [self-evaluation prompt tuning notebook](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/%20self-evaluator_prompt_tuning.ipynb).
- Generation of synthetic data through the [preference data generation notebook](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/preference-dataset-generation.ipynb) ([preference dataset link](https://huggingface.co/datasets/August4293/Preference-Dataset)).
- Red team prompt dataset utilization to generate responses, subsequently labeled with a self-evaluation template to determine harmfulness. Non-harmful responses were filtered to maintain helpfulness, and a preference dataset was created.
- Training of two adapters using supervised fine-tuning and direct preference optimization training methods, as depicted in the following notebooks:
  - [SFT training notebook](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/SFT_mistral_on_preference_data.ipynb)
  - [DPO training notebook](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/DPO_mistral_on_preference_dataset.ipynb).

## Evaluation

Evaluation involved the creation of a new red team prompt dataset, where Mistral 7b failed at every response, to assess the newly fine-tuned models. Results indicated a rejection rate of approximately 98% for red teaming prompts, with the DPO model showing slightly better performance. Refer to the following notebooks for detailed analysis:
- [Red teaming SFT adapter](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/red-teaming-sft-model-on-test-data.ipynb)
- [Red teaming DPO adapter](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/red-teaming-dpo-model-on-test-data.ipynb).

## Challenges and Further Considerations

Despite the success rate of the fine-tuned models, there was a noticeable reduction in helpfulness, rendering the models overly cautious. They refrained from answering questions even with a slight chance of a harmful response. A notebook comparing the base Mistral model to the fine-tuned model is available for reference:
- [Mistral vs Self-Aligned](https://github.com/August-murr/Lab/blob/main/Mistral%20Self%20Alignment/Notebooks/mistral-vs-self-aligned.ipynb).

This reduction in helpfulness could potentially be mitigated by curating a more diverse dataset that incorporates helpful answers to questions.

## Project Availability

While initially a personal project aimed at implementing a basic form of self-improvement, all the code and notebooks are available for public use and exploration. Feel free to utilize them for your own purposes.
