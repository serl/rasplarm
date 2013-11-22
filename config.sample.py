config = {
  "snooze_minutes": 10,

  #to enable/disable Calendars and Alarms, simply uncomment/comment their sections
  "Calendars": (
    {
      "type": "Google",
      "username": "...",
      "password": "...",
      "terms": ['wake'] # calendar entries containing these terms will be used
    },
    { "type": "Always" } # testing purposes
  ),
  "Alarms": (
    #{ "type": "Console" }, # testing purposes
    #{
    #  "type": "Command",
    #  I'll call "command 'event name'", so if not interested, end command with #
    #  "command": "mplayer some://internet.radio/listen.pls #",
    #  after timeout seconds I'll check if your command is still alive. if not, I'll try to use the next alarm
    #  default value is None = going straight to the next alarm
    #  "timeout": 5 # for example: in after 5sec mplayer is exited, maybe our internet radio is unreachable and we should play an mp3...
    #},
    {
      "type": "Mp3",
      "command": "mplayer -quiet", # an alternative: "mpg321 -g 100",
      "directory": "path/to/dir" # I will choose in the directory one random file to play
    }
  )
}
