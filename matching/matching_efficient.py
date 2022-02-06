import numpy as np
import time

def mse(song, speech):
    mse_error = np.square(np.subtract(speech,song)).mean()
    return mse_error

def match(song, speech):
    # song is a mxn matrix
    # speech is a pxn matrix
    # same number of columns, different number of rows
    output = []
    if len(song[0]) == len(speech[0]):
        for i in range(len(song)):
            song_row = song[i]
            mse_list = np.array([mse(row, song_row) for row in song])
            index = np.argmin(mse_list)
            output_row = speech[index]
            output.append(output_row)
    else:
        print("Column numbers do not match")
        exit
    
    return output

def main ():
    song_ex = [[1,2,3,4,5],[3,5,6,7,8]]
    speech_ex = [[1,2,3,4,5],[6,7,8,9,10],[3,4,6,8,9]]
    t0 = time.time()

    # song_ex = np.random.randint(1,100, size=(100,100))
    print("song_ex = " + str(song_ex))

    # speech_ex = np.random.randint(1,100, size=(100,100))
    print("speech_ex = " + str(speech_ex))

    output = match(song_ex, speech_ex)
    print("output" + str(output))

    t1 = time.time() - t0
    print("time elapsed:" + str(t1))
  
if __name__ == '__main__':
    main()