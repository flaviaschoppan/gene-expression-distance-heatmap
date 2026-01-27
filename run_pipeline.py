"""
Gene Expression Distance + Heatmap Pipeline

This script implements a minimal and explicit pipeline to:

1. Load raw gene expression counts
2. Normalize counts to CPM
3. Apply log2(x + 1) transformation
4. Compute sample-to-sample distance matrix
5. Save distance matrix
6. Plot distance heatmap

The goal is to make the geometric structure of samples explicit before any clustering or dimensionality reproduction.
"""

from pipeline.io import load_counts
from pipeline.normalization import cpm
from pipeline.transform import log2_transform
from pipeline.distance import compute_sample_distance
from pipeline.plots import plot_distance_heatmap

import os

def main():
    # --------------------------------------------------
    # Create about directories if they don't exist
    # --------------------------------------------------
    os.makedirs("outputs/matrices", exist_ok=True)
    os.makedirs("outputs/figures", exist_ok=True)

    # --------------------------------------------------
    # Step 1 - Load raw data
    # --------------------------------------------------
    print("Loading raw counts...")
    counts = load_counts("data/raw/counts.csv")
    print("✓ Step 1 finished: raw counts loaded\n")

    # ---------------------------------------------------
    # Step 2 — CPM normalization
    # ---------------------------------------------------
    print("Applying CPM normalization...")
    cpm_matrix = cpm(counts)
    print("✓ Step 2 finished: CPM normalization applied\n")

    # ---------------------------------------------------
    # Step 3 — Log2 transformation
    # ---------------------------------------------------
    print("Applying log2 transformation...")
    log_matrix = log2_transform(cpm_matrix)
    print("✓ Step 3 finished: log2 transformation applied\n")

    # ---------------------------------------------------
    # Step 4 — Compute sample distance matrix
    # ---------------------------------------------------
    print("Computing sample-to-sample distance matrix...")
    dist_matrix = compute_sample_distance(log_matrix)
    print("✓ Step 4 finished: distance matrix computed\n")

    # ---------------------------------------------------
    # Step 5 — Save distance matrix
    # ---------------------------------------------------
    print("Saving distance matrix...")
    dist_matrix.to_csv("outputs/matrices/sample_distance_matrix.csv")
    print("✓ Step 5 finished: distance matrix saved\n")

    # ---------------------------------------------------
    # Step 6 — Plot heatmap
    # ---------------------------------------------------
    print("Generating distance heatmap...")
    plot_distance_heatmap(
        dist_matrix,
        outpath="outputs/figures/distance_heatmap.png"
    )
    print("✓ Step 6 finished: heatmap saved\n")

    print("Pipeline finished successfully.")


if __name__ == "__main__":
    main()