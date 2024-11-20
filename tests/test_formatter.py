import unittest
from pathlib import Path
import polars as pl
from great_tables import GT
from csv2table.formatter import *


class TestFormatter(unittest.TestCase):
    """Test suite for formatting functions."""

    def setUp(self) -> None:
        """Creates a temporary csv file."""
        outfile = Path("/tmp/test.csv")
        with outfile.open("w") as out:
            out.write("name,age,email\n")
            out.write("Jane,28,jane@email.com\n")
            out.write("Chris,34,chris@email.com\n")
            out.write("Laura,40,laura@email.com\n")

        assert outfile.exists()
        self.df = pl.read_csv(outfile)

    def test_tabulate_default(self):
        """Expected to return a GT object."""
        tbl = tabulate(self.df)
        self.assertIsInstance(tbl, GT)
        self.assertIsNone(tbl._heading.title)
        self.assertIsNone(tbl._heading.subtitle)
        self.assertEqual(len(tbl._source_notes), 0)

    def test_tabulate_with_title(self):
        """Expected to return a GT object with a tab header containing a title."""
        tbl = tabulate(self.df, title="This is a title")
        self.assertIsInstance(tbl._heading.title, str)
        self.assertIsNone(tbl._heading.subtitle)
        self.assertEqual(len(tbl._source_notes), 0)

    def test_tabulate_with_subtitle(self):
        """Expected to return a GT object with a tab header containing None values
        for both title and subtitle."""
        tbl = tabulate(self.df, subtitle="This is a subtitle")
        self.assertIsNone(tbl._heading.title)
        self.assertIsNone(tbl._heading.subtitle)
        self.assertEqual(len(tbl._source_notes), 0)

    def test_tabulate_with_footer(self):
        """Expected to return a GT object with a tab source note containing a footer."""
        tbl = tabulate(self.df, footer="This is a footer")
        self.assertIsNone(tbl._heading.title)
        self.assertIsNone(tbl._heading.subtitle)
        self.assertEqual(len(tbl._source_notes), 1)
        self.assertIsInstance(tbl._source_notes[0], str)

    def tearDown(self) -> None:
        """Deletes the temporary csv file."""
        outfile = Path("/tmp/test.csv")
        if outfile.exists():
            outfile.unlink()
