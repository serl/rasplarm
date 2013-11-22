from interfaces import Alarm

class Console(Alarm):

  def ring(self, event):
    print event
    return False

  def ringing(self):
    return False

  def kill(self):
    pass
