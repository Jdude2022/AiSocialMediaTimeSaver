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
# fake_dic = dict()

# base = SocialBase(fake_dic)
# for key in fake_dic.keys():
#     print(key)
    def month_view(self, date: str) -> List:
        """Prints out the current month calander."""
        pass

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
