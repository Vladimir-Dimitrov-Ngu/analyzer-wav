import numpy as np


def generate_formant_like_noise(
    duration, sampling_rate, num_formants=3, formant_freqs=None, formant_bw=None
):
    """
    Generates a noise signal with formant-like characteristics.

    Args:
        duration (float): Duration of the signal in seconds.
        sampling_rate (int): Sampling rate of the signal in Hz.
        num_formants (int, optional): Number of formants to include in the signal. Defaults to 3.
        formant_freqs (list, optional): List of formant frequencies in Hz. If not provided, defaults to [500, 1500, 2500].
        formant_bw (list, optional): List of formant bandwidths in Hz. If not provided, defaults to [80, 80, 80].

    Returns:
        np.ndarray: A noise signal with formant-like characteristics, normalized to [-1, 1].

    """
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
    """
    Generates pink noise (1/f noise) for a given duration and sampling rate.

    Args:
        duration (float): Duration of the noise signal in seconds.
        sampling_rate (int): Sampling rate of the noise signal in Hz.

    Returns:
        np.ndarray: A pink noise signal, normalized to [-1, 1].

    """
    num_samples = int(duration * sampling_rate)
    pink_noise = np.zeros(num_samples)
    b = [0.049922035, -0.095993537, 0.050612699, -0.004408786]
    a = [1, -2.494956002, 2.017265875, -0.522189400]

    pink_noise = np.random.randn(num_samples)
    pink_noise = np.convolve(pink_noise, b)
    pink_noise = np.convolve(pink_noise, a)

    return pink_noise[:num_samples]
