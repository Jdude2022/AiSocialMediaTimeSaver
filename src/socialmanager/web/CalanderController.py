"""Page controller for social media manager.

Author John Jalali jjalali@ksu.edu
Version 0.1
"""
from flask import render_template, request
from flask_classful import FlaskView, route  # type: ignore
from src.socialmanager.data.planner.Generator import Generator
from typing import List


class CalanderController:
    """Controlls the calander."""
    route_base = "/"

    @route('/')
    def index(self):
        """Load app index page."""
        return render_template("index.html")
    
    @route('mediamanager')
    def media_manager(self):
        db = Generator.connect()
