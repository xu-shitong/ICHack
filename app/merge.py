from scipy.io import wavfile
import numpy as np

PAUSE_CONST = 10000
SAMPLE_RATE = 48000

def merge(names, output_name):
  print(names)
  result = None
  for name in names:
    if name == "pause":
      result = np.vstack([result, np.zeros((PAUSE_CONST, result.shape[1]))])
    else:
      n, wavefront = wavfile.read(name)
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
