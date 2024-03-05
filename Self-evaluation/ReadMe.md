This directory contains two notebooks: `self-evaluator_prompt_tuning` and `mistral_harmlessness_self_evaluation`. Both notebooks are developed using the (Anthropic's Red Teaming Prompt Dataset)[https://huggingface.co/datasets/Anthropic/hh-rlhf]

## self-evaluator_prompt_tuning

In this notebook, a test framework has been crafted to assess the accuracy and agreement of the Mistral 7b model with various prompts, including one-shot and few-shot prompts. These prompts instruct the model to evaluate its own responses and judge them for harm, unethical content, or danger. The framework measures prompt accuracy using a labeled dataset of 50 red team prompt response judgments. It also calculates prompt speed and efficiency to identify the most effective prompt. The result of the testing indicates an 82% agreement for a one-shot prompt.

## mistral_harmlessness_self_evaluation

This notebook utilizes the previously tuned one-shot prompt from the `self-evaluator_prompt_tuning` notebook to self-evaluate the base Mistral 7b model on the Anthropic's dataset. The obtained results will serve as a baseline for comparison with fine-tuned models, which will undergo additional fine-tuning for alignment and safety.

In addition to self-evaluation for harmlessness, the [llm_judge](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge) module from FastChat is employed to evaluate the base model and subsequently fine-tuned models on the MT-Bench dataset, as explained in [this paper](https://arxiv.org/abs/2306.05685). This evaluation aims to determine if alignment efforts result in a reduction of model helpfulness, commonly referred to as alignment tax.
