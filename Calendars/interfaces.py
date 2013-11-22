class Calendar:
  "abstract class for calendar"

  def __init__(self, config):
    "construct using config options"
    self.config = config

  def check(self):
    """check if some events match with current time,
    should return an almost-unique string (to avoid double-firing of alarms)
    usually should be "time//label". and yes, time should be orderable """
    raise NotImplementedError("Should have implemented this")
