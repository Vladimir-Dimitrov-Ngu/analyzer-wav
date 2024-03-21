from fire import Fire
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def generate_formant_like_noise(
    duration, sampling_rate, num_formants=3, formant_freqs=None, formant_bw=None
):
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    signal = np.zeros_like(t)
    if formant_freqs is None:
        formant_freqs = [500, 1500, 2500]
    if formant_bw is None:
        formant_bw = [80, 80, 80]

    for freq, bw in zip(formant_freqs, formant_bw):
        formant_noise = np.random.normal(0, 1, len(t))
        formant_noise = (
            np.convolve(formant_noise, [1] * int(bw * sampling_rate), mode="same")
            / sampling_rate
        )
        signal += np.sin(2 * np.pi * freq * t) * formant_noise

    return signal / np.max(np.abs(signal))


def generate_pink_noise(duration, sampling_rate):
    num_samples = int(duration * sampling_rate)
    pink_noise = np.zeros(num_samples)
    b = [0.049922035, -0.095993537, 0.050612699, -0.004408786]
    a = [1, -2.494956002, 2.017265875, -0.522189400]
    pink_noise = np.random.randn(num_samples)
    pink_noise = np.convolve(pink_noise, b)
    pink_noise = np.convolve(pink_noise, a)
    return pink_noise[:num_samples]


def plot_and_save_mel_spectrogram(
    audio_file_path: str,
    output_image_path: str,
    sample_rate: int = 22050,
    add_white_noise: bool = False,
    noise_level: int = 0.4,
    add_formant_noise: bool = False,
    num_formants=3,
    formant_freqs: int | None = None,
    formant_bw: int | None = None,
    add_pink_noise: bool = False,
):
    """
    Load an audio file, compute its Mel spectrogram, plot and save the Mel spectrogram.

    Parameters:
        audio_file_path (str): Path to the input audio file.
        output_image_path (str): Path to save the output Mel spectrogram image.
        sample_rate (int, optional): Sampling rate of the audio file. Default is 22050.
        add_white_noise (bool, optional): Whether to add white noise to the audio. Default is False.
        noise_level (float, optional): Level of white noise to add. Default is 0.05.
        add_formant_noise (bool, optional): Whether to add formant-like noise to the audio. Default is False.
        formant_freqs (list, optional): List of formant frequencies. Default is None (uses default frequencies).
        formant_bw (list, optional): List of formant bandwidths. Default is None (uses default bandwidths).
        add_pink_noise (bool, optional): Whether to add pink noise to the audio. Default is False.
    Returns:
        None: The function saves the Mel spectrogram image to the specified output path.
    """
    y, sr = librosa.load(audio_file_path, sr=sample_rate)
    if add_white_noise:
        noise = np.random.randn(len(y))
        noise = noise * noise_level
        y += noise
    if add_formant_noise:
        duration = len(y) / sr
        formant_noise = generate_formant_like_noise(
            duration, sr, num_formants, formant_freqs, formant_bw
        )
        y += formant_noise
    if add_pink_noise:
        pink_noise = generate_pink_noise(len(y) / sr, sr)
        y += pink_noise

    mel_spec = librosa.feature.melspectrogram(y=y, sr=sr)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)

    plt.figure(figsize=(10, 4))
    librosa.display.specshow(mel_spec_db, sr=sr, x_axis="time", y_axis="mel")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Mel-Spectrogram")
    plt.savefig(output_image_path, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    Fire(plot_and_save_mel_spectrogram)
