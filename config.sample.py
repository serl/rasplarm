config = {
  "snooze_minutes": 10,
  "Calendars": {
    "GoogleCalendar": {
      "username": "...",
      "password": "...",
      "terms": ['wake']
    },
    #"AlwaysCalendar": {} testing purposes
  },
  "Alarms": {
    #"ConsoleAlarm": {}, testing purposes
    "CommandAlarm": {
      "command": "echo 'an alarm' #" # i'll call command 'event name', so if not interested, end command with #
    },
    "Mp3Alarm": {
      "command": "mpg321 -g 100",
      "directory": "path/to/dir" # I will choose one random file in the directory
    }
  }
}
