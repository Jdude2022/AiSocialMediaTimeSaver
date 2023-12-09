"""Test the social base class.


Author: John Jalali JJalali@ksu.edu
version: v0.1
"""
from src.socialmanager.data.socials.SocialBase import SocialBase
from datetime import date
import datetime


class TestSocialBase:
    """Test the social base class, Could use fakes..."""

    def test_true_is_true(self):
        """Asserts true is true."""
        assert True is True

    def test_number_gen(self):
        """Tests the 90 day count."""
        fake_db = dict()
        base = SocialBase(fake_db)
        assert len(fake_db) == 90

    def test_cur_date(self):
        """Test the current date works."""
        fake_db = dict()
        base = SocialBase(fake_db)
        assert date.today().strftime('%a %d %b %Y') in fake_db.keys()

    def test_15_days(self):
        """Test if 15 days have been added to the base."""
        fake_db = dict()
        base = SocialBase(fake_db)
        test_date = date.today() + datetime.timedelta(days=15)
        assert test_date.strftime('%a %d %b %Y') in fake_db.keys()

    def test_30_days(self):
        """Test if 30 days have been added to the base."""
        fake_db = dict()
        base = SocialBase(fake_db)
        test_date = date.today() + datetime.timedelta(days=30)
        assert test_date.strftime('%a %d %b %Y') in fake_db.keys()
