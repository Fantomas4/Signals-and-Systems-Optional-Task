import my_convolve

if __name__ == '__main__':
    # Get user's input for N and check whether it is greater than 10
    # a_vector_len = int(input("Enter the random vector length N (N>10): "))
    # while a_vector_len <= 10:
    #     a_vector_len = int(input("Wrong input. N must be greater than 10. Try again: "))
    #
    # print("DIAG: vector_len: ", a_vector_len)
    a_vector_len = 13

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

    print(my_convolve.MyConvolve(a_vector, b_vector))


