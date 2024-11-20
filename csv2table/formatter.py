import polars as pl
from great_tables import GT


def clean_headers(headers: list[str]) -> list[str]:
    """Replaces word delimiters with whitespaces and sets casing to title."""

    def convert_to_whitespace(s: str):
        for delim in ["_", "-", "|", ",", "."]:
            s = s.replace(delim, " ")
        return s

    spaced_header = map(convert_to_whitespace, headers)
    title_case = map(str.title, spaced_header)
    return list(title_case)


def tabulate(data: pl.DataFrame, **kwargs):
    """Convert DataFrame into a GreatTable object."""
    data.columns = clean_headers(data.columns)
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
