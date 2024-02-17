# Mistral Self-Evaluator Prompt

This repository contains a notebook where we have developed a self-evaluator prompt for Mistral.
The goal of this prompt is to enable Mistral to evaluate and criticize its own responses when prompted to give harmful, unethical, or illegal advice.

## Dataset
We utilized the [Anthopics Red Teaming Prompt Dataset](https://huggingface.co/datasets/Anthropic/hh-rlhf) to develop this self-evaluator prompt. We manually labeled a subset of 50 Red Teaming prompts to create an evaluation dataset, which serves as a benchmark to compare the accuracy of different prompts.

## Functionality
In addition to the evaluation dataset, the function compares the accuracy, speed, and inference time of different prompts. This self-evaluation and classification of responses are crucial, considering that Mistral rejects approximately 25% of the Red Teaming prompts. Filtering out non-harmful prompts and responses is imperative to prevent the model from becoming less helpful in the self-alignment process.

## Versatility
While this prompt was primarily tuned for safety and toxicity evaluation, it is versatile enough to test a wide range of creative ideas. These include self-rewarding, self-evaluation for reasoning and logic, hallucination, coding, and various other tasks.

## Usage
The code and prompt provided in this notebook will be used to align Mistral for safety. 
While originally intended for personal use, feel free to explore, utilize, and contribute to this repository.
