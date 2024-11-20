import unittest
import polars as pl
from csv2table.io import *


class TestIO(unittest.TestCase):
    """Test suite for IO functions."""

    def setUp(self) -> None:
        """Creates a temporary csv file."""
        outfile = Path("/tmp/test.csv")
        with outfile.open("w") as out:
            out.write("name,age,email\n")
            out.write("Jane,28,jane@email.com\n")
            out.write("Chris,34,chris@email.com\n")
            out.write("Laura,40,laura@email.com\n")

        assert outfile.exists()

    def test_read_csv_func(self):
        """Expects to load csv file as a DataFrame object."""
        path = Path("/tmp/test.csv")
        df = read_csv(path)
        self.assertIsInstance(df, pl.DataFrame)
        self.assertTupleEqual(df.shape, (3, 3))

    def save_table(self):
        """Expects a file to be written in specified path."""
        pass

    def tearDown(self) -> None:
        """Deletes the temporary csv file."""
        outfile = Path("/tmp/test.csv")
        if outfile.exists():
            outfile.unlink()
