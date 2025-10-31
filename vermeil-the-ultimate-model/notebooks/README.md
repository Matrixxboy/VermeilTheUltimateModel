# Notebooks

This directory contains Jupyter notebooks for data exploration, model debugging, and performance analysis. Notebooks provide an interactive environment for experimenting with code and visualizing data, making them a valuable tool for a research project like Vermeil.

## Types of Notebooks

-   **`data_exploration.ipynb`**: This notebook is for exploring the datasets used in the project. It can be used to visualize the data distribution, identify outliers, and get a general sense of the data's characteristics.

-   **`model_debugger.ipynb`**: This notebook is for debugging the models. It can be used to step through the model's architecture, visualize the activations of different layers, and identify potential issues with the model's implementation.

-   **`multimodal_visuals.ipynb`**: This notebook is for creating visualizations of the multimodal model's behavior. This can include things like attention maps, cross-modal embeddings, and generated samples.

-   **`performance_comparison.ipynb`**: This notebook is for comparing the performance of different models or different versions of the same model. It can be used to generate plots and tables that summarize the key performance metrics.

-   **`tokenization_tests.ipynb`**: This notebook is for testing and experimenting with different tokenization strategies. It can be used to visualize the output of the tokenizer and to compare the vocabulary sizes of different tokenizers.

## Best Practices for Using Notebooks

-   **Keep notebooks focused**: Each notebook should have a clear and specific purpose. Avoid creating monolithic notebooks that try to do too many things at once.

-   **Document your work**: Use markdown cells to document your code and explain your reasoning. This will make it easier for others (and for your future self) to understand your work.

-   **Keep notebooks clean**: Remove any unnecessary code or output before committing a notebook to the repository. A clean notebook is easier to read and review.

-   **Consider converting to scripts**: If a notebook contains code that you want to reuse, consider converting it to a Python script and adding it to the `src/` or `tools/` directory. This will make the code more modular and easier to test.

-   **Manage your environment**: Make sure that your notebooks are run in the same Conda environment as the rest of the project. This will ensure that you are using the same versions of the libraries and that your results are reproducible.

You can start a Jupyter Lab server by running the following command in your terminal:

```bash
jupyter lab
```
