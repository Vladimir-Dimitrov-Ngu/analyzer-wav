import numpy as np
import librosa
import soundfile as sf
from fire import Fire


def add_white_noise(
    wav_file_path: str,
    output_file_path: str,
    noise_level: int = 0.4,
    sample_rate: int = 22050,
):
    """
    Adds white noise to an audio file and saves the result.

    Parameters:
        wav_file_path (str): The path to the input audio file (WAV format).
        output_file_path (str): The path to save the audio file with added noise.
        noise_level (float, optional): The level of white noise to add.
            This parameter controls the amplitude of the noise.
            Default is 0.4.
        sample_rate (int): The sample rate of the audio files. Default is 22050.

    Returns:
        None
    """
    y, sr = librosa.load(wav_file_path, sr=sample_rate)
    noise = np.random.randn(len(y))
    noise = noise * noise_level
    y_with_noise = y + noise
    sf.write(output_file_path, y_with_noise, sr)


if __name__ == "__main__":
    Fire(add_white_noise)
