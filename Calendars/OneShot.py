from interfaces import Calendar
from time import gmtime, strftime

class OneShot(Calendar):

  def __init__(self, config):
    Calendar.__init__(self, config)
    self.done = False

  def check(self):
    if not self.done:
      self.done = True
      return strftime('%Y-%m-%d %H:%M//oneshot', gmtime())
    return None
   