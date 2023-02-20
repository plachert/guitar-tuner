import numpy as np


def calc_amp_spect(data: np.ndarray, sr: int):
    dtype = data.dtype
    data -= np.mean(data).astype(dtype)
    data = np.hanning(data.size) * data
    spect = np.abs(np.fft.rfft(data))
    freq = np.fft.rfftfreq(data.size, d=1./sr)
    return freq, spect
    
def downsample(spect: np.ndarray, factor: int = 2):
    return spect[::factor]

def hps(data, sr, no_harmonics=7):
    freq, spect = calc_amp_spect(data, sr)
    harmonics = np.zeros((spect.size, no_harmonics))
    for i in range(no_harmonics):
        downsampled = downsample(spect, factor=i+1)
        harmonics[:downsampled.size, i] = downsampled
    harmonics_product = np.prod(harmonics, axis=-1)
    return freq, harmonics_product

def get_fundamental(data: np.ndarray, sr: int = 8000):
    freqs, harmonics = hps(data, sr)
    idx = np.argmax(harmonics)
    return freqs[idx]