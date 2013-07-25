Rasplarm
========

Raspberry Pi customizable alarm clock

Inspiration from <http://www.esologic.com/?p=634>, thanks Devon!

WARNING: I'm not a pythonist, so please forgive me... thanks...

Installation
============

First of all, you've to install the dependencies. That's how I made it (not so elegant):

    sudo apt-get install python-setuptools
    sudo easy_install pip
    sudo pip install -r requirements.txt

Next, to configure the thing, copy `config.sample.py` to `config.py` and edit it, you should find there some configuration hints.

Usage
=====

    python start.py

Then, there are some interesting signals (assuming $pid is the PID):

    kill -SIGUSR1 $pid #snooze the alarm, it'll restart after config['snooze_minutes'] minutes
    kill -SIGUSR2 $pid #stop completely the alarm

Know bugs
=========

* Actually, I need something really really easy to send SIGUSR1. I'll think something when I need it: tomorrow morning.
* Not so good english.
