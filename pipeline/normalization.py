import pandas as pd

def cpm(counts: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize raw counts to CPM (Counts per Million).

    Input:
    • rows = genes
    • columns = samples

    Outputs:
    • CPM-normalized matrix with same shape.
    """

    library_sizes = counts.sum(axis=0)
    cpm_matrix = counts.div(library_sizes, axis=1) * 1e6
    return cpm_matrix