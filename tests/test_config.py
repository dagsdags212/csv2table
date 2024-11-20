import unittest
from csv2table.config import *


class TestConfigFile(unittest.TestCase):
    """Test suit for default config file."""

    def test_param_span(self):
        """Checks if SPAN constant is set"""
        self.assertIsNotNone(SPAN)
