from pymumble.pymumble_py3 import Mumble, constants
import alsaaudio

class MumbleClient:
    def __init__(self, config):
        self.mumble = Mumble(config['host'], config['user'], debug=False)
        self.mumble.start()
        self.mumble.is_ready()

        self.mumble.set_receive_sound(True)
        self.mumble.users.myself.unmute()

        self.mumble.channels.find_by_name(config['channel']).move_in()
        self.mumble.set_bandwidth(200000)

        self.mumble.callbacks.set_callback(
            constants.PYMUMBLE_CLBK_SOUNDRECEIVED, self.play_sound)

        self.output_device = alsaaudio.PCM(
            alsaaudio.PCM_PLAYBACK, alsaaudio.PCM_NONBLOCK, config['output'])
        self.output_device.setchannels(1)
        self.output_device.setrate(48000)
        self.output_device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        self.output_device.setperiodsize(1920)

        self.input_device = alsaaudio.PCM(
            alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, config['input'])

        self.input_device.setchannels(1)
        self.input_device.setrate(48000)
        self.input_device.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        self.input_device.setperiodsize(1920)

    def send_audio_chunk(self, audio_chunk):
        self.mumble.sound_output.add_sound(audio_chunk)

    def play_sound(self, info, sound_chunk):
        self.device.write(sound_chunk.pcm)

    def send_input_audio(self):
        length, data = self.input_device.read()

        if length:
            self.send_audio_chunk(data)
