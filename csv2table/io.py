from pathlib import Path
import polars as pl
from great_tables import GT
from csv2table.validation import _validate_filepath


def read_csv(filepath: str | Path) -> pl.DataFrame:
    """Loads a csv file into memory as a DataFrame if given file path is valid."""
    filepath = _validate_filepath(filepath)
    return pl.read_csv(filepath)


def save_table(tbl: GT, outpath: str | Path, **kwargs) -> None:
    if isinstance(outpath, str):
        outpath = Path(outpath)

    options = {"encoding": "utf-8"}
    if "scale" in kwargs:
        options.update({"scale": kwargs["scale"]})

    # TODO: assert path extension is valid
    print(f"Saving to {outpath} as a {outpath.stem} file")
    tbl.save(outpath, **options)
