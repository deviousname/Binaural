# Binaural Beats Chakra Meditation
This script generates a binaural beat playlist for meditation based on chakra frequencies. It plays each beat for a specified duration, and smoothly transitions between the beats using overlap.

# Requirements
Python 3
pydub library

# Installation
Install Python 3 if you haven't already.
Install the pydub library using pip:
    pip install pydub

# Usage
Copy the provided code into a Python file, e.g., binaural_beat_chakra_meditation.py.
Run the script using Python:
    python binaural_beat_chakra_meditation.py
The script will play a binaural beat playlist based on chakra frequencies. The default play time for each beat is 10 minutes with a 5-second transition between each beat. You can customize the duration and transition time by modifying the play_time and transition_time parameters when creating the BinauralPlaylist instance:
    playlist = BinauralPlaylist(frequency_pairs, play_time=600, transition_time=5)
The play_time is in seconds, and the transition_time is the time it takes to smoothly transition between two beats, also in seconds.

# Customization
You can modify the base frequencies and Schumann frequency in the script to create a custom playlist. By default, the script uses the following chakra frequencies and Schumann frequency:
    Base frequencies: 396 Hz, 417 Hz, 528 Hz, 639 Hz, 741 Hz, 852 Hz, 963 Hz
    Schumann frequency: 7.83 Hz
These frequencies are lowered by two octaves and combined with the Schumann frequency to create the final binaural beat frequencies.

To change the base frequencies or Schumann frequency, update the base_frequencies and schumann_freq variables in the script accordingly.

# Disclaimer
Please make sure to use this script responsibly, keeping the frequencies within the safe range for human hearing (20 Hz - 20,000 Hz) and the amplitude at a comfortable level. The script includes safeguards to prevent the use of frequencies outside the safe range and amplitudes outside the valid range. However, it is the user's responsibility to ensure they are using the script safely and in accordance with their own preferences and health considerations.

# License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute the code as needed.
