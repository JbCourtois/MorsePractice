import pygame
import numpy as np

import time


freq = 550  # Hz
dotLength = 40  # milliseconds


pygame.mixer.init(frequency=44100)


def generate_sound(frequency, duration=dotLength / 1000):
    # Generate the sound wave
    sample_rate = 44100  # Samples per second
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    # Convert to 16-bit data
    sound_wave = np.int16(wave * 32767)

    # Create a sound object
    return pygame.mixer.Sound(sound_wave)


sound = generate_sound(400)
background = generate_sound(20, duration=1)


def beep(dur):
    """
    makes noise for specific duration.
    :param dur: duration of beep in number of cycles
    """
    channel = sound.play(loops=dur - 1)
    while channel.get_busy():
        continue
    pause(2)


def pause(dur):
    """
    pauses audio
    :param dur: duration of pause in number of cycles
    """
    time.sleep(dur * dotLength / 1000)
