# Modalities

This directory contains the main model implementations for the different modalities that Vermeil supports. Each file in this directory defines a complete model for a specific modality (e.g., text, image, audio) or a combination of modalities (multimodal).

These models are constructed by assembling the core components from the `src/core/` directory into a larger architecture.

## Key Models

-   **`text_model.py`**: This file defines the main text-based model, which is likely a Transformer-based language model (similar to BERT or GPT). It can be used for tasks like text classification, question answering, and text generation.

-   **`image_model.py`**: This file defines the main image-based model. This could be a generative model like a Generative Adversarial Network (GAN) or a diffusion model for image synthesis. It could also be a model for image classification or object detection.

-   **`audio_model.py`**: This file defines the main audio-based model. This could be a model for speech recognition, music generation, or audio classification.

-   **`multimodal_fusion.py`**: This file is where the magic happens for multimodal tasks. It defines the architecture for fusing the representations from different modalities. This could involve techniques like cross-attention, concatenation, or more complex fusion strategies.

## Design Principles

-   **Separation of Concerns**: Each file should define a single model for a specific modality. The code for the model's architecture should be separate from the training loop and the data loading.
-   **Configuration-Driven**: The models should be configurable through the YAML files in the `configs/` directory. This allows for easy experimentation with different model architectures and hyperparameters.
-   **Clarity and Readability**: The code should be well-documented and easy to understand. A clear and readable implementation is crucial for debugging and for collaboration.

## How to Add a New Modality

To add a new modality to Vermeil, you would need to:

1.  **Create a new model file**: Create a new Python file in this directory that defines the architecture for the new modality.
2.  **Add core components**: If the new model requires any new core components, add them to the `src/core/` directory.
3.  **Add a data loader**: Create a new data loader in `datasets/loaders/` to handle the data for the new modality.
4.  **Add a training configuration**: Create a new training configuration file in `configs/training/` for the new modality.
5.  **Add an evaluation script**: Create a new evaluation script in `src/evaluation/` to evaluate the performance of the new model.
