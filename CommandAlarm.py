from interfaces import Alarm
import random, os, os.path

class CommandAlarm(Alarm):

  def __init__(self):
    Alarm.__init__(self)
    if os.system("which " + self.config['command'].split()[0] + " >/dev/null") != 0:
      raise Exception("install '%s' first" % (self.config['command']))

  def command(self):
    return self.config['command']

  def ring(self, event):
    command = "%s '%s'" % (self.command(), event)
    os.system(command)

if __name__ == "__main__":
  a = CommandAlarm()
  a.ring("event")
