import threading
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
        if not (20 <= left_freq <= 20000) or not (20 <= right_freq <= 20000):
            print("Error: One or both frequencies are outside the safe hearing range (20 Hz - 20,000 Hz).")
            return
        
        left_sine = Sine(left_freq).to_audio_segment(duration=self.play_time * 1000)
        right_sine = Sine(right_freq).to_audio_segment(duration=self.play_time * 1000)

        # Apply a short fade in and fade out to the sine wave segments
        left_sine = left_sine.fade_in(self.transition_time).fade_out(self.transition_time)
        right_sine = right_sine.fade_in(self.transition_time).fade_out(self.transition_time)

        binaural_beat = AudioSegment.from_mono_audiosegments(left_sine, right_sine)
        binaural_beat = binaural_beat - (20 - self.amplitude * 20)
        play(binaural_beat)

    def _start_next_beat(self, i):
        if i < len(self.frequency_pairs):
            left_freq, right_freq = self.frequency_pairs[i]
            print(f"Playing binaural beat: left frequency {left_freq} Hz, right frequency {right_freq} Hz")
            self._play_beat(left_freq, right_freq)

    def play(self):
        for i, (left_freq, right_freq) in enumerate(self.frequency_pairs):
            print(f"Playing binaural beat: left frequency {left_freq} Hz, right frequency {right_freq} Hz")
            beat_thread = threading.Thread(target=self._play_beat, args=(left_freq, right_freq))
            beat_thread.start()
            time.sleep(self.play_time)
        beat_thread.join()
        print("Finished")

    @staticmethod
    def lower_octave(freq, num_octaves=1):
        return freq / (2 ** num_octaves)

# Define frequency pairs (base frequency, binaural beat frequency)
schumann_freq = 7.83

# Define base frequencies
base_frequencies = [396, 417, 528, 639, 741, 852, 963]

# Lower the base frequencies and keep the Schumann frequency intact
lowered_frequencies = [BinauralPlaylist.lower_octave(f, 2) for f in base_frequencies]

# Calculate the frequency pairs based on the lowered base frequencies and the Schumann frequency
frequency_pairs = [(f - schumann_freq / 2, f + schumann_freq / 2) for f in lowered_frequencies]

# Create a playlist with a 20-second duration and a 10-second transition between each beat
playlist = BinauralPlaylist(frequency_pairs, play_time=20, transition_time=10)

playlist.play()
