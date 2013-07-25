from interfaces import Alarm
import random, os, os.path

class Mp3Alarm(Alarm):

  def __init__(self):
    Alarm.__init__(self)
    if self.config.has_key('directory') and not os.path.isdir(self.config['directory']):
      raise Exception("directory '%s' does not exists" % (self.config['directory'],))
    if self.config.has_key('directory') and not os.listdir(self.config['directory']):
      raise Exception("directory '%s' is empty" % (self.config['directory'],))
    if os.system("which " + self.config['command'] + " >/dev/null") != 0:
      raise Exception("install '%s' first" % (self.config['command']))

  def ring(self, event):
    command ="%s '%s' " % (self.config['command'], os.path.join(self.config['directory'], random.choice(os.listdir(self.config['directory']))),)
    if self.config.has_key('arguments'):
      command += self.config['arguments']
 
    os.system(command)

if __name__ == "__main__":
  a = Mp3Alarm()
  a.ring("event")
