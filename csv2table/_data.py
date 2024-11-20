from pathlib import Path
import httpx


def fetch_sample_csv() -> str:
    """Fetches a csv file from GitHub and returns its contents as a string."""
    URL = "https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv"
    r = httpx.get(URL)
    r.raise_for_status()
    return r.text

def write_to_tmp(s: str) -> Path:
    """Writes a string to a temporary file and returns its path."""
    outfile = Path("/tmp/sample.csv")
    with outfile.open("w") as f:
        f.write(s)
    assert outfile.exists(), f"failed to write contents to {outfile}"
    return outfile
