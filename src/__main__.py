"""Main Project file.

Social media manager. 

Author : John Jalali jjalali@ksu.edu
Version 0.1
"""

import sys
from src.socialmanager.web.Web import Web
app = Web.main(sys.argv)
app.run()
