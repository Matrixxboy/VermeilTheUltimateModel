# Tools

This directory contains various tools to support the development workflow of the Vermeil project. These tools are designed to automate common tasks, improve productivity, and help with the analysis and optimization of the models.

## Directory Structure

-   **`dataset_tools/`**: This subdirectory contains tools for working with datasets. This can include scripts for summarizing datasets, merging multiple datasets, or converting datasets from one format to another.

-   **`distributed/`**: This subdirectory contains tools for distributed training. This can include launchers for different distributed training frameworks (e.g., DeepSpeed, Horovod) and configuration files for setting up a distributed training environment.

-   **`optimization/`**: This subdirectory contains tools for model optimization. This can include scripts for pruning, quantization, and knowledge distillation. These tools can be used to reduce the size of the models and to improve their inference speed.

-   **`profiling/`**: This subdirectory contains tools for profiling the performance of the models. This can include scripts for counting the number of floating-point operations (FLOPs) in a model, measuring the memory usage of a model, and identifying performance bottlenecks.

-   **`visualization/`**: This subdirectory contains tools for creating visualizations of the models and their outputs. This can include scripts for plotting loss curves, visualizing gradient flow, and generating attention maps.

## Usage

The tools in this directory are designed to be run from the command line. Each tool should have a clear and well-documented command-line interface.

**Example:**

```bash
# Get a summary of a dataset
python tools/dataset_tools/dataset_summary.py --dataset_path data/processed/text/train.txt

# Profile the memory usage of a model
python tools/profiling/memory_profiler.py --config configs/training/text_config.yaml

# Plot the loss curve from a training log
python tools/visualization/loss_curve_plotter.py --log_file experiments/exp_001_text_baseline/logs/training.log
```

## Adding New Tools

If you have a script that you think would be useful to other members of the team, consider adding it to this directory.

When adding a new tool, please make sure to:

-   Place it in the appropriate subdirectory.
-   Give it a clear and descriptive name.
-   Add a command-line interface using a library like `argparse`.
-   Add a docstring that explains what the tool does and how to use it.
