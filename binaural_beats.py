import threading
import time
import math
from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play
import logging

logging.basicConfig(level=logging.INFO)

class BinauralPlaylist:
    """
    A class used to represent a BinauralPlaylist.

    ...

    Attributes
    ----------
    frequencies : dict
        a dictionary of frequency pairs for binaural beats.
    play_time : int
        the duration of each binaural beat in seconds (default 600).
    transition_time : int
        the time for fade in and fade out in seconds (default 5).
    amplitude : float
        the amplitude of the binaural beats (default 0.3).
    lower_octave : int
        the number of octaves to lower (default 0).

    Methods
    -------
    play(scale)
        Plays a scale of binaural beats from the frequencies dictionary.
    _play_beat(central_freq, binaural_freq)
        Internal method that generates and plays a binaural beat for a given pair of frequencies.
    _lower_octave(freq)
        Internal method that lowers the input frequency by a certain number of octaves.
    """
    
    bb = { # binaural wave (difference between two base waves)
        'kundalini_awakening': 55,
        'memory_enhancer': 40,
        'zen_focus': 14,
        'love_meditation': 12.5,
        'astral_projection': 12,
        'tantric_stimulation': 9,
        'anxiety_release': 8.6,
        'positive_thinking': 8,
        'schumann': 7.83,
        'spiritual_awakening': 7.5,
        'lucid_dreaming': 7,
        'chill_pill': 6,
        'deep_meditation': 5,
        'tinnitus_relief': 4,
        'blissful_sleep': 3.9,
        'power_nap': 3.4,
    }

    frequency_scales = { # base wave, which is centered around the binaural wave and split into two.
        'chakra': [
            (480, bb['schumann']), # Crown Chakra
            (440, bb['spiritual_awakening']), # Third Eye Chakra
            (392, bb['lucid_dreaming']), # Throat Chakra
            (329.63, bb['chill_pill']), # Heart Chakra
            (261.63, bb['deep_meditation']), # Solar Plexus Chakra
            (210, bb['tinnitus_relief']),  # Sacral Chakra
            (194, bb['blissful_sleep']), # Root Chakra
        ],
    }

    def __init__(self, frequencies, play_time=600.0, transition_time=5.0, amplitude=0.3, lower_octave=0):
        if play_time < 0 or transition_time < 0 or lower_octave < 0:
            raise ValueError("Play_time, transition_time and lower_octave must be non-negative.")
        if amplitude < 0 or amplitude > 1:
            raise ValueError("Amplitude must be between 0 and 1.")
        self.frequencies = frequencies
        self.play_time = play_time
        self.transition_time = transition_time
        self.amplitude = amplitude
        self.lower_octave = lower_octave

    def _play_beat(self, central_freq, binaural_freq):
        central_freq = self._lower_octave(central_freq)
        if not (20 <= central_freq - binaural_freq/2 <= 20000) or \
           not (20 <= central_freq + binaural_freq/2 <= 20000):
            logging.error(
                f"One or both frequencies are outside the safe hearing range "
                f"(20 Hz - 20,000 Hz). Central Frequency: {central_freq}, "
                f"Binaural Frequency: {binaural_freq}"
            )
            return  # Skip this frequency pair if it's out of range
        left_freq = central_freq - binaural_freq/2
        right_freq = central_freq + binaural_freq/2
        left_sine = Sine(left_freq).to_audio_segment(duration=int(self.play_time * 1000))
        right_sine = Sine(right_freq).to_audio_segment(duration=int(self.play_time * 1000))
        left_sine = left_sine.fade_in(int(self.transition_time * 1000)).fade_out(int(self.transition_time * 1000))
        right_sine = right_sine.fade_in(int(self.transition_time * 1000)).fade_out(int(self.transition_time * 1000))
        binaural_beat = AudioSegment.from_mono_audiosegments(left_sine, right_sine)
        binaural_beat = binaural_beat - (20 - 20 * math.log10(self.amplitude))  # Scale amplitude to dB
        play(binaural_beat)

    def play(self, scale):
        if scale not in self.frequencies:
            logging.error(f"Scale '{scale}' not found in frequency dictionary.")
            return

        threads = []
        for central_freq, binaural_freq in self.frequencies[scale]:
            logging.info(
                f"Playing binaural beat: central frequency {central_freq} Hz, "
                f"binaural frequency {binaural_freq} Hz"
            )
            beat_thread = threading.Thread(target=self._play_beat, args=(central_freq, binaural_freq))
            beat_thread.start()
            threads.append(beat_thread)
            sleep_time = self.play_time - self.transition_time
            if sleep_time > 0:
                time.sleep(sleep_time)  # Only sleep if sleep_time is positive

        for thread in threads:
            thread.join()

        logging.info("Finished")

    def _lower_octave(self, freq):
        return freq / (2 ** self.lower_octave)


if __name__ == "__main__":
    playlist = BinauralPlaylist(BinauralPlaylist.frequency_scales, play_time=150.0, transition_time=15.0, amplitude=0.5, lower_octave=0)
    playlist.play('chakra')

# End of the line, partner.
