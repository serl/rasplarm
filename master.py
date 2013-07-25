from config import config
import signal

def create_class(name):
  mod = __import__(name)
  cls = getattr(mod, name)
  return cls()

class Master:

  def __init__(self):
    self.calendars = {}
    for k in config["Calendars"].keys():
      self.calendars[k] = create_class(k)
    if not len(self.calendars):
      print "Warning: No calendars configured"

    self.alarms = {}
    for k in config["Alarms"].keys():
      self.alarms[k] = create_class(k)
    if not len(self.alarms):
      print "Warning: No alarms configured"

    self.past_event = {}

  def check(self):
    events_to_fire = []
    for k, cal in self.calendars.items():
      current_event = cal.check()
      past_event = self.past_event[k] if self.past_event.has_key(k) else None
      if current_event != None and current_event != past_event:
        events_to_fire.append(current_event)
        self.past_event[k] = current_event

    if len(events_to_fire):
      events_to_fire.sort()
      self.ring_start(events_to_fire[0])

  def ring_start(self, event):
    for k, alarm in self.alarms.items():
      if not alarm.ringing():
        alarm.ring(event)

  def ring_stop(self):
    for k, alarm in self.alarms.items():
      alarm.kill()

  def ring_snooze(self):
    self.ring_stop()
    signal.signal(signal.SIGALRM, self.sigalarm_handler)
    signal.alarm(config['snooze_minutes']*60)

  def sigalarm_handler(self, signum, frame):
    self.ring_start("snooze")

if __name__ == "__main__":
  from time import sleep
  m = Master()
  m.check()
  sleep(2)
  m.check()
  sleep(2)
  m.check()
  sleep(1)
