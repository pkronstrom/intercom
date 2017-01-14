from pymumble.pymumble_py3 import Mumble
import time

HOST = '127.0.0.1'
USER = 'puhelias'
CHANNEL = 'Mumble Server'

class MumbleClient():
	def __init__(self):
		self.mumble = Mumble(HOST, USER, debug=False)
		self.mumble.start()
		self.mumble.is_ready()

		self.mumble.set_receive_sound(True)
		self.mumble.users.myself.unmute()

		self.mumble.channels.find_by_name(CHANNEL).move_in()
		# mumble.set_bandwidth(200000)

		self.exit = False
		self.loop()

	def loop(self):
		while not self.exit:
			# do audio stuff
			time.sleep(0.01)

if __name__ == '__main__':
	MumbleClient()