# Source Code

This directory contains the main source code for the Vermeil model. It is organized into a modular structure to promote code reuse, maintainability, and collaboration.

## Directory Structure

-   **`core/`**: This subdirectory contains the core building blocks of the models, such as attention mechanisms, transformer blocks, and diffusion layers. These are the fundamental components that are used to build the larger models.

-   **`embeddings/`**: This subdirectory contains code for generating text and image embeddings. Embeddings are vector representations of the input data that are used by the models.

-   **`evaluation/`**: This subdirectory contains scripts for evaluating the performance of the models. This includes implementations of various metrics for different modalities, such as BLEU, ROUGE, FID, and IS.

-   **`inference/`**: This subdirectory contains scripts for running inference with the trained models. These scripts are designed to be used for generating predictions on new data.

-   **`modalities/`**: This subdirectory contains the main model implementations for the different modalities (text, image, audio, multimodal). These models are built using the core components from the `core/` directory.

-   **`tokenizers/`**: This subdirectory contains code for training and using tokenizers. Tokenizers are used to convert raw text into a sequence of tokens that can be processed by the models.

-   **`training/`**: This subdirectory contains the code for training the models. This includes the main training loop, optimizer factories, and callbacks for things like logging and checkpointing.

-   **`utils/`**: This subdirectory contains general utility functions that are used throughout the project. This can include things like configuration loaders, loggers, and checkpoint managers.

## Coding Style and Conventions

To ensure that the codebase is consistent and easy to read, we follow a set of coding style and conventions. These include:

-   **PEP 8**: We follow the PEP 8 style guide for Python code.
-   **Type Hinting**: We use type hints to improve code clarity and to allow for static analysis.
-   **Docstrings**: We use Google-style docstrings to document our code.
-   **Unit Tests**: We use the `pytest` framework to write unit tests for our code. All new code should be accompanied by unit tests.

Before submitting a pull request, please make sure that your code conforms to these conventions and that all the tests pass.

You can run the linter and the tests by running the following commands from the root of the repository:

```bash
# Run the linter
flake8 src/

# Run the tests
pytest tests/
```
