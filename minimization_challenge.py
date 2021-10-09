def ArrayChallenge(arr):

    # code goes here
    N = arr[0]
    size = len(arr)
    diff = 0
    new_list = []

    for q in range(1, size - 1):
        a = arr[q] - arr[q + 1]
        if a < 0:
            a = a * -1

        diff = diff + a
        new_list.append(arr[q])

    if diff == 0:
        return 0

    new_list.append(arr[size - 1])

    sorted_list = sorted(new_list, reverse=True)
    give = True
    while give:
        give = False
        for i in range(0, len(sorted_list) - 1):

            temp = sorted_list[i] - sorted_list[i + 1]

            if temp != 0 and N > 0:
                if temp < 0:
                    sorted_list[i] = sorted_list[i] - N
                    give = True
                else:
                    sorted_list[i] = sorted_list[i] - temp
                    N = N - temp
                    give = True

                break

    diff = 0
    for x in range(0, len(sorted_list) - 1):
        a = sorted_list[x] - sorted_list[x + 1]
        if a < 0:
            a = a * -1

        diff = diff + a

    return diff


# keep this function call here
print(ArrayChallenge(input()))
