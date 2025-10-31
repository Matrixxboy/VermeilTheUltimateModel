# Training

This directory contains the code for training the Vermeil models. The training loop is one of the most critical parts of the project, and the code in this directory is designed to be flexible, extensible, and easy to use.

## Key Components

-   **`trainer_base.py`**: This file contains the main training loop for the project. It is a generic trainer that can be used to train any of the models in the `src/modalities/` directory. It handles tasks like:
    -   Loading the model and the data.
    -   Iterating over the training data in epochs and batches.
    -   Performing the forward and backward passes.
    -   Updating the model's weights.
    -   Evaluating the model on a validation set.
    -   Saving checkpoints.
    -   Logging metrics to TensorBoard or other monitoring tools.

-   **`optimizer_factory.py`**: This file contains a factory function for creating optimizers. It allows you to easily switch between different optimizers (e.g., Adam, SGD) and to configure their hyperparameters through the YAML configuration files.

-   **`callbacks.py`**: This file contains a set of callbacks that can be used to add custom logic to the training loop. Callbacks can be used for things like:
    -   Early stopping: Stop the training if the validation loss does not improve for a certain number of epochs.
    -   Learning rate scheduling: Adjust the learning rate during training.
    -   Logging custom metrics: Log additional metrics that are not captured by the main training loop.

-   **`distributed_training.py`**: This file contains utilities for distributed training. It provides a wrapper around PyTorch's `DistributedDataParallel` (DDP) module to make it easier to train models on multiple GPUs or multiple nodes.

## The Training Process

The training process is initiated by running the `trainer_base.py` script with a specific training configuration file.

```bash
python src/training/trainer_base.py --config configs/training/text_config.yaml
```

The trainer then performs the following steps:

1.  **Load the configuration**: The trainer loads the configuration file specified by the `--config` argument.
2.  **Initialize the model**: The trainer initializes the model specified in the configuration file.
3.  **Initialize the data loaders**: The trainer initializes the data loaders for the training and validation sets.
4.  **Initialize the optimizer and scheduler**: The trainer initializes the optimizer and the learning rate scheduler.
5.  **Run the training loop**: The trainer runs the main training loop for the specified number of epochs.
6.  **Save the best model**: The trainer saves the model checkpoint with the best validation performance.

## Customizing the Training Process

The training process can be customized in several ways:

-   **By modifying the configuration file**: You can change the model architecture, the hyperparameters, and other training settings by modifying the YAML configuration file.
-   **By creating new callbacks**: You can add custom logic to the training loop by creating new callbacks in the `callbacks.py` file.
-   **By creating a new trainer**: For more complex training scenarios, you can create a new trainer that inherits from the `TrainerBase` class and overrides its methods.
