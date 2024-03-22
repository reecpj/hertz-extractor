
import librosa
import numpy as np

def process_audio(video):
    audio_array = list(video.audio.iter_frames())

    # Convert the list of samples to a NumPy array
    sound_array = np.array(audio_array)
    audio_data = sound_array[:, 0]  # Extracting only one channel if it's stereo

    # Get the sampling rate of the audio
    sr = sound_array.shape[0] / video.duration

    # Compute the Short-Time Fourier Transform (STFT) to get the frequency content
    D = np.abs(librosa.stft(audio_data))

    # Convert the frequency content to a logarithmic scale (in decibels)
    DB = librosa.amplitude_to_db(D, ref=np.max)

    # Define the frequency range
    freqs = librosa.core.fft_frequencies(sr=sr)

    return sound_array, audio_data, sr, D, DB, freqs

def extract_frequency_magnitude(DB, freqs, sr, target_freq):
    target_freq_index = np.argmin(np.abs(freqs - target_freq))
    magnitude_at_target = DB[target_freq_index]
    print(f"mean magnitude at {target_freq}hz: {np.mean(magnitude_at_target):.2f}")

    hop_length = 512
    time_bin_length = sr / hop_length
    num_time_bins_per_10s = int(10 * time_bin_length)

    average_magnitudes_per_10s = [np.mean(DB[target_freq_index, i:i + num_time_bins_per_10s]) for i in range(0, DB.shape[1], num_time_bins_per_10s)]
    average_magnitudes_formatted = [f"{x:.2f}" for x in average_magnitudes_per_10s]
    print(f"mean magnitude at {target_freq}hz for every 10s chunk: {average_magnitudes_formatted}")