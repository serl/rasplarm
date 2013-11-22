from interfaces import Alarm
import subprocess, shlex, atexit

class Command(Alarm):

  def __init__(self, config):
    Alarm.__init__(self, config)
    base = self.config['command'].split()[0]
    if subprocess.call("which " + base + " >/dev/null", shell=True) != 0:
      raise Exception("install '%s' first" % (base))
    self.proc = None
    atexit.register(self.kill)

  def command(self):
    return self.config['command']

  def ring(self, event):
    command = self.command()
    if isinstance(command, basestring):
      command = shlex.split(self.command())
    args = command + [event]
    print args
    try:
      self.proc = subprocess.Popen(args, stdin = subprocess.PIPE, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
    except Exception:
      self.kill()

  def ringing(self):
    if self.proc is None:
      return False
    return self.proc.poll() is None

  def kill(self):
    if self.proc is not None:
      self.proc.kill()
