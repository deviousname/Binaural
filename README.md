# Binaural Beats Chakra Meditation
This script generates a binaural beat playlist designed for meditation, based on specific frequencies associated with each of the seven chakras. Each beat is played for a specified duration, with a smooth transition to the next one.

# Requirements
Python 3
pydub library

# Installation
Install Python 3 if you haven't already.
Install the pydub library using pip:

    pip install pydub

# Usage
Copy the provided code into a Python file, e.g., binaural_beats.py.
Run the script using Python:

    python binaural_beats.py
    
The script will play a binaural beat playlist based on specified chakra frequencies. By default, the play time for each beat is 150 seconds (2.5 minutes) with a 15-second transition between each beat. You can customize the duration and transition time by modifying the play_time and transition_time parameters when creating the BinauralPlaylist instance:

    playlist = BinauralPlaylist(BinauralPlaylist.frequency_scales, play_time=150.0, transition_time=15.0, amplitude=0.5, lower_octave=0)

    
play_time and transition_time are specified in seconds. The amplitude parameter adjusts the volume of the binaural beats (range 0-1) and lower_octave determines how many octaves to lower the base frequencies.

# Customization
You can modify the base frequencies and binaural frequencies in the script to create a custom playlist. By default, the script uses the following chakra frequencies and binaural frequencies:

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
    
To change the base frequencies or binaural frequencies, update the bb and frequency_scales variables in the script accordingly.

# Disclaimer
Please use this script responsibly. Keep the frequencies within the safe range for human hearing (20 Hz - 20,000 Hz) and the amplitude at a comfortable level. The script includes safeguards to prevent the use of frequencies outside the safe range and amplitudes outside the valid range. Nonetheless, it is the user's responsibility to ensure they are using the script safely, considering their own preferences and health.

# License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute the code as needed.
