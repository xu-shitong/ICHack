import numpy as np
import multiprocessing as mp
import time

# TODO: Return index of song in front, and re-order with that
# TODO: Remove index from MSE calculation

row_num = 3
col_num = 5
results = []

def get_result(result):
    global results
    results.append(result) 
    # results = np.append(results,np.array([result]))

# Comparing one row to all other rows and re-ordering
def list_mse(song_row, speech):
    mse_list = np.array([mse(row, song_row[1:]) for row in speech])
    mse_min_index = np.argmin(mse_list)
    song_index = song_row[0]
    output_row = np.array(speech[mse_min_index])
    output_row = np.insert(speech[mse_min_index], 0, np.array([song_index]), axis=0) # append indices
    print(output_row)
    return output_row

# Comparing one row
def mse(song, speech):
    if (len(song) != len(speech)):
        print("dimensions don't match!")
    else:
        mse_error = np.square(np.subtract(speech,song)).mean()
    return mse_error

def match(song, speech):
    # song is a mxn matrix
    # speech is a pxn matrix
    # same number of columns, different number of rows
    pool = mp.Pool(mp.cpu_count())
    print("CPU count = " + str(mp.cpu_count()))

    for i in range(len(song)):
        song_row = song[i]
        pool.apply_async(list_mse, args=(song_row, speech), callback=get_result)
    pool.close()
    pool.join()
    
    return results

def main ():
    song_ex = np.array([[1,2,3,4,5],[3,5,6,7,8],[3,4,6,8,9]])
    speech_ex = np.array([[1,2,3,4,5],[6,7,8,9,10],[3,4,6,8,9]])
    t0 = time.time()

    global row_num
    global col_num
    indices = list(range(row_num))

    # song_ex = np.random.randint(1,100, size=(row_num,col_num))
    song_ex = np.insert(song_ex, 0, indices, axis=1) # append indices

    # speech_ex = np.random.randint(1,100, size=(row_num,col_num))
    # speech_ex = np.insert(speech_ex, 0, indices, axis=1) #NOTE: don't need to insert speech

    print("song_ex = " + str(song_ex))
    print("speech_ex = " + str(speech_ex))

    output = match(song_ex, speech_ex)

    #sorted_output = output[np.argsort(output[:, 0])]

    t1 = time.time() - t0
    print("sorted_output: ") 
    print(output)

    print("time elapsed:" + str(t1))
  
if __name__ == '__main__':
    main()