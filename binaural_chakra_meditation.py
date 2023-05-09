import threading
import time
from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play

class BinauralPlaylist:
    # Initialize the BinauralPlaylist class with frequency pairs, play time, transition time, and amplitude
    def __init__(self, frequency_pairs, play_time=600, transition_time=5, amplitude=0.3):
        self.frequency_pairs = frequency_pairs  # List of frequency pairs for binaural beats
        self.play_time = play_time  # Duration of each binaural beat in seconds
        self.transition_time = transition_time  # Time for fade in and fade out in milliseconds

        # Validate amplitude value to be between 0 and 1
        if amplitude < 0 or amplitude > 1:
            raise ValueError("Amplitude must be between 0 and 1.")
        self.amplitude = amplitude  # Amplitude of the binaural beats

    # Play a single binaural beat with the given left and right frequencies
    def _play_beat(self, left_freq, right_freq):
        # Check if the frequencies are within the safe hearing range
        if not (20 <= left_freq <= 20000) or not (20 <= right_freq <= 20000):
            print("Error: One or both frequencies are outside the safe hearing range (20 Hz - 20,000 Hz).")
            return

        # Generate sine waves for left and right frequencies
        left_sine = Sine(left_freq).to_audio_segment(duration=self.play_time * 1000)
        right_sine = Sine(right_freq).to_audio_segment(duration=self.play_time * 1000)

        # Apply a short fade in and fade out to the sine wave segments
        left_sine = left_sine.fade_in(self.transition_time).fade_out(self.transition_time)
        right_sine = right_sine.fade_in(self.transition_time).fade_out(self.transition_time)

        # Combine the left and right sine waves into a binaural beat
        binaural_beat = AudioSegment.from_mono_audiosegments(left_sine, right_sine)

        # Adjust the volume of the binaural beat based on the amplitude
        binaural_beat = binaural_beat - (20 - self.amplitude * 20)

        # Play the binaural beat
        play(binaural_beat)

    # Start playing the next binaural beat in the playlist
    def _start_next_beat(self, i):
        if i < len(self.frequency_pairs):
            left_freq, right_freq = self.frequency_pairs[i]
            print(f"Playing binaural beat: left frequency {left_freq} Hz, right frequency {right_freq} Hz")
            self._play_beat(left_freq, right_freq)

    # Play the entire binaural beats playlist
    def play(self):
        for i, (left_freq, right_freq) in enumerate(self.frequency_pairs):
            print(f"Playing binaural beat: left frequency {left_freq} Hz, right frequency {right_freq} Hz")
            beat_thread = threading.Thread(target=self._play_beat, args=(left_freq, right_freq))
            beat_thread.start()
            time.sleep(self.play_time)
        beat_thread.join()
        print("Finished")

    # Lower the frequency by a specified number of octaves
    @staticmethod
    def lower_octave(freq, num_octaves=1):
        return freq / (2 ** num_octaves)

# Define frequency pairs (base frequency, binaural beat frequency)
schumann_freq = 7.83

# Define base frequencies
solfeggio_frequencies = [396, 417, 528, 639, 741, 852, 963]
chakra_frequencies = [194, 210, 261.63, 329.63, 392, 440, 480]

# Choose the desired scale: 'solfeggio' or 'chakra'
scale = 'chakra'

# Choose whether to lower the chosen frequencies and how many octaves to lower
lower_octave = True
lower_octaves_by = 1

# Select the chosen frequencies based on the chosen scale
chosen_frequencies = solfeggio_frequencies if scale == 'solfeggio' else chakra_frequencies

# Lower the chosen frequencies if the lower_octave option is set
if lower_octave:
    chosen_frequencies = [BinauralPlaylist.lower_octave(f, lower_octaves_by) for f in chosen_frequencies]

# Calculate the frequency pairs based on the chosen frequencies and the Schumann frequency
frequency_pairs = [(f - schumann_freq / 2, f + schumann_freq / 2) for f in chosen_frequencies]

# Create a playlist with a 5-minute duration, a 5-second transition between each beat and an amplitude of 0.3
playlist = BinauralPlaylist(frequency_pairs, play_time=300, transition_time=5, amplitude=0.3)

playlist.play()
