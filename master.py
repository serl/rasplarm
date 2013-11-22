from config import config
import signal

def create_class(mod_name, cls_name, config):
  mod = __import__(mod_name + "." + cls_name)
  submod = getattr(mod, cls_name)
  cls = getattr(submod, cls_name)
  return cls(config)

class Master:

  def __init__(self):
    self.calendars = []
    self.alarms = []

    for t in ["Calendars", "Alarms"]:
      for conf in config[t]:
        instance = create_class(t, conf['type'], conf)
        if t is "Calendars":
          self.calendars.append(instance)
        elif t is "Alarms":
          self.alarms.append(instance)

    if not len(self.calendars):
      print "Warning: No calendars configured"
    if not len(self.alarms):
      print "Warning: No alarms configured"

    self.past_event = {}
    self.latest_event = ""

  def check(self):
    events_to_fire = []
    for k, cal in enumerate(self.calendars):
      current_event = cal.check()
      past_event = self.past_event[k] if self.past_event.has_key(k) else None
      if current_event != None and current_event != past_event:
        events_to_fire.append(current_event)
        self.past_event[k] = current_event

    if len(events_to_fire):
      events_to_fire.sort()
      self.ring_start(events_to_fire[0])

  def ring_start(self, event):
    self.latest_event = event
    for alarm in self.alarms:
      if alarm.start(event):
        break

  def ring_stop(self):
    signal.alarm(0) #disables snooze
    for alarm in self.alarms:
      alarm.kill()

  def ring_snooze(self):
    self.ring_stop()
    signal.signal(signal.SIGALRM, self.sigalarm_handler)
    signal.alarm(config['snooze_minutes']*60)

  def sigalarm_handler(self, signum, frame):
    self.ring_start(self.latest_event)

if __name__ == "__main__":
  from time import sleep
  m = Master()
  m.check()
  sleep(2)
  m.check()
  sleep(2)
  m.check()
  sleep(1)
