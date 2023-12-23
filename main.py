import sounddevice as sd
import numpy as np

# 1: Play a Sine Wave
def play_sine_wave(frequency=440, duration=3, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(sine_wave, samplerate=sample_rate)
    sd.wait()

# 2: Record Audio
def record_audio(duration=5, sample_rate=44100):
    print("Recording... Press Ctrl+C to stop.")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()
    print("Recording complete.")

# 3: Play White Noise
def play_white_noise(duration=3, sample_rate=44100):
    white_noise = np.random.normal(0, 0.5, int(sample_rate * duration))
    sd.play(white_noise, samplerate=sample_rate)
    sd.wait()

# 4: Play a Chirp Signal
def play_chirp_signal(start_freq=100, end_freq=1000, duration=3, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    chirp_signal = 0.5 * np.sin(2 * np.pi * np.linspace(start_freq, end_freq, len(t)) * t)
    sd.play(chirp_signal, samplerate=sample_rate)
    sd.wait()

# 5: Play a Custom Sound
def play_custom_sound(sound_data, sample_rate=44100):
    sd.play(sound_data, samplerate=sample_rate)
    sd.wait()

if __name__ == "__main__":
    # Example usage
    play_sine_wave()
    record_audio()
    play_white_noise()
    play_chirp_signal()
    # Replace `custom_sound_data` with your own sound data (NumPy array)
    custom_sound_data = np.random.rand(44100)
    play_custom_sound(custom_sound_data)
