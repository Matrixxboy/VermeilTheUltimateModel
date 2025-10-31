import os

# === CONFIG ===
PROJECT_NAME = "vermeil-the-ultimate-model"

# === STRUCTURE MAP ===
structure = {
    "configs": {
        "training": ["text_config.yaml", "image_config.yaml", "multimodal_config.yaml"],
        "inference": ["api_config.yaml"],
        "hardware": ["gpu_cluster_config.yaml"],
    },
    "data": {
        "raw": ["text/", "images/", "audio/", "video/"],
        "processing": [
            "preprocess_text.py",
            "preprocess_images.py",
            "preprocess_audio.py"
        ],
        "processed": ["text/", "image/", "audio/"],
        "logs": ["preprocessing_report.md", "dataset_summary.json"],
    },
    "datasets": {
        "metadata": ["dataset_sources.xlsx", "licenses.md"],
        "loaders": ["text_loader.py", "image_loader.py", "multimodal_loader.py"],
        "scripts": ["scrape_data.py", "data_merge.py"],
    },
    "src": {
        "core": ["attention.py", "transformer_block.py", "diffusion_layers.py"],
        "embeddings": ["text_embedding.py", "image_embedding.py"],
        "tokenizers": ["train_tokenizer.py", "custom_vocab.json"],
        "modalities": ["text_model.py", "image_model.py", "audio_model.py", "multimodal_fusion.py"],
        "training": ["trainer_base.py", "distributed_training.py", "optimizer_factory.py", "callbacks.py"],
        "evaluation": ["nlp_metrics.py", "image_metrics.py", "multimodal_metrics.py"],
        "inference": ["text_infer.py", "image_infer.py", "multimodal_infer.py"],
        "utils": ["logger.py", "seed_everything.py", "config_loader.py", "checkpoint_manager.py"],
    },
    "experiments": {
        "exp_001_text_baseline": ["config.yaml", "logs/", "results.json", "report.md"],
        "exp_002_image_gan": ["train.ipynb", "samples/", "metrics/"],
        "exp_003_multimodal_fusion": ["fusion_train.py", "tensorboard/"],
    },
    "notebooks": [
        "data_exploration.ipynb",
        "tokenization_tests.ipynb",
        "model_debugger.ipynb",
        "multimodal_visuals.ipynb",
        "performance_comparison.ipynb",
    ],
    "research": {
        "literature_reviews": ["attention_research.md", "diffusion_review.md"],
        "theoretical": ["scaling_laws.md", "loss_landscape_study.md"],
        "experiments_notes": ["ablation_studies.xlsx", "optimizer_trials.md"],
        "future_scope": ["unified_model_vision.md", "reasoning_extension.md"],
    },
    "models": {
        "checkpoints": ["text/", "image/", "multimodal/"],
        "pretrained": ["tokenizer/", "embeddings/"],
        "exports": ["vermeil_v1/", "vermeil_v1.1/"],
    },
    "analytics": {
        "dashboards": ["wandb_dashboard_link.md"],
        "reports": ["performance_plotter.py", "fid_score_visuals.py"],
        "visualizations": ["confusion_matrix.png", "attention_map.png"],
    },
    "deployment": {
        "api": {
            "routes": ["text.py", "image.py", "multimodal.py"],
            "_files": ["app.py"]
        },
        "gradio_ui": ["demo_interface.py"],
        "docker": ["Dockerfile", "compose.yaml"],
        "ci_cd": ["github_actions.yaml", "deployment_pipeline.yaml"],
        "fastapi_app": ["main.py", "schemas.py", "utils.py"],
    },
    "governance": [
        "changelog.md",
        "version_tracking.xlsx",
        "dependencies_audit.md",
        "dataset_ethics.md",
        "license_compliance.md",
        "security_notes.md",
    ],
    "tools": {
        "profiling": ["memory_profiler.py", "flops_counter.py"],
        "dataset_tools": ["merge_datasets.py", "dataset_summary.py"],
        "optimization": ["quantization_script.py", "pruning_tool.py"],
        "distributed": ["deepspeed_launcher.py", "fsdp_config.yaml"],
        "visualization": ["loss_curve_plotter.py", "gradient_flow_plot.py"],
    },
    "versioning": ["v0.1.md", "v0.2_beta.md", "v1.0_release_notes.md"],
}

# === ROOT FILES ===
root_files = [
    "README.md",
    "LICENSE",
    "setup.py",
    "requirements.txt",
    "pyproject.toml",
    "environment.yml",
    ".gitignore",
    ".gitattributes",
    "dvc.yaml",
    "Makefile",
]

# === UTILITY FUNCTIONS ===
def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file(path):
    open(path, "a").close()

def build_tree(base, tree):
    """
    Recursively build directories and files
    """
    for key, value in tree.items():
        if isinstance(value, dict):
            # if key starts with underscore, files inside folder
            if key == "_files":
                for file in value:
                    create_file(os.path.join(base, file))
            else:
                dir_path = os.path.join(base, key)
                make_dir(dir_path)
                build_tree(dir_path, value)
        elif isinstance(value, list):
            dir_path = os.path.join(base, key)
            make_dir(dir_path)
            for item in value:
                if item.endswith("/"):
                    make_dir(os.path.join(dir_path, item))
                else:
                    create_file(os.path.join(dir_path, item))
        else:
            # single file
            create_file(os.path.join(base, key))

# === MAIN SCRIPT ===
def main():
    base_path = os.path.join(os.getcwd(), PROJECT_NAME)
    make_dir(base_path)

    # Root files
    for file in root_files:
        create_file(os.path.join(base_path, file))

    # Build full hierarchy
    build_tree(base_path, structure)

    print(f"✅ Successfully created full structure for: {PROJECT_NAME}")
    print(f"📁 Location: {base_path}")

if __name__ == "__main__":
    main()
