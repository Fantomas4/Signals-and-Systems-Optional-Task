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

    import random
    a_vector = random.sample(range(1, 100), a_vector_len)

    print("DIAG: random_vector: ", a_vector)

    b_vector = [1/5, 1/5, 1/5, 1/5, 1/5]

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
