def MyConvolve(a_vector, b_vector):
    # y_vector holds the result of the convolution
    # initialize the y_vector with 0s
    y_vector = [0] * (len(a_vector) + len(b_vector) - 1)

    # print("DIAG: y_vector:", y_vector)

    # i holds the index of the first element of a_vector that belongs
    # to the sliding window's current instance
    i = 0

    # j holds the index of the last element of a_vector that belongs
    # to the sliding window's current instance
    j = 0

    # n holds the index of the result vector where
    # we are currently doing calculations
    n = 0


    # At first, the sliding window has not fully covered
    # the indexes of vector A
    import tqdm
    pbar = tqdm.tqdm(total=len(b_vector))

    while j < len(b_vector) - 1:
        # print("DIAG: Loop1")
        b_index = 0
        for k in range(i, j + 1):
            y_vector[n] += a_vector[k] * b_vector[b_index]
            b_index += 1
        j += 1
        n += 1
        pbar.update(1)
    pbar.close()

    # The sliding window has now fully covered the first
    # 5 indexes of vector A
    pbar = tqdm.tqdm(total=len(a_vector)-j-1)
    while j < len(a_vector):
        print("DIAG: Loop2")
        b_index = 0
        for k in range(i, j + 1):
            y_vector[n] += a_vector[k] * b_vector[b_index]
            b_index += 1
        print("y_vector is: " + str(y_vector))
        # print("DIAG: For n = " + str(n) + " y_vector is: " + str(y_vector[n]))
        i += 1
        j += 1
        n += 1
        pbar.update(1)
    pbar.close()

    # Finally, the sliding window has to fully stop covering all
    # of A vector's indexes
    pbar = tqdm.tqdm(total=j-i-1)
    while i < j:
        print("DIAG: Loop3")
        b_index = 0
        for k in range(i, j):
            y_vector[n] += a_vector[k] * b_vector[b_index]
            b_index += 1
        i += 1
        n += 1
        pbar.update(1)
    pbar.close()

    return y_vector

