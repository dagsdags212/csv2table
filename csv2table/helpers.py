from typing import Optional
import polars as pl


def filter_df_by_row_index(
    df: pl.DataFrame, start: Optional[int] = None, end: Optional[int] = None
):
    """Return a subset of the data, starting from `start` and ending at `end`"""
    nrows, _ = df.shape
    match (start, end):
        case (None, None):
            return df
        case (0, nrows):
            return df
        case (start, None):
            return df[start:, :]
        case (None, end):
            return df[:end, :]
        case (start, end):
            return df[start:end, :]
        case _:
            raise IndexError("cannot subset data with given indices")
