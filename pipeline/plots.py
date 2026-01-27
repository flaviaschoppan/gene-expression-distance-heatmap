import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Global style for figures
sns.set_theme(style="whitegrid", context="talk")

def plot_distance_heatmap(distance_matrix: pd.DataFrame, outpath: str):
    """
    Plot a heatmap of the sample-to-sample distance matrix.

    Parameters
    ----------
    distance_matrix : pd.DataFrame
        Square distance matrix.
        Index = sample names
        Columns = sample names
    
    outpath : str
        Path where the figure will be saved.
    """

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        distance_matrix,
        cmap="viridis",
        square=True,
        cbar_kws={"label": "Distance"}
    )

    plt.title("Sample-to-sample distance heatmap")
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()