from scipy.io import wavfile
import torch
import numpy as np

PAUSE_CONST = 10000

def merge(names, output_name):
  result = None
  for name in names:
    if name == "pause":
      result = np.vstack([result, np.zeros((PAUSE_CONST, result.shape[1]))])
    else:
      SAMPLE_RATE, wavefront = wavfile.read(name)
      DTYPE = wavefront.dtype
      if result is None:
        result = wavefront
      else:
        result = np.vstack([result, wavefront])

  wavfile.write(
      output_name,
      SAMPLE_RATE,
      result.astype(DTYPE)
  )
  return result
