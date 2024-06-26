#!/bin/bash
source input_variables.txt

# Command to create sliced WAV files
python3 scripts/split_wav.py "$WAV_FILE" "$SLICED_FOLDER" --trim_seconds=5

# Command to generate white noise folder
python3 scripts/add_noise.py ./data/sliced/example ./data/noise/White --add_white_noise=True --white_noise_level=0.3

# Command to generate pink noise folder
python3 scripts/add_noise.py ./data/sliced/example ./data/noise/Pink --add_pink_noise=True

# Command to denoising white noise 
python3 scripts/denoising.py ./data/noise/White ./data/denoising/White

# Command to denoising pink noise 
python3 scripts/denoising.py ./data/noise/Pink ./data/denoising/Pink

# Command to convert WAV files to Mel spectrograms without adding noise
python3 scripts/wav_to_mel.py "$SLICED_FOLDER" "$MEL_TRUE_FOLDER"

# Command to convert WAV files to Mel spectrograms with adding noise
python3 scripts/wav_to_mel.py "$SLICED_FOLDER" "$MEL_WHITE_NOISE_FOLDER" --add_white_noise=True

# Command to convert WAV files to Mel spectrograms with adding noise
python3 scripts/wav_to_mel.py "$SLICED_FOLDER" "$MEL_PINK_NOISE_FOLDER" --add_pink_noise=True

# Command to create train and test folders
python3 scripts/create_dataset.py    

echo "Everything is ready"
