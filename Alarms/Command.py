from interfaces import Alarm
import subprocess, shlex, atexit
from time import sleep

class Command(Alarm):

  def __init__(self, config):
    Alarm.__init__(self, config)
    base = self.config['command'].split()[0]
    if subprocess.call("which " + base + " >/dev/null", shell=True) != 0:
      raise Exception("install '%s' first" % (base))
    self.proc = None
    if not self.config.has_key('timeout'):
      self.config['timeout'] = None
    atexit.register(self.kill)

  def command(self):
    return self.config['command']

  def ring(self, event):
    command = self.command()
    if isinstance(command, basestring):
      command = shlex.split(self.command())
    args = command + [event]
    #print args
    try:
      self.proc = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
      if self.config['timeout'] > 0:
        sleep(self.config['timeout'])
        return self.proc.poll() is None
    except Exception:
      self.kill()
    return False

  def ringing(self):
    if self.proc is None:
      return False
    return self.proc.poll() is None

  def kill(self):
    try:
      self.proc.kill()
    except:
      pass
