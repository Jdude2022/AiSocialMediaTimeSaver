"""Basically the bass class the named ones will be built on tope of.

Named classes will extend the functionality of this, however this will have 
base functionality for additional user generated sites. Factory should be able
to construct aditional classes from the info here, it will just not be api
tailred..

Author: John Jalali
Ver: 0.1
"""
import datetime
from datetime import date
from typing import List

class SocialBase:
    def __init__(self, db: dict):
        """Populates the diction with curr + 90."""
        self._db = db
        current_date = date.today()
        current_date_converted = current_date.strftime('%a %d %b %Y')
        if current_date_converted not in self._db.keys():
            for i in range(90):
                current_date_converted = current_date.strftime('%a %d %b %Y') 
                self._db[current_date_converted] = [[]]
                current_date = current_date + datetime.timedelta(days=1)

    def month_view(self, req_date: str) -> List[str]:
        """Prints out the current month calander."""
        # Get current Month.
        split_date = req_date.split(" ")
        desired_month = split_date[2]
        month_range: List[str] = list()
        if desired_month in self._db.keys():
            month_range.append()
            pass
            # Find first of the month.

            # Populate the List until the next month.

        # return the List

    def week_view(self, date: str) -> List:
        """Prints out the current week calander."""
        pass

    def day_view(self, date: str) -> List:
        """Prints out the current day calander."""
        pass

    def gen_thirty(self, date: str) -> None:
        """Generates 30 days."""
        pass

    def signal(self) -> bool:
        """If db is populated True, else False."""
        pass
