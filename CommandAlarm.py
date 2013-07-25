from interfaces import Alarm
import subprocess, shlex, atexit

class CommandAlarm(Alarm):

  def __init__(self):
    Alarm.__init__(self)
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
      self.proc = subprocess.Popen(args, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    except Exception:
      self.kill()

  def ringing(self):
    if self.proc is None:
      return False
    return self.proc.poll() is None

  def kill(self):
    if self.proc is not None:
      self.proc.kill()

if __name__ == "__main__":
  from time import sleep
  a = CommandAlarm()
  a.ring("event")
  sleep(60)
