config = {
  "Calendars": {
    "GoogleCalendar": {
      "username": "...",
      "password": "...",
      "terms": ['wake']
    },
    "AlwaysCalendar": {}
  },
  "Alarms": {
    "ConsoleAlarm": {},
    "Mp3Alarm": {
      "command": "mpg321",
      "arguments": "-g 100",
      "directory": "path/to/dir", #this line has precedence
      "file": "path/to/file"
    }
  }
}
