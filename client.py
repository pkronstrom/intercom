from pymumble.pymumble_py3 import Mumble, constants
import alsaaudio

class MumbleClient:
    def __init__(self, host, user, channel):
        self.mumble = Mumble(host, user, debug=False)
        self.mumble.start()
        self.mumble.is_ready()

        self.mumble.set_receive_sound(True)
        self.mumble.users.myself.unmute()

        self.mumble.channels.find_by_name(channel).move_in()
        self.mumble.set_bandwidth(200000)

        self.mumble.callbacks.set_callback(constants.PYMUMBLE_CLBK_SOUNDRECEIVED, self.play_sound)

        # setup sound output
        self.device = alsaaudio.PCM(mode=alsaaudio.PCM_NONBLOCK, cardindex=0)
        self.device.setchannels(1)  # use only one channel of audio (aka mono)
        self.device.setrate(48000)  # how many samples per second
        self.device.setformat(alsaaudio.PCM_FORMAT_S16_LE)  # sample format
        self.device.setperiodsize(1920)

    def send_audio_chunk(self, audio_chunk):
        self.mumble.sound_output.add_sound(audio_chunk)


    def play_sound(self, info, sound_chunk):
        self.device.write(sound_chunk.pcm)
