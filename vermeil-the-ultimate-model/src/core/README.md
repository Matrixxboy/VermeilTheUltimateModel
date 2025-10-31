# Core

This directory contains the core building blocks of the Vermeil models. These are the fundamental, reusable components that are combined to create the larger, more complex models for each modality. The code in this directory should be generic and not specific to any particular modality.

## Key Components

-   **`attention.py`**: This file contains implementations of various attention mechanisms, such as:
    -   `SelfAttention`: The standard self-attention mechanism from the Transformer model.
    -   `CrossAttention`: An attention mechanism for attending to an encoder's output.
    -   `FlashAttention`: An efficient implementation of attention for faster training and inference.

-   **`transformer_block.py`**: This file contains the implementation of a standard Transformer block, which typically consists of a self-attention layer followed by a feed-forward network. This is a fundamental building block for many of the models in this project.

-   **`diffusion_layers.py`**: This file contains layers and components specific to diffusion models, which are used for generative tasks like image synthesis. This might include components for noise scheduling, denoising steps, and conditioning.

## Design Principles

-   **Modularity**: Each file should contain a single, well-defined component or a small set of related components.
-   **Reusability**: The components in this directory should be designed to be reusable across different models and modalities.
-   **Generality**: The code should be as general as possible and should not contain any modality-specific logic.
-   **Efficiency**: The components should be implemented in an efficient way to ensure fast training and inference.

## How to Contribute

When adding a new core component, please ensure that it follows the design principles outlined above. The new component should be well-documented, with clear type hints and a comprehensive docstring. It should also be accompanied by unit tests to ensure that it is working correctly.

If you have an idea for a new core component that could be useful for multiple models, please open an issue to discuss it with the team.
