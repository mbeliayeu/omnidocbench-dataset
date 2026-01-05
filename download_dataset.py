#!/usr/bin/env python3
"""Download OmniDocBench dataset from HuggingFace"""

from datasets import load_dataset
import os

print("Downloading OmniDocBench dataset...")
print("This may take a while depending on the dataset size...")

try:
    # Load the dataset
    dataset = load_dataset("opendatalab/OmniDocBench", trust_remote_code=True)

    # Save the dataset to disk
    dataset.save_to_disk("./OmniDocBench")

    print(f"\nDataset downloaded successfully!")
    print(f"Dataset info: {dataset}")

except Exception as e:
    print(f"Error downloading dataset: {e}")
    print("\nTrying alternative method with snapshot_download...")

    from huggingface_hub import snapshot_download

    # Download the entire repository
    snapshot_download(
        repo_id="opendatalab/OmniDocBench",
        repo_type="dataset",
        local_dir="./OmniDocBench",
        local_dir_use_symlinks=False
    )

    print("Dataset downloaded successfully using snapshot_download!")
