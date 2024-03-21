import os
from fire import Fire
from tqdm import tqdm
from mel_spectorgram import plot_and_save_mel_spectrogram


def convert_wavs_to_mels(
    audio_folder_path: str,
    save_images_folder: str,
    sample_rate: int = 22050,
    add_white_noise: bool = False,
    noise_level: int = 0.4,
    add_formant_noise: bool = False,
    num_formants=3,
    formant_freqs: int | None = None,
    formant_bw: int | None = None,
    add_pink_noise: bool = False,
) -> None:
    """
    Converts all WAV files in the specified audio folder to mel-spectrogram images
    and saves them in the specified folder.

    Parameters:
        audio_folder_path (str): The path to the folder containing WAV files.
        save_images_folder (str): The path to the folder where mel-spectrogram images will be saved.
        sample_rate (int, optional): The sample rate of the audio files. Default is 22050.
        add_white_noise (bool, optional): Whether to add white noise to the audio. Default is False.
        noise_level (float, optional): Level of white noise to add. Default is 0.05.
        add_formant_noise (bool, optional): Whether to add formant-like noise to the audio. Default is False.
        formant_freqs (list, optional): List of formant frequencies. Default is None (uses default frequencies).
        formant_bw (list, optional): List of formant bandwidths. Default is None (uses default bandwidths).
    Returns:
        None
    """
    files = os.listdir(audio_folder_path)
    if add_white_noise:
        title = "Create mels with white noise"
    elif add_formant_noise:
        title = "Create mels with formant noise"
    elif add_pink_noise:
        title = "Create mels with pink noise"
    else:
        title = "Create mels without noise"
    for file in tqdm(files, desc=title):
        if not file.endswith(".wav"):
            continue
        path_to_file = os.path.join(audio_folder_path, file)
        output_image_path = os.path.join(
            save_images_folder, file.split(".")[0] + ".png"
        )
        plot_and_save_mel_spectrogram(
            path_to_file,
            output_image_path,
            sample_rate=sample_rate,
            add_white_noise=add_white_noise,
            noise_level=noise_level,
            add_formant_noise=add_formant_noise,
            num_formants=num_formants,
            formant_freqs=formant_freqs,
            formant_bw=formant_bw,
            add_pink_noise=add_pink_noise,
        )


if __name__ == "__main__":
    Fire(convert_wavs_to_mels)
