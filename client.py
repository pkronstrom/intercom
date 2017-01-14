from pymumble.pymumble_py3 import Mumble, constants
import alsaaudio

class MumbleClient:
    def __init__(self, config):
        debug = int(config['debug']) == 1
        self.mumble = Mumble(config['host'], config['user'], debug=debug)
        self.mumble.start()
        self.mumble.is_ready()

        self.mumble.set_receive_sound(True)
        self.mumble.users.myself.unmute()

        self.mumble.channels.find_by_name(config['channel']).move_in()
        self.mumble.set_bandwidth(int(config['bandwith']))

        self.mumble.callbacks.set_callback(
            constants.PYMUMBLE_CLBK_SOUNDRECEIVED, self.play_sound)

        self.output_device = alsaaudio.PCM(
            alsaaudio.PCM_PLAYBACK, alsaaudio.PCM_NONBLOCK, config['output'])
        self.output_device.setchannels(int(config['channels']))
        self.output_device.setrate(int(config['bitrate']))
        self.output_device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        self.output_device.setperiodsize(int(config['periodsize']))

        self.input_device = alsaaudio.PCM(
            alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, config['input'])

        self.input_device.setchannels(int(config['channels']))
        self.input_device.setrate(int(config['bitrate']))
        self.input_device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        self.input_device.setperiodsize(int(config['periodsize']))

    def send_audio_chunk(self, audio_chunk):
        self.mumble.sound_output.add_sound(audio_chunk)

    def play_sound(self, info, sound_chunk):
        self.output_device.write(sound_chunk.pcm)

    def clear_input(self):
        self.input_device.read()

    def send_input_audio(self):
        length, data = self.input_device.read()

        if length:
            self.send_audio_chunk(data)
