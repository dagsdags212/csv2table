import polars as pl
from great_tables import GT


def tabulate(data: pl.DataFrame, **kwargs):
    """Convert DataFrame into a GreatTable object."""
    tbl = GT(data)
    if "title" in kwargs:
        tbl = tbl.tab_header(title=kwargs["title"])
    if "subtitle" in kwargs:
        tbl = tbl.tab_header(title=kwargs["subtitle"])
    if "footer" in kwargs:
        tbl = tbl.tab_source_note(source_note=kwargs["footer"])
    return tbl
