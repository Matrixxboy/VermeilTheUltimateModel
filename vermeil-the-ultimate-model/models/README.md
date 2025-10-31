# Models

This directory is for storing the trained models of the Vermeil project. This includes model checkpoints saved during training, as well as models that have been exported for deployment.

## Directory Structure

-   **`checkpoints/`**: This subdirectory contains model checkpoints saved during training. A checkpoint is a snapshot of the model's weights at a particular point in time. Checkpoints can be used to resume training from a previous state or to evaluate the model at different stages of training.

-   **`exports/`**: This subdirectory contains models that have been exported for deployment. An exported model is typically a more lightweight and optimized version of the model that is suitable for running in a production environment. This can include models that have been quantized, pruned, or converted to a format like ONNX.

-   **`pretrained/`**: This subdirectory contains pre-trained components that are used by the models, such as tokenizers and embeddings. These components are often trained on a large corpus of data and can be used to initialize the model before training on a specific task.

## Model Versioning

It is important to keep track of the different versions of the models you train. A good way to do this is to use a consistent naming convention for your model directories and files. For example, you could name your model checkpoints like this:

`{model_name}_{dataset}_{timestamp}.pt`

This would result in a checkpoint file like `text_model_wikipedia_2023-10-27-10-30-00.pt`.

For exported models, you can use version numbers to keep track of the different versions you have deployed:

`vermeil_v1/`
`vermeil_v1.1/`

## Data Version Control (DVC)

Because model files can be very large, they should not be checked into Git. Instead, we use a data version control tool like [DVC](https://dvc.org/) to track our models. DVC allows you to version your models and store them in a remote storage service like Amazon S3, Google Cloud Storage, or a self-hosted server.

The `dvc.yaml` file in the root of the repository is used to configure DVC and to define the data and model pipelines.

To add a model to DVC, you can use the `dvc add` command:

```bash
dvc add models/checkpoints/text/best_model.pt
```

This will create a `.dvc` file that contains a hash of the model file. You can then commit this `.dvc` file to Git to version your model.
