import configparser
import time
import RPi.GPIO as GPIO

from client import MumbleClient

class InterCom:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('intercom.ini')
        self.mumble_client = MumbleClient(config['mumbleclient'])
        self.exit = False

        if config['general']['gpiotype'] == 'BCM':
            GPIO.setmode(GPIO.BCM)

        self.button = int(config['general']['button'])
        GPIO.setup(self.button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


    def run(self):
        while not self.exit:
            if GPIO.input(self.button):
                self.mumble_client.send_input_audio()
            else:
                self.mumble_client.clear_input()

if __name__ == '__main__':
    try:
        InterCom().run()
    except Exception as e:
        raise e
    finally:
        GPIO.cleanup()
