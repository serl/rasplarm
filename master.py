from config import config

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
      for k, alarm in self.alarms.items():
        alarm.ring(events_to_fire[0])

if __name__ == "__main__":
  m = Master()
  m.check()
  m.check()
  m.check()
