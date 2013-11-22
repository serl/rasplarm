from Command import Command
import random, os, os.path, shlex

class Mp3(Command):

  def __init__(self, config):
    Command.__init__(self, config)
    if self.config.has_key('directory') and not os.path.isdir(self.config['directory']):
      raise Exception("directory '%s' does not exists" % (self.config['directory'],))
    if self.config.has_key('directory') and not os.listdir(self.config['directory']):
      raise Exception("directory '%s' is empty" % (self.config['directory'],))
    if not self.config.has_key('count'):
      self.config['count'] = 1

  def random_file(self, directory):
    f = os.path.join(directory, random.choice(os.listdir(directory)))
    if os.path.isdir(f):
      return self.random_file(f)
    else:
      return f

  def command(self):
    command = shlex.split(self.config['command'])

    files = []
    for i in range(0, self.config['count']):
      for j in range(0, 5):
        f = self.random_file(self.config['directory'])
        if f in files:
          #print 'S', f
          continue
        files.append(f)
        #print 'A', f
        break

    return command + files
