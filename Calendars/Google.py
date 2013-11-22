#inspiration from http://www.esologic.com/?p=634

from interfaces import Calendar
from gdata.calendar.service import CalendarService, CalendarEventQuery
from time import strptime, gmtime, strftime

class Google(Calendar):

  def __init__(self, config):
    Calendar.__init__(self, config)
    self.calendar_service = CalendarService()
    self.calendar_service.email = self.config['username']
    self.calendar_service.password = self.config['password']
    self.calendar_service.source = 'Google-Calendar_Python_Sample-1.0'
    self.calendar_service.ProgrammaticLogin()

  def check(self):
    events = []
    for t in self.config['terms']:
      events += self.FullTextQuery(t)
    events.sort()
    return events[0] if len(events) else None

  def FullTextQuery(self, text_query):
    #print 'Full text query for events on Primary Calendar: \'%s\'' % ( text_query,)
    events = []
    query = CalendarEventQuery('default', 'private', 'full', text_query)
    query.singleevents = 'true'
    query.orderby = 'starttime'
    query.sortorder = 'ascending'
    query.futureevents = 'true'
    query.ctz = 'UTC'
    feed = self.calendar_service.CalendarQuery(query)
    comparison_time_format = '%Y-%m-%d %H:%M'
    for i, an_event in enumerate(feed.entry):
      for a_when in an_event.when:
        try:
          event_time = strptime(a_when.start_time, '%Y-%m-%dT%H:%M:%S.000Z')
        except Exception, e:
          continue #all-day events
            
        current_time = gmtime()
        event_time_formatted = strftime(comparison_time_format, event_time)
        current_time_formatted = strftime(comparison_time_format, current_time)
        comparison = event_time_formatted == current_time_formatted

        #print an_event.title.text, "Number:", i, "Event Time:", event_time_formatted, "Current Time:", current_time_formatted, "Comparison:", comparison
 
        if comparison:
          events.append("%s//%s" % (event_time_formatted, an_event.title.text))
    return events
