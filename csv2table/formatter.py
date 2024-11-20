import polars as pl
from great_tables import GT


def tabulate(data: pl.DataFrame, **kwargs):
    """Convert DataFrame into a GreatTable object."""
    tbl = GT(data)
    if "title" in kwargs and "subtitle" in kwargs:
        tbl = tbl.tab_header(title=kwargs["title"], subtitle=kwargs["subtitle"])
    elif "title" in kwargs:
        tbl = tbl.tab_header(title=kwargs["title"])
    # Cannot add a subtitle without a provided title
    # Warns the user but does not raise an error. Value is discarded.
    elif "subtitle" in kwargs:
        print("Cannot add subtitle without a title. Discarding subtitle...")
    if "footer" in kwargs:
        tbl = tbl.tab_source_note(source_note=kwargs["footer"])
    return tbl
