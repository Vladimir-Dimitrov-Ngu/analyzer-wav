import librosa
import soundfile as sf
import os
from fire import Fire


def split_audio(
    input_file: str, output_dir: str, segment_duration=10, trim_seconds=60
) -> None:
    """
    Splits an audio file into segments of specified duration.

    Parameters:
        input_file (str): Path to the input audio file.
        output_dir (str): Path to the output directory where segments will be saved.
        segment_duration (float): Duration of each segment in seconds. Default is 10.
        trim_seconds (int): Number of seconds to trim from the beginning and end of the audio. Default is 60.

    Returns:
        None: The function saves the segments of the audio file in the output directory.
    """
    y, sr = librosa.load(input_file, sr=None)
    trim_samples = trim_seconds * sr
    y_trimmed = y[trim_samples:-trim_samples]
    input_file_name = input_file.split("/")[-1].split(".")[0]
    segment_samples = segment_duration * sr
    for i, start_sample in enumerate(range(0, len(y_trimmed), segment_samples)):
        segment = y_trimmed[start_sample : start_sample + segment_samples]
        output_file = os.path.join(output_dir, f"{input_file_name}_segment_{i+1}.wav")
        sf.write(output_file, segment, sr)


if __name__ == "__main__":
    Fire(split_audio)
