from pymumble.pymumble_py3 import Mumble

class MumbleClient:
    def __init__(self, host, user, channel):
        self.mumble = Mumble(host, user, debug=False)
        self.mumble.start()
        self.mumble.is_ready()

        self.mumble.set_receive_sound(True)
        self.mumble.users.myself.unmute()

        self.mumble.channels.find_by_name(channel).move_in()
        # mumble.set_bandwidth(200000)

    def handle_loop(self):
        # do audio stuff
        sd = "sd"
