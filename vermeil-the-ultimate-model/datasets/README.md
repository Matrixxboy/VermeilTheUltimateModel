# Datasets

This directory contains scripts and metadata related to the datasets used in the Vermeil project. While the `data/` directory holds the actual data, this directory is for the code that handles the datasets, such as data loaders, download scripts, and metadata files.

## Directory Structure

-   **`loaders/`**: This subdirectory contains custom data loaders for different modalities and tasks. These loaders are responsible for reading the processed data from the `data/processed/` directory and feeding it to the model in batches. They can also handle tasks like padding, masking, and creating attention masks.

-   **`metadata/`**: This subdirectory contains metadata about the datasets used in the project. This can include information about the source of the data, its license, its size, and its characteristics. Maintaining this metadata is crucial for data governance and for ensuring that the project complies with any licensing requirements.

-   **`scripts/`**: This subdirectory contains utility scripts for managing datasets. This can include scripts for downloading datasets from the internet, scraping data from websites, merging multiple datasets, or converting datasets from one format to another.

## Usage

The scripts and modules in this directory are used throughout the project.

-   The **data loaders** in `loaders/` are used by the training scripts in `src/training/` to feed data to the model.
-   The **scripts** in `scripts/` are used to populate the `data/raw/` directory with data.
-   The **metadata** in `metadata/` is used for documentation and for ensuring compliance with data licenses.

## Adding a New Dataset

When adding a new dataset to the project, you should:

1.  **Add a download script**: If the dataset needs to be downloaded, add a script to `scripts/` to automate the process.
2.  **Add a data loader**: Create a new data loader in `loaders/` to read the processed data and prepare it for the model.
3.  **Update the metadata**: Add a new entry to the metadata files in `metadata/` to document the new dataset.
4.  **Update the configuration**: Add the new dataset to the appropriate training configuration file in `configs/training/`.
