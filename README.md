# Raspberry Pi Intercom

Raspberry Pi Intercom brings back the old-fashioned intercom radio!
Just press the big, friendly button to open a connection to other intercoms
connected to the intercom network! Fancy!

# Required Hardware

You need the following items to get started with this project.
Ideally, you should build at least two intercom units!

- A RaspberryPi (The original intercom uses a RPi3)
- (A WS2812 RGB LED ring (12 leds) for amazing light effects)
- A '3D SOUND' USB sound card
- An external mic with a 3.5 mm plug
- An external speaker with a 3.5 mm plug
- A big, friendly push button

# Software Installation and configuration
The installation procedure assumes a Raspbian Wheezy or similar OS.
Everything is done via command line.

## Install dependencies
- install dependencies `sudo apt-get install git python3-dev python3-pip libsound2-dev libopus-dev`

## Install a mumble server

Documentation can be found [here](https://pimylifeup.com/raspberry-pi-mumble-server/).

- `sudo apt-get install mumble-server`
- `sudo dpkg-reconfigure mumble-server`
- Modify settings `sudo vi /etc/mumble-server.ini`
- Restart the server `sudo /etc/init.d/mumble-server restart`

Mumble server should now start automatically upon restart

## Python and friends

- Install virtualenv in your project folder `sudo pip3 install virtualenv`
- Create a new virtualenv `virtualenv -p /usr/bin/python3 venv`
- Activate it `source venv/bin/activate`

- clone this git repo `git clone https://github.com/pkronstrom/intercom`
- update submodules `git submodule update --recursive`
- `pip install -r requirements.txt`
- `python pymumble/setup.py install`

# Hardware Installation and configuration
- Plug the USB sound card in and attach your mic and speaker to it.
- Add a push button between 3V3 and GPIO4 pins.

# Getting it running!
RPi.GPIO requires admin rights, so we need to run the intercom server as root.
Make a copy of the settings file `cp intercom.ini.example intercom.ini` and modify it before running the server.
The server can be started by calling `sudo python3 intercom.py`.

# Links
- [pymumble](https://github.com/azlux/pymumble)
- [pyalsaaudio](http://larsimmisch.github.io/pyalsaaudio)
- [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)
