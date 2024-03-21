# analyzer-wav



python3 scripts/create_wav.py './data/Kuji_Podcast_150.wav' './data/sliced' 
python3 scripts/wav_to_mel.py './data/sliced/Kuji' './mel-spectrogram/Kuji/True' --add_noise=False
python3 scripts/wav_to_mel.py './data/sliced/Kuji' './mel-spectrogram/Kuji/Noise' --add_noise=True
