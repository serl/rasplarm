class Alarm:
  "abstract class for alarm action"

  def __init__(self, config):
    "construct using config options"
    self.config = config

  def ring(self, event):
    "run when event occurs"
    raise NotImplementedError("Should have implemented this")

  def ringing(self):
    "return False if you don't fear overlap"
    raise NotImplementedError("Should have implemented this")

  def kill(self):
    "run when snooze event arrives"
    raise NotImplementedError("Should have implemented this")
