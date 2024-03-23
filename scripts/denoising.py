import noisereduce as nr
import numpy as np
from scipy.io import wavfile
import os
from fire import Fire


def denoising(input_file: str, output_file: str) -> None:
    """
    Removes noise from an audio file using the noisereduce library.

    The function reads the audio file specified in input_file and applies
    a noise reduction algorithm from the noisereduce library. The result
    is saved to a file named 'denoised_audio.wav' in the current directory.

    Args:
    input_file (str): Path to the input audio file in WAV format.
    output_file (str): Path to the output audio file in WAV format.

    Notes:
    - The input audio file must be in WAV format.
    - The output file 'denoised_audio.wav' will be overwritten if it already exists.
    - The function uses the noisereduce, numpy, and scipy.io.wavfile libraries.

    Example usage:
    denoising('/path/to/audio/file.wav')
    """
    rate, data = wavfile.read(input_file)
    denoised_audio = nr.reduce_noise(y=data, sr=rate, prop_decrease=1.0)
    wavfile.write(output_file, rate, denoised_audio.astype(np.int16))


def create_folder_with_denoising(
    input_folder_with_noise: str, output_folder: str
) -> None:
    """
    Creates a new folder with denoised audio files.

    Args:
        input_folder_with_noise (str): Path to the folder containing the noisy audio files.
        output_folder (str): Path to the folder where the denoised audio files will be saved.

    Returns:
        None

    Notes:
        - Only WAV files in the input_folder_with_noise will be processed.
        - The denoised files will be saved in the output_folder with the prefix "Denosing_" added to the filename.
        - The denoising function must be defined and available in the current scope.
    """
    files = [
        file for file in os.listdir(input_folder_with_noise) if file.endswith(".wav")
    ]

    for file in files:
        path_to_file = os.path.join(input_folder_with_noise, file)
        path_to_output = os.path.join(output_folder, "Denosing_" + file)
        denoising(path_to_file, path_to_output)


if __name__ == "__main__":
    Fire(create_folder_with_denoising)
