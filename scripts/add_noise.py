import numpy as np
import librosa
import soundfile as sf
import os
from tqdm import tqdm
from fire import Fire
from generate_noise import generate_pink_noise, generate_formant_like_noise


def add_noise(
    wav_file_path: str,
    output_file_path: str,
    white_noise_level: int = 0.3,
    sample_rate: int = 22050,
    add_white_noise: bool = True,
    add_formant_noise: bool = False,
    num_formants: int = 3,
    formant_freqs: int | None = None,
    formant_bw: int | None = None,
    add_pink_noise: bool = False,
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
    if add_white_noise:
        noise = np.random.randn(len(y))
        noise = noise * white_noise_level
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

    sf.write(output_file_path, y, sr)


def create_folder_with_noise(
    input_original_folder: str,
    output_folder_path: str,
    add_white_noise: bool = False,
    add_pink_noise: bool = False,
    white_noise_level: int = 0.3,
):
    """
    Creates a new folder with audio files that have added noise (white or pink).

    Args:
        input_original_folder (str): Path to the folder containing the original audio files.
        output_folder_path (str): Path to the folder where the modified audio files will be saved.
        add_white_noise (bool, optional): Whether to add white noise to the audio files. Defaults to False.
        add_pink_noise (bool, optional): Whether to add pink noise to the audio files. Defaults to False.
        white_noise_level (int, optional): The level of white noise to be added, between 0 and 1. Defaults to 0.3.

    Returns:
        None

    Notes:
        - Only WAV files in the input_original_folder will be processed.
        - The output files will be saved in the output_folder_path with the prefix "Noise_" added to the filename.
        - Either add_white_noise or add_pink_noise (but not both) must be set to True.
        - The add_noise function must be defined and available in the current scope.
        - A progress bar will be displayed during the process using tqdm.
    """
    files = [
        file for file in os.listdir(input_original_folder) if file.endswith(".wav")
    ]

    if add_white_noise:
        title = "Create folder with white noise"
    elif add_pink_noise:
        title = "Create folder with pink noise"
    else:
        title = "Create folder without noise"

    for file in tqdm(files, desc=title):
        path_to_file = os.path.join(input_original_folder, file)
        output_file_path = os.path.join(output_folder_path, "Noise_" + file)
        add_noise(
            path_to_file,
            output_file_path,
            add_white_noise=add_white_noise,
            add_pink_noise=add_pink_noise,
            white_noise_level=white_noise_level,
        )

    print("All done!")


if __name__ == "__main__":
    Fire(create_folder_with_noise)
