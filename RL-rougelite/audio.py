from __future__ import annotations

import soundfile
import tcod.sdl.audio

mixer = tcod.sdl.audio.BasicMixer(tcod.sdl.audio.open())  # Setup BasicMixer with the default audio output

def play_audio(file: str):
    """Plays the audio for the given consumable"""
    sound, sample_rate = soundfile.read(file)  # Load an audio sample using SoundFile.
    sound = mixer.device.convert(sound, sample_rate)  # Convert this sample to the format expected by the device.
    channel = mixer.play(sound)
    return None