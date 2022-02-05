import numpy as np
import multiprocessing as mp
import time

results = []

def get_result(result):
    global results
    results.append(result) 

# Comparing one row to all other rows and re-ordering
def list_mse(song_row, speech):
    mse_list = np.array([mse(row, song_row) for row in speech])
    index = np.argmin(mse_list)
    return speech[index]

# Comparing one row
def mse(song, speech):
    mse_error = np.square(np.subtract(speech,song)).mean()
    return mse_error

def match(song, speech):
    # song is a mxn matrix
    # speech is a pxn matrix
    # same number of columns, different number of rows
    # results = []
    pool = mp.Pool(mp.cpu_count())
    print("CPU count = " + str(mp.cpu_count()))

    if len(song[0]) == len(speech[0]):
        for i in range(len(song)):
            song_row = song[i]
            # output_row = list_mse(song_row, speech)
            # results.append(output_row)
            # get_result(list_mse(song_row, speech))
            pool.apply_async(list_mse, args=(song_row, speech), callback=get_result)
        pool.close()
        pool.join()
    else:
        print("Column numbers do not match")
        exit
    
    return results

def main ():
    # song_ex = [[1,2,3,4,5],[3,5,6,7,8]]
    # speech_ex = [[1,2,3,4,5],[6,7,8,9,10],[3,4,6,8,9]]
    t0 = time.time()

    row_num = 1000
    col_num = 10
    indices = list(range(row_num))

    song_ex = np.random.randint(1,100, size=(row_num,col_num))
    song_ex = np.insert(song_ex, 0, indices, axis=1) # append indices

    # speech_ex = np.random.randint(1,100, size=(row_num,col_num))
    # speech_ex = np.insert(speech_ex, 0, indices, axis=1)
    speech_ex = song_ex

    print("song_ex = " + str(song_ex))
    print("speech_ex = " + str(speech_ex))

    output = match(song_ex, speech_ex)

    t1 = time.time() - t0
    print("output" + str(output))   
    print("time elapsed:" + str(t1))
  
if __name__ == '__main__':
    main()