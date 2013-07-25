config = {
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
    "Mp3Alarm": {
      "command": "mpg321",
      "arguments": "-g 100",
      "directory": "path/to/dir" # I will choose one random file in the directory
    }
  }
}
