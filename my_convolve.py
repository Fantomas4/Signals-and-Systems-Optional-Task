def MyConvolve(a_vector, b_vector):
    # y_vector holds the result of the convolution
    # initialize the y_vector with 0s
    y_vector = [0] * (len(a_vector) + len(b_vector) - 1)

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
    # (The sliding window is entering A vector's frame)
    while j < len(b_vector) - 1:
        b_index = 0
        for k in range(i, j + 1):
            y_vector[n] += a_vector[k] * b_vector[b_index]
            b_index += 1
        j += 1
        n += 1

    # The sliding window has now fully covered the first
    # 5 (5 is b_vector's size) indexes of vector A
    # (the sliding windows has entered A vector's frame)
    while j < len(a_vector):
        b_index = 0
        for k in range(i, j + 1):
            y_vector[n] += a_vector[k] * b_vector[b_index]
            b_index += 1
        i += 1
        j += 1
        n += 1

    # Finally, the sliding window has to stop covering
    # A vector's indexes
    # (The slide window is leaving A vector's frame)
    while i < j:
        b_index = 0
        for k in range(i, j):
            y_vector[n] += a_vector[k] * b_vector[b_index]
            b_index += 1
        i += 1
        n += 1

    return y_vector

