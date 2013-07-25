from interfaces import Calendar
from time import gmtime, strftime

class AlwaysCalendar(Calendar):

  def __init__(self):
    Calendar.__init__(self)

  def check(self):
    return strftime('%Y-%m-%d %H:%M//always', gmtime())
   