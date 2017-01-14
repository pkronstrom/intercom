# intercom
A Raspberry Pi intercom - Gofore hackathon project

## Install and configure server

https://pimylifeup.com/raspberry-pi-mumble-server/

`sudo apt-get install mumble-server`

`sudo dpkg-reconfigure mumble-server`

Modify `/etc/mumble-server.ini`

Restart `sudo /etc/init.d/mumble-server restart`

## Python installation

- `sudo apt-get install python3-dev`
- `sudo apt-get install python3-pip`
- `sudo pip3 install virtualenv`
- `virtualenv -p /usr/bin/python3 venv`
- `source venv/bin/activate`

- `(git submodule update --recursive)`
- `cd pymumble`
- `python setup.py install`
- `pip install -r requirements.txt`

### Install Opus Library
- sudo apt-get install libopus-dev