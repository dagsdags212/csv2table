import unittest
import polars as pl
from csv2table.helpers import *
from csv2table._data import *


class TestHelpers(unittest.TestCase):
    """Test suit for helper functions."""

    def setUp(self):
        self.outfile = write_to_tmp(fetch_sample_csv())
        self.df = pl.read_csv(self.outfile)

    def test_filter_rows_default(self):
        """Expected to return the same input DataFrame."""
        df = filter_df_by_row_index(self.df)
        self.assertIsInstance(df, pl.DataFrame)
        self.assertTupleEqual(self.df.shape, df.shape)

    def test_filter_rows_without_start(self):
        """Expected to return a DataFrame subset starting at index `start`."""
        start, end = None, 10
        df = filter_df_by_row_index(self.df, start, end)
        self.assertIsInstance(df, pl.DataFrame)
        self.assertEqual(df.shape[0], end)

    def test_filter_rows_without_end(self):
        """Expected to return a DataFrame subset starting at index `start`."""
        start, end = 20, None
        df = filter_df_by_row_index(self.df, start, end)
        self.assertIsInstance(df, pl.DataFrame)
        self.assertEqual(df.shape[0], self.df.shape[0] - start)

    def test_filter_rows_with_invalid_indices(self):
        """Expected to raise an IndexError."""
        # invalid start value
        start, end = -1, 10
        with self.assertRaises(IndexError):
            df = filter_df_by_row_index(self.df, start, end)
            print(df)
        # invalid end value
        start, end = 10, -1
        with self.assertRaises(IndexError):
            filter_df_by_row_index(self.df, start, end)
        # invalid start and end values
        start, end = -10, 1000
        with self.assertRaises(Exception):
            filter_df_by_row_index(self.df, start, end)

    def tearDown(self):
        self.outfile.unlink()
