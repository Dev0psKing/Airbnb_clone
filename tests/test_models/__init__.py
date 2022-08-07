#!/usr/bin/python3
"""
Unit tests for <file>
Run with: python -m unittest test_module
"""
import unittest
from models.something import something

class TestBaseModel(unittest.TestCase):
    """
    Generic testing class for a template
    Functions:
    something()
    """
    def something(self):
        """
        Generic Something function
        """
        self.do_something()

if __name__ == "__main__":
    unittest.main()
