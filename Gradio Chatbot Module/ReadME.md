## Gradio Chatbot Module

These modules enable you to load Mistral or Llama along with PEFT adapters in Google Colab through a Gradio GUI.

This project is based on a script originally written by the Hugging Face team for a llama Gradio GUI on Hugging Faces Spaces. You can find the original script [here](https://huggingface.co/spaces/huggingface-projects/llama-2-7b-chat/blob/main/app.py).

Although this module was initially developed for personal use to test fine-tuned models, you are welcome to clone it if you find it useful.

## Usage

The script takes two parameters: `path_to_model` and `path_to_peft` (optional for base Mistral and Llama). Both should be provided as strings, and paths can be either file paths or Hugging Face Hub IDs.

### Example in Colab

```bash
!python mistral_peft_gradio_gui.py "path_to_model" "path_to_peft"
