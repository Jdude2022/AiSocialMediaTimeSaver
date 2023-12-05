"""Web gui for the Social Media manager.

Author John Jalali jjalali@ksu.edu
Version 0.1
"""
from flask import Flask
from typing import List
from src.socialmanager.web.CalanderController import CalanderController

class Web:
    """Enables use of web."""
    @staticmethod
    def main(args: List[str]):
        """Main method."""
        app = Flask(__name__)
        CalanderController.register(app)
        return app
