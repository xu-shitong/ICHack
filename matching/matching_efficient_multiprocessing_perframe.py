import numpy as np
import multiprocessing as mp
import time

results = []

def get_result(result):
    global results
    results.append(result) 

# Comparing one row
def mse(song, speech):
    mse_error = np.square(np.subtract(speech,song)).mean()
    return mse_error

def match(song, speech):
    # song is a mxn matrix
    # speech is a pxn matrix
    # same number of columns, different number of rows
    global results
    results = []
    output = []

    if len(song[0]) == len(speech[0]):
        for i in range(len(song)):
            pool = mp.Pool(mp.cpu_count())
            print("CPU count = " + str(mp.cpu_count()))
            
            for j in range(len(speech)):
                pool.apply_async(mse, args=(song[i], speech[j]), callback=get_result)
            pool.close()
            pool.join()
            index = np.argmin(results)
            output.append(results[index])            
        
    else:
        print("Column numbers do not match")
        exit
    
    return output

def main ():
    # song_ex = [[1,2,3,4,5],[3,5,6,7,8]]
    # speech_ex = [[1,2,3,4,5],[6,7,8,9,10],[3,4,6,8,9]]
    t0 = time.time()

    row_num = 10
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