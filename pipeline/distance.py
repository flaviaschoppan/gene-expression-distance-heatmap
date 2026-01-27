import pandas as pd
from scipy.spatial.distance import pdist, squareform

def compute_sample_distance(matrix: pd.DataFrame, metric: str = "euclidean") -> pd.DataFrame:
    """
    Compute a sample-by-sample distance matrix from an expression matrix.

    Input:
        matrix: pd.DataFrame
            • rows = genes
            • columns = samples
    
    Outout:
        dist_df: pd.DataFrame
            • rows = samples
            • columns = samples
            • values = pairwise distances
    """

    # --------------------------------------------------
    # Transpose: rows = samples, columns = genes
    # --------------------------------------------------
    X = matrix.T

    # --------------------------------------------------
    # Compute pairwise distances
    # --------------------------------------------------
    dist_array = pdist(X, metric=metric)
    dist_matrix = squareform(dist_array)

    # --------------------------------------------------
    # Compute pairwise distances
    # --------------------------------------------------
    dist_array = pdist(X, metric = metric)
    dist_matrix = squareform(dist_array)

    # --------------------------------------------------
    # Build Labeled DataFrame
    # --------------------------------------------------
    dist_df = pd.DataFrame(
        dist_matrix,
        index=X.index,
        columns=X.index 
    )

    return dist_df
