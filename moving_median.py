import numpy as np


def ArrayChallenge(arr):

    # code goes here
    N = arr[0]
    arr = arr[1:]
    length = len(arr)

    sol = []
    cols = []
    for i in range(length):
        cols.append(arr[i])
        sol.append(int(np.median(cols)))

    return ",".join(map(str, sol))


# keep this function call here
print(ArrayChallenge(input()))
