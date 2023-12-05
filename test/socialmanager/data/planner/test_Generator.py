"""Test battery for the db dictionary.

Author: John Jalali JJalali@ksue.edu
Version: 0.1
"""
from src.socialmanager.data.planner.Generator import Generator
import pytest


class TestGenerator:
    """Db test suite."""
    db: dict = Generator
    db = db.connect()

    def test_true_is_true(self):
        """Makes sure tests work."""
        assert True == True
    
    def test_can_connect(self):
        """Attempts to connect to generator."""
        try:
            db: dict = Generator.connect()
        except Exception:
            pytest.fail("Database not connecting...")

    def test_examples_included_key(self):
        """Make sure base fields are populated."""
        db = Generator.connect()
        assert "date" in db.keys()

    def test_example_included_data(self):
        """Tests to make sure base items included after key."""
        assert self.db["date"][0] == ["Social Name", "Topic", "Post"]

    def test_adding_items_works(self):
        """Adds a key to db."""
        self.db["test 2"] = "Pass"
        assert self.db["test 2"] == "Pass"

    def test_append_to_example(self):
        """Tests if you can append to a current example."""
        self.db["date"].append(["Test social", "Test Topic", "Test Post"])
        assert self.db["date"][1] == ["Test social", "Test Topic", "Test Post"]

    def test_cant_overwrite(self):
        """Tests if class is singleton."""
        db = Generator.connect()
        db["date"] = "three"
        db2 = Generator.connect()
        assert db2["date"] == "three"
