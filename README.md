# Gene Expression Distance and Heatmap Pipeline

---

## Overview

This repository implements a minimal, explicit, and reproducible pipeline to compute and visualize sample-to-sample distances in gene expression data.

The pipeline formalizes a critical exploratory step in transcriptomics: making the geometric relationships between samples explicit before clustering or dimensionality reduction.

This repository is designed as a didactic and structural example of the distance exploration stage that precedes clustering and dimensionality reduction in gene expression analysis pipelines.


> How similar or different are the samples, numerically, in the full expression space?


---

## What this pipeline does

1. Loads a raw gene expression count matrix
2. Normalizes counts to CPM (Counts Per Million)
3. Applies log2(x + 1) transformation
4. Computes a sample-to-sample distance matrix
5. Saves the distance matrix as a versioned artifact
6. Generates a heatmap visualization of the distance matrix

---

## Why this matters

Many multivariate methods (PCA, clustering, UMAP, etc.) are based on distances between samples.

However, in practice:

    • Distances are rarely inspected directly
    • Problems like batch effects, outliers, or scale issues can remain hidden
    • Clustering or PCA can look “clean” while being numerically misleading

This project makes the distance structure itself a first-class object of analysis by explicitly exposing:

    • Which samples are close to each other
    • Which samples are far apart
    • Whether groups actually exist in the raw geometry of the data

---

## What this project is NOT

    • This is not a differential expression analysis
    • This is not a clustering pipeline
    • This is not a dimensionality reduction pipeline

It is strictly a distance computation and visualization step that sits before those analyses.

---

## Conceptual focus

> Before projecting or clustering data, you should understand the geometry of the space you are working in.

---

## Project structure

```text
gene-expression-distance-heatmap/
├── data/
│   └── raw/
│       └── counts.csv
├── pipeline/
│   ├── __init__.py
│   ├── io.py
│   ├── normalization.py
│   ├── transform.py
│   ├── distance.py
│   └── plots.py
├── outputs/
│   ├── matrices/
│   └── figures/
├── run_pipeline.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Outputs

The pipeline produces the following versionable artifacts:

```text
outputs/matrices/sample_distance_matrix.csv
outputs/figures/distance_heatmap.png
```

• The CSV contains the full pairwise distance matrix between samples
• The PNG is a heatmap visualization of that matrix

---

## How to run

1. Install dependencies: ```pip install -r requirements.txt```

2. Run the pipeline: ```python run_pipeline.py```


All outputs will be written to the ```outputs/``` folder.

---

## Reproducibility

All steps in this pipeline are:

    • Explicit
    • Deterministic
    • Scripted
    • And produce versionable artifacts

The pipeline is fully deterministic and produces explicit, versionable artifacts, making every transformation step auditable and reproducible.

---

## Data note

The data used in this repository are synthetic and intended solely to demonstrate:

    • The numerical behavior of the pipeline
    • The structure of the workflow
    • The geometry of sample relationships

They are not intended for biological interpretation.

---

## License

This project is released under the MIT License.