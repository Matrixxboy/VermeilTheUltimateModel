# Configurations

This directory contains all the configuration files for the Vermeil project. Using YAML files for configuration allows for a clear separation of model architecture, training parameters, and hardware settings from the source code. This makes it easier to manage experiments and reproduce results.

## Directory Structure

-   **`hardware/`**: This subdirectory contains configurations related to the hardware used for training and inference. For example, you might have a configuration file for a single GPU setup and another for a multi-GPU cluster.

-   **`inference/`**: This subdirectory contains configurations for the inference API. This can include settings like the port to run the API on, the path to the model checkpoint to use, and any post-processing steps to apply.

-   **`training/`**: This subdirectory contains configurations for training runs. Each modality (text, image, multimodal) has its own configuration file, which specifies the model architecture, hyperparameters, dataset paths, and other training-related settings.

## Usage

The configuration files are used by the training and inference scripts to set up the model and the environment. You can specify which configuration file to use with a command-line argument.

**Example:**

```bash
# Train a model using a specific training configuration
python src/training/trainer_base.py --config configs/training/text_config.yaml

# Run the inference API using a specific API configuration
python deployment/fastapi_app/main.py --config configs/inference/api_config.yaml
```

## Creating New Configurations

To run a new experiment, you can create a new configuration file by copying an existing one and modifying the parameters. It is good practice to give your configuration files descriptive names to make it easy to identify them later.

For example, if you want to experiment with a different learning rate for the text model, you could create a new file called `text_config_lr_1e-5.yaml` and modify the `learning_rate` parameter in that file.

By keeping a record of your configuration files, you can easily track the different experiments you have run and reproduce your results.
