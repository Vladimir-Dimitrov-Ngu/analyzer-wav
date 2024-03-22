# WAV analyzer with Noise Detection Neural Network

## File Preparation

Place your WAV file in the following directory:
```
/data
```

## Setting Parameters

Specify the necessary arguments in the file 
```
input_variables.txt.
```
## Running the Analysis

Open the terminal and execute the command:
```bash
bash process_audio.sh
```

## Docker 
Build docker image:
```bash
docker build --build-arg ENVIRONMENT=<your_environment> -t <image_name>:latest .
```

Run docker container:
```bash
docker run -it <image_name>
```

Interactive format:
```bash
docker run -it <image_name> bash    
```

## Functionality:

- Audio File Splitting. The file will be divided into required segments for analysis.
- Noise Type Specification. Choose between pink or white noise.
- Dataset Creation. Analysis results will be utilized to generate a dataset.
- Noise Detection Neural Network. Utilizes a trained neural network capable of accurately detecting various types of noise within the audio file.

## Stack
1. Programming Languages: Bash scripting for automation.
2. Neural Network Framework: Python with PyTorch for implementing and training the neural network.
3. File Handling: Utilizes standard file handling libraries in Python.
4. Audio Libraries: Audio processing libraries like Librosa.

## Contributing
Copy of the [`contributing.md`](https://github.com/Vladimir-Dimitrov-Ngu/analyzer-wav/blob/master/contributing.md).

## Authors
- [Vladimir Dimitrov](https://github.com/Vladimir-Dimitrov-Ngu)