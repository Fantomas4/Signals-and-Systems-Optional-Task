def MyConvolve(a_vector, b_vector):

    # y_vector holds the result of the convolution
    # initialize the y_vector with 0s
    y_vector = [0] * (len(a_vector) + len(b_vector) - 1)

    # n is the index counter of y_vector
    n = 0

    a_vector_len = len(a_vector)
    b_vector_len = len(b_vector)

    # Check if the kernel (b_vector) is of even size
    if b_vector_len % 2 == 0:
        # If so, add a "0" to the end of the vector to
        # make its size odd
        b_vector.append(0)

    for i in range(0, a_vector_len):
        # Calculate the center index of the kernel
        center_index = int((b_vector_len - 1) / 2)

        a_start_index = int(i - (b_vector_len - 1) / 2)
        b_start_index = a_start_index
        # Check if a_start_index goes out of the a_vector's bounds
        if a_start_index < 0:
            a_start_index = 0
            b_start_index = int(((b_vector_len - 1) / 2) - i)

        a_end_index = int(i + (b_vector_len - 1) / 2)
        # Check if a_end_index goes out of the b_vector's bounds
        if a_end_index > a_vector_len - 1:
            a_end_index = a_vector_len - 1

        b_cur_pos = b_start_index
        for k in range(a_start_index, a_end_index + 1):
            y_vector[n] += a_vector[k] * b_vector[b_cur_pos]
            b_cur_pos += 1

        n += 1

    return y_vector





