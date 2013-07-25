from interfaces import Alarm

class ConsoleAlarm(Alarm):

  def ring(self, event):
    print event

  def ringing(self):
    return False

  def kill(self):
    pass
