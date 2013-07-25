from apscheduler.scheduler import Scheduler
from master import Master
import signal

m = Master()
m.check()

def snooze_signal(signum, frame):
  m.ring_snooze()
signal.signal(signal.SIGUSR1, snooze_signal)

def stop_signal(signum, frame):
  m.ring_stop()
signal.signal(signal.SIGUSR2, stop_signal)

scheduler = Scheduler(standalone=True)
scheduler.add_interval_job(m.check, seconds=10)
try:
  scheduler.start()
except KeyboardInterrupt:
  pass
