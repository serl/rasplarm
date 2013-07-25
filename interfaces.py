from config import config

class Calendar:
  "abstract class for calendar"

  def __init__(self):
    "construct using config options"
    self.config = config["Calendars"][self.__class__.__name__]

  def check(self):
    """check if some events match with current time,
    should return an almost-unique string (to avoid double-firing of alarms)
    usually should be "time//label". and yes, time should be orderable """
    raise NotImplementedError("Should have implemented this")


class Alarm:
  "abstract class for alarm action"

  def __init__(self):
    "construct using config options"
    self.config = config["Alarms"][self.__class__.__name__]

  def ring(self, events):
    "run when event occurs"
    raise NotImplementedError("Should have implemented this")
