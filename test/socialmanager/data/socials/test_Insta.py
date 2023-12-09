"""Tests for the Instagram class.

Author: John Jalali jjalali@ksu.edu
Version: 0.1
"""
from src.socialmanager.data.dbs.Generator import Generator


class TestInsta:
    """Test battery for the Insta class."""
    db: dict = Generator.connect()

    def test_true_is_true(self):
        """Makes sure pytest works."""
        assert True == True
