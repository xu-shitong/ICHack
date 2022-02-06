from scipy.io import wavfile

# from speech_to_text.Audio_into_Words import speech_to_word_list
import torch
import numpy as np
from scipy.io import wavfile
from torch_pitch_shift import *
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.special import softmax

PITCH_SHIFT_RATE = 0.001

# TODO: remove and use the pretrained speech to word
def speech_to_word_list(music):
  for i in range(0, music.shape[0], 65403):
    print("i :", i, "out off: ", music.shape[0] // 65403)
    yield "", i, i + 65403

# classify how high the pitch is, by calculating weighted fft
def classify_pitch(fft_output, range):
  fft_real = fft_output.real[:range // 2]
  soft_max_output = softmax(fft_real)
  return (soft_max_output * np.arange(range // 2)).sum()

# get a word string, return the (sample rate, wav file) tuple
def word_to_wav(word):
  # TODO: fetch file according to word
  return wavfile.read("./male_noise4.wav")

# get music numpy between start end time stamp
def get_music_fragment(music, start, end):
  return music[start : end]

# take 2 input files
_, raw_music = wavfile.read("./auld_lang_syne.wav")
print(raw_music.shape)
dictionary = speech_to_word_list(raw_music)

output_voice_tensor = None
# for each time slice of the word, tune the sound
cnt = 0
for word, start, end in dictionary:
  if cnt > 10:
    break
  cnt += 1
  music = get_music_fragment(raw_music, start, end)

  # 1. read human voice file TODO: check valid file
  #    fit the voice file to the music file, if more than the music file, cast
  SAMPLE_RATE, voice = word_to_wav(word)
  DTYPE = voice.dtype
  print("music shape: ", music.shape)
  print("voice shape: ", voice.shape)
  time_length = min(music.shape[0], voice.shape[0])

  # 2. split to intervals, interval as one second
  FEATURE_NUM = min(256, SAMPLE_RATE)
  if time_length // FEATURE_NUM <= 0:
    break
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
  print("pitch tuning amount ", 2 * int(PITCH_SHIFT_RATE * (voice_pitch - music_pitch)**2))
  voice_new_pitch = pitch_shift(voice_new_pitch, 2 * int(PITCH_SHIFT_RATE * (voice_pitch - music_pitch)**2), SAMPLE_RATE)

  # discard batch number
  voice_new_pitch = voice_new_pitch[0]

  if output_voice_tensor == None:
    output_voice_tensor = voice_new_pitch
  else:
    output_voice_tensor = torch.hstack([output_voice_tensor, voice_new_pitch])
  print(output_voice_tensor.shape)

print(output_voice_tensor.shape)
wavfile.write(
    "./shifted_octave_+1.wav",
    SAMPLE_RATE,
    np.swapaxes(output_voice_tensor.cpu().numpy(), 0, 1).astype(DTYPE),
)
  