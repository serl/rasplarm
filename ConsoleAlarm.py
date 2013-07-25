from interfaces import Alarm

class ConsoleAlarm(Alarm):

  def ring(self, event):
    print event
