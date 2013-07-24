#inspiration from http://www.esologic.com/?p=634

import config
import os, time
import gdata.calendar.service
from apscheduler.scheduler import Scheduler

calendar_service = gdata.calendar.service.CalendarService()
calendar_service.email = config.gdata['username']
calendar_service.password = config.gdata['password']
calendar_service.source = 'Google-Calendar_Python_Sample-1.0'
calendar_service.ProgrammaticLogin()

def FullTextQuery(calendar_service, text_query):
    print 'Full text query for events on Primary Calendar: \'%s\'' % ( text_query,)
    query = gdata.calendar.service.CalendarEventQuery('default', 'private', 'full', text_query)
    query.singleevents = 'true'
    query.orderby = 'starttime'
    query.sortorder = 'ascending'
    query.futureevents = 'true'
    query.ctz = 'UTC'
    feed = calendar_service.CalendarQuery(query)
    comparison_time_format = '%d-%m-%Y %H:%M'
    for i, an_event in enumerate(feed.entry):
        for a_when in an_event.when:
            try:
                event_time = time.strptime(a_when.start_time, '%Y-%m-%dT%H:%M:%S.000Z')
            except Exception, e:
                continue #all-day events
            
            current_time = time.gmtime()
            event_time_formatted = time.strftime(comparison_time_format, event_time)
            current_time_formatted = time.strftime(comparison_time_format, current_time)
            comparison = event_time_formatted == current_time_formatted

            print an_event.title.text, "Number:", i, "Event Time:", event_time_formatted, "Current Time:", current_time_formatted, "Comparison:", comparison
 
            if comparison:
                print
            #    songfile = random.choice(os.listdir("/home/pi/alarmclock/test_MP3s/")) #chooses the .mp3 file
            #    print "File Selected:", songfile
            #    command ="mpg321" + " " + "/home/pi/alarmclock/test_MP3s/" + "'"+songfile+"'"+ " -g 100" #plays the MP3 in it's entierty. As long as the song is longer than a minute then will only trigger once in the minute that start of the "wake" event
 
            #    print command
                #os.system(command) #runs the bash command
 
def callable_func():
    os.system("clear") #this is more for my benefit and is in no way necesarry
    print "------------start-----------"
    for t in config.terms:
        FullTextQuery(calendar_service, t)
    print "-------------end------------"
 
#scheduler = Scheduler(standalone=True)
#scheduler.add_interval_job(callable_func,seconds=5)
#scheduler.start() #runs the program indefinatly on an interval of 5 seconds

callable_func()
