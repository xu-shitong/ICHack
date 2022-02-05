import numpy as np
import time

def match(song, speech):
    # song is a mxn matrix
    # speech is a pxn matrix
    # same number of columns, different number of rows
    output = []
    if len(song[0]) == len(speech[0]):
        for i in range(len(song)):
            song_row = song[i]
            # print(song_row)
            output_mse = (0,[])
            for j in range(len(speech)):
                speech_row = speech[j]
                mse = np.square(np.subtract(speech_row,song_row)).mean()
                if mse == 0:
                    output_mse = (0, speech_row)
                    break
                # print("mse ="+ str(mse))
                if mse > output_mse[0] and output_mse[0] != 0: # If mse larger than previous entry, discard
                    pass
                else:
                    output_mse = (mse, speech_row)
            output.append(output_mse[1])
        print("output" + str(output))
    else:
        print("Column numbers do not match")
        exit

def main ():
    # song_ex = [[1,2,3,4,5],[3,5,6,7,8]]
    # speech_ex = [[1,2,3,4,5],[6,7,8,9,10],[3,4,6,8,9]]

    t0 = time.time()

    song_ex = np.random.randint(1,100, size=(100,100))
    print("song_ex = " + str(song_ex))

    speech_ex = np.random.randint(1,100, size=(100,100))
    print("speech_ex = " + str(speech_ex))

    match(song_ex, speech_ex)

    t1 = time.time() - t0

    print("now: " + str(t1) + " time elapsed: " + str(t1-t0))
  
if __name__ == '__main__':
    main()