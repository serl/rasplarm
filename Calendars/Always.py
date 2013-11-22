from interfaces import Calendar
from time import gmtime, strftime

class Always(Calendar):

  def check(self):
    return strftime('%Y-%m-%d %H:%M//always', gmtime())
   