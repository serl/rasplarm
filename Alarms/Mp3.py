from Command import Command
import random, os, os.path, shlex

class Mp3(Command):

  def __init__(self, config):
    Command.__init__(self, config)
    if self.config.has_key('directory') and not os.path.isdir(self.config['directory']):
      raise Exception("directory '%s' does not exists" % (self.config['directory'],))
    if self.config.has_key('directory') and not os.listdir(self.config['directory']):
      raise Exception("directory '%s' is empty" % (self.config['directory'],))

  def command(self):
    command = shlex.split(self.config['command'])
    command += [os.path.join(self.config['directory'], random.choice(os.listdir(self.config['directory'])))]
    return command

if __name__ == "__main__":
  from time import sleep
  a = Mp3()
  a.ring("event")
  sleep(60)
