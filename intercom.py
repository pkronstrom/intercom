import configparser
import time

from client import MumbleClient

class InterCom:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('intercom.ini')
        self.mumble_client = MumbleClient(config['mumbleclient'])
        self.exit = False

    def run(self):
        while not self.exit:
            self.mumble_client.send_input_audio()
            time.sleep(0.01)

if __name__ == '__main__':
    InterCom().run()
