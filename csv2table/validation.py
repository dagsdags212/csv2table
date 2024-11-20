from pathlib import Path


def _validate_filepath(filepath: str | Path) -> Path:
    """Returns a Path object if the given file path exists."""
    if isinstance(filepath, str):
        filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError("invalid file path")
    return filepath
