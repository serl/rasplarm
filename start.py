from apscheduler.scheduler import Scheduler
from master import Master

m = Master()

scheduler = Scheduler(standalone=True)
scheduler.add_interval_job(m.check,seconds=20)
scheduler.start() #runs the program on an interval of 5 seconds
