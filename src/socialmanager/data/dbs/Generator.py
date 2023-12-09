"""Social media generator.

Just someplace to build the dictionary.

Author: John Jalali
Ver: 0.1
"""
from typing import Optional, Dict


class Generator:
    """Generates the Dictory."""
    _instance: Optional["Generator"] = None
    __db: dict = dict()

    def __init__(self) -> None:
        """Singleton."""
        pass

    def __new__(cls) -> "Generator":
        """There can only be one."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def __build() -> None:
        """Builds the dictionary.
        
        keys: Wed 21 Feb 2024
        vals: [[][Social name, topic, Post][social name.., topic..]
        """
        Generator.__db = {"date": [["Social Name", "Topic", "Post"]]}

    @staticmethod
    def connect() -> Dict:
        """Connects to the dictionary."""
        if "date" not in Generator.__db.keys():
            Generator.__build()
        return Generator.__db
