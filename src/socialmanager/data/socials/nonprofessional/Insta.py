"""General stuff with insta log in here. 

Insta has a schedule that looks interesting.
"""
from src.socialmanager.data.socials.SocialBase import SocialBase
from datetime import date


class Insta(SocialBase):
    """Basic info the the site."""
    def __init__(self, db: dict) -> None:
        """Parses db for Insta posts."""
        self._db: dict = db
        super().__init__(self._db)
        self._db["date"].append(["Insta", "Topic", "Post"])
        self.__post_index: int = 0
        for i, item in enumerate(self._db["date"]):
            if item == ["Insta", "Topic", "Post"]:
                self.__post_index = i
                break

    def new_post(self, date: date, text: str) -> None:
        """Creats a new post."""
        self._db[date][self.__post_index][3] = text

    def new_topic(self, date: date, text: str) -> None:
        """Creates new Topic."""
        self._db[date][self.__post_index][2] = text
