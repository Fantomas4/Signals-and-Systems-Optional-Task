def MyConvolve(a_vector, b_vector):
    # y_vector holds the result of the convolution
    # initialize the y_vector with 0s
    y_vector = [0] * (len(a_vector) + len(b_vector) - 1)

    print("DIAG: y_vector:", y_vector)

    # i holds the index of the first element of a_vector that belongs
    # to the sliding window's current instance
    i = 0

    # j holds the index of the last element of a_vector that belongs
    # to the sliding window's current instance
    j = len(b_vector) - 1

    # n holds the index of the result vector where
    # we are currently doing calculations
    n = 0

    while j < len(a_vector):
        b_index = 0
        for k in range(i, j + 1):
            y_vector[n] += a_vector[k] * b_vector[b_index]
            b_index += 1

        print("y_vector is: " + str(y_vector))
        # print("DIAG: For n = " + str(n) + " y_vector is: " + str(y_vector[n]))

        i += 1
        j += 1
        n += 1

    return y_vector


if __name__ == '__main__':
    # Get user's input for N and check whether it is greater than 10
    a_vector_len = int(input("Enter the random vector length N (N>10): "))
    while a_vector_len <= 10:
        a_vector_len = int(input("Wrong input. N must be greater than 10. Try again: "))

    print("DIAG: vector_len: ", a_vector_len)

    # # generate random floating point values
    # from numpy.random import seed
    # from numpy.random import rand
    #
    # # seed random number generator
    # seed(1)
    # # generate random numbers between 0-1
    # a_vector = rand(a_vector_len)

    # import random
    # a_vector = random.sample(range(1, 100), a_vector_len)

    # TEST ONLY!
    a_vector = [1, 4, 5, 6, 7, 8, 9, 10, 22, 56, 2, 3, 11]

    print("DIAG: a_vector: ", a_vector)

    b_vector = [1/5, 1/5, 1/5, 1/5, 1/5]

    print("DIAG: b_vector: ", b_vector)

    print(MyConvolve(a_vector, b_vector))


