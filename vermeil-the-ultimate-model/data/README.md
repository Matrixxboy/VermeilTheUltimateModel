# Data

This directory is the central hub for all data used in the Vermeil project. It is organized to support a clear and reproducible data processing pipeline, from raw data to processed data ready for training.

## Directory Structure

-   **`raw/`**: This subdirectory contains the original, unmodified data downloaded from various sources. The data is organized into subdirectories by modality (e.g., `text/`, `images/`, `audio/`). It is important to keep this data immutable to ensure that you can always go back to the original source.

-   **`processing/`**: This subdirectory contains scripts for processing the raw data. These scripts handle tasks like cleaning, filtering, normalization, and data augmentation. The goal is to transform the raw data into a format that is suitable for training the model.

-   **`processed/`**: This subdirectory contains the output of the processing scripts. This is the data that will be fed into the model for training. Like the `raw/` directory, it is organized into subdirectories by modality.

-   **`logs/`**: This subdirectory contains logs and reports generated during the data processing pipeline. This can include things like dataset summaries, preprocessing reports, and error logs. These logs are useful for debugging and for understanding the characteristics of the data.

## Data Pipeline Workflow

The typical data pipeline workflow is as follows:

1.  **Download Raw Data**: Download the raw data from its source and place it in the appropriate subdirectory in `raw/`.

2.  **Process Data**: Run the processing scripts in `processing/` to transform the raw data into a clean and usable format. The output of these scripts should be saved to the `processed/` directory.

3.  **Log Everything**: Ensure that your processing scripts generate logs and reports that are saved to the `logs/` directory. This will help you track the data lineage and reproduce your results.

## Git LFS

This project uses [Git LFS](https://git-lfs.github.com/) to handle large files. The `.gitignore` file is configured to ignore the contents of the `raw/` and `processed/` directories to prevent large data files from being checked into Git. Instead, you should use a data versioning tool like [DVC](https://dvc.org/) to track your data and models.

## Adding New Datasets

When adding a new dataset to the project, please follow these steps:

1.  Add a script to `datasets/scripts/` to download the dataset.
2.  Add the raw data to the appropriate subdirectory in `raw/`.
3.  Add a processing script to `processing/` to clean and transform the data.
4.  Generate the processed data in the `processed/` directory.
5.  Update the dataset metadata in `datasets/metadata/`.
