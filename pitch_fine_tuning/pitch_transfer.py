import torch
import numpy as np
from scipy.io import wavfile
from torch_pitch_shift import *
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.special import softmax


# # read an audio file
# SAMPLE_RATE, sample = wavfile.read("./raw_voice.wav")

# # convert to tensor of shape (batch_size, channels, samples)
# dtype = sample.dtype
# print(sample.shape)
# sample = torch.tensor(
#     [np.swapaxes(sample, 0, 1)],  # (samples, channels) --> (channels, samples)
#     dtype=torch.float32,
# )

# up = pitch_shift(sample, -12, SAMPLE_RATE)
# assert up.shape == sample.shape
# wavfile.write(
#     "./shifted_octave_+1.wav",
#     SAMPLE_RATE,
#     np.swapaxes(up.cpu()[0].numpy(), 0, 1).astype(dtype),
# )

PITCH_SHIFT_RATE = 0.03

def classify_pitch(fft_output, range):
  fft_real = fft_output.real[:range // 2]
  soft_max_output = softmax(fft_real)
  return (soft_max_output * np.arange(range // 2)).sum()

sample_rate_1, music = wavfile.read("./raw_voice.wav")

# 1. read 2 files TODO: check valid file
#    fit the voice file to the music file, if more than the music file, cast
SAMPLE_RATE, voice = wavfile.read("./male_noise.wav")
DTYPE = voice.dtype
time_length = min(music.shape[0], voice.shape[0])

# 2. split to intervals, interval as one second
FEATURE_NUM = min(256, SAMPLE_RATE)
indices = list(range(0, time_length, time_length // FEATURE_NUM))
fft_music_samples = music[indices, 0]
fft_voice_samples = voice[indices, 0]

# 3. apply fft on each
fft_music_output = fft(fft_music_samples)
fft_voice_output = fft(fft_voice_samples)

# 4. calculate softmax
voice_pitch = classify_pitch(fft_voice_output, FEATURE_NUM)
music_pitch = classify_pitch(fft_music_output, FEATURE_NUM)

# 5. change pitch of the segment
voice_new_pitch = torch.tensor(
    [np.swapaxes(voice, 0, 1)],  # (samples, channels) --> (channels, samples)
    dtype=torch.float32,
)
voice_new_pitch = pitch_shift(voice_new_pitch, 4 * int(PITCH_SHIFT_RATE * (voice_pitch - music_pitch)), SAMPLE_RATE)
# voice_new_pitch = pitch_shift(voice_new_pitch, -12, SAMPLE_RATE)

wavfile.write(
    "./shifted_octave_+1.wav",
    SAMPLE_RATE,
    np.swapaxes(voice_new_pitch.cpu()[0].numpy(), 0, 1).astype(DTYPE),
)
