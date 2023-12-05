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


class SocialBase:
    def __init__(self, db: dict):
        """Populates the diction with curr + 90."""
        self._db = db
        current_date = date.today()
        if current_date not in self._db.keys():
            for i in range(90):
                current_date
                current_date_converted = current_date.strftime('%a %d %b %Y') 
                self._db[current_date_converted] = [[]]
                current_date = current_date + datetime.timedelta(days=1)

# fake_dic = dict()

# base = SocialBase(fake_dic)
# for key in fake_dic.keys():
#     print(key)
