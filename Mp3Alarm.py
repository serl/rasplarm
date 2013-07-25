from interfaces import Alarm
import random, os, os.path

class Mp3Alarm(Alarm):

  def __init__(self):
    Alarm.__init__(self)
    if self.config.has_key('directory') and not os.path.isdir(self.config['directory']):
      raise Exception("directory '%s' does not exists" % (self.config['directory'],))
    if self.config.has_key('directory') and not os.listdir(self.config['directory']):
      raise Exception("directory '%s' is empty" % (self.config['directory'],))
    if self.config.has_key('file') and not os.path.isfile(self.config['file']):
      raise Exception("file '%s' does not exists" % (self.config['file'],))
    if os.system("which " + self.config['command'] + " >/dev/null") != 0:
      raise Exception("install '%s' first" % (self.config['command']))

  def get_file(self):
    if self.config.has_key('directory'):
      songfile = os.path.join(self.config['directory'], random.choice(os.listdir(self.config['directory'])))
    elif self.config.has_key('file'):
      songfile = self.config['file']
    return songfile

  def ring(self, event):
    command ="%s '%s' " % (self.config['command'], self.get_file(),)
    if self.config.has_key('arguments'):
      command += self.config['arguments']
 
    print command
    os.system(command)

if __name__ == "__main__":
  a = Mp3Alarm()
  a.ring("event")
