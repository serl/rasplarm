config = {
  "snooze_minutes": 10,

  #to enable/disable Calendars and Alarms, simply uncomment/comment their sections
  "Calendars": {
    "GoogleCalendar": {
      "username": "...",
      "password": "...",
      "terms": ['wake'] # calendar entries containing these terms will be used
    },
    #"AlwaysCalendar": {} # testing purposes
  },
  "Alarms": {
    #"ConsoleAlarm": {}, # testing purposes
    #"CommandAlarm": {
    #  i'll call "command 'event name'", so if not interested, end command with #
    #  "command": "mplayer some://internet.radio/listen.pls #"
    #},
    "Mp3Alarm": {
      "command": "mplayer -quiet", # an alternative: "mpg321 -g 100",
      "directory": "path/to/dir" # I will choose in the directory one random file to play
    }
  }
}
