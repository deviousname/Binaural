import time
from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play


class BinauralPlaylist:
    def __init__(self, frequency_pairs, play_time=600, transition_time=5, amplitude=0.5):
        self.frequency_pairs = frequency_pairs
        self.play_time = play_time
        self.transition_time = transition_time

        if amplitude < 0 or amplitude > 1:
            raise ValueError("Amplitude must be between 0 and 1.")
        self.amplitude = amplitude

    def _play_beat(self, left_freq, right_freq):
        # Check if frequencies are within the safe hearing range
        if not (20 <= left_freq <= 20000) or not (20 <= right_freq <= 20000):
            print("Error: One or both frequencies are outside the safe hearing range (20 Hz - 20,000 Hz).")
            return

        # Generate and play binaural beat
        left_sine = Sine(left_freq).to_audio_segment(duration=self.play_time * 1000)
        right_sine = Sine(right_freq).to_audio_segment(duration=self.play_time * 1000)
        binaural_beat = AudioSegment.from_mono_audiosegments(left_sine, right_sine)
        binaural_beat = binaural_beat - (20 - self.amplitude * 20)
        play(binaural_beat)

    def play(self):
        for i, (left_freq, right_freq) in enumerate(self.frequency_pairs):
            print(f"Playing binaural beat: left frequency {left_freq} Hz, right frequency {right_freq} Hz")
            self._play_beat(left_freq, right_freq)

            if i < len(self.frequency_pairs) - 1:
                if self.transition_time > 0:
                    print("Transitioning...")
                    time.sleep(self.transition_time)
            else:
                print("Finished")

    @staticmethod
    def lower_octave(freq, num_octaves=1):
        return freq / (2 ** num_octaves)


# Define frequency pairs (base frequency, binaural beat frequency)
schumann_freq = 7.83

frequency_pairs = [
    (BinauralPlaylist.lower_octave(396 - schumann_freq / 2, 2), BinauralPlaylist.lower_octave(396 + schumann_freq / 2, 2)),
    (BinauralPlaylist.lower_octave(417 - schumann_freq / 2, 2), BinauralPlaylist.lower_octave(417 + schumann_freq / 2, 2)),
    (BinauralPlaylist.lower_octave(528 - schumann_freq / 2, 2), BinauralPlaylist.lower_octave(528 + schumann_freq / 2, 2)),
    (BinauralPlaylist.lower_octave(639 - schumann_freq / 2, 2), BinauralPlaylist.lower_octave(639 + schumann_freq / 2, 2)),
    (BinauralPlaylist.lower_octave(741 - schumann_freq / 2, 2), BinauralPlaylist.lower_octave(741 + schumann_freq / 2, 2)),
    (BinauralPlaylist.lower_octave(852 - schumann_freq / 2, 2), BinauralPlaylist.lower_octave(852 + schumann_freq / 2, 2)),
    (BinauralPlaylist.lower_octave(963 - schumann_freq / 2, 2), BinauralPlaylist.lower_octave(963 + schumann_freq / 2, 2)),
]

# Create a playlist with a 10-minute duration and a 5-second transition between each beat
playlist = BinauralPlaylist(frequency_pairs, play_time=600, transition_time=5)

# Play the playlist
playlist.play()
