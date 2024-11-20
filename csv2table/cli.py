from pathlib import Path
import click
import polars as pl
from csv2table.io import read_csv, save_table
from csv2table.formatter import tabulate
from csv2table.helpers import filter_df_by_row_index
from csv2table.config import SPAN, SCALE


@click.group()
def main():
    """Convert csv files into beautiful tables."""
    pass


@click.command(help="display the csv content in a table")
@click.argument("filepath")
@click.option("--start", type=int, default=None, help="start at this row index")
@click.option("--end", type=int, default=None, help="end at this row index")
@click.option("--head", is_flag=True, help="display first 10 rows")
@click.option("--tail", is_flag=True, help="display last 10 rows")
def view(filepath, start, end, head, tail) -> None:
    """Writes rows of a tabulated csv file to stdout."""
    filepath = Path(filepath).absolute()
    df = read_csv(filepath)
    nrows, _ = df.shape

    if head and tail:
        raise ValueError(
            "cannot pass both `--head` and `--tail` flags at the same time"
        )
    # display first 10 rows
    if head:
        with pl.Config(tbl_rows=10):
            print(df.head(10))
            return
    # disply last 10 rows
    if tail:
        with pl.Config(tbl_rows=10):
            print(df.tail(10))
            return

    if start or end:
        # deal with empty values
        match (start, end):
            case (start, None):
                end = start + SPAN
            case (None, end):
                start = end - SPAN
        # deal with invalid values
        assert end > start, f"end value must be greater than start value"
        assert start >= 0 and start < nrows, f"start must be between 0 and {nrows}"
        assert end > 0 and end < nrows, f"end must be between 1 and {nrows}"
        # display the subsetted data
        with pl.Config(tbl_rows=end - start):
            subset = filter_df_by_row_index(df, start, end)
            print(subset)
            return
    # default is to print the first 10 rows
    print(df.head(10))


@click.command(help="convert csv into a table")
@click.argument("filepath")
@click.option("-o", "--outfile", required=True, type=Path, help="output file name")
@click.option("--title", type=str, default=None, help="include a table title")
@click.option("--subtitle", type=str, default=None, help="include a table subtitle")
@click.option("--footer", type=str, default=None, help="include a table footer")
def export(filepath, outfile, title, subtitle, footer):
    df = read_csv(filepath)
    ACCEPTED_EXTS = ["png", "bmp", "pdf"]
    # generate path to output
    if outfile.suffix[1:] not in ACCEPTED_EXTS:
        raise ValueError("invalid file extension (must be .png, .mbp, or .pdf)")

    # add optional table fields
    kwargs = {}
    if title:
        kwargs.update(dict(title=title))
    if subtitle:
        kwargs.update(dict(subtitle=subtitle))
    if footer:
        kwargs.update(dict(footer=footer))

    tbl = tabulate(df, **kwargs)
    save_table(tbl, outfile.absolute(), scale=SCALE)


main.add_command(view)
main.add_command(export)

if __name__ == "__main__":
    main()
