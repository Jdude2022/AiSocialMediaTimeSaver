"""General stuff with insta log in here. 

Insta has a schedule that looks interesting.
"""
from src.socialmanager.data.socials.SocialBase import SocialBase
from src.socialmanager.data.dbs.other_dbs.RandomTopics import RandomTopics
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

    def make_post(self, input: str, date: str) -> None:
        """Method to write a social media post.
        
        input: Text to be added to the database
        date: Date of where the post goes to the database.
        """
        self._db[date][3] = input
    
    def change_topic(self, input: str, date: str) -> None:
        """Method to write the topic to the db.
        
        input: Topic off the day.
        date: Date to post the topic
        """
        self._db[date][2] = input

    def random_topic(self, date: str) -> None:
        """Populates a radnom topic for the day."""
        topic_roulte: RandomTopics = RandomTopics()
