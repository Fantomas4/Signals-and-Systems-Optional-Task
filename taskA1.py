import numpy

import my_convolve

if __name__ == '__main__':
    # Get user's input for N and check whether it is greater than 10
    a_vector_len = int(input("=> Enter the random vector length N (N>10): "))
    while a_vector_len <= 10:
        a_vector_len = int(input("\n=> Wrong input. N must be greater than 10. Try again: "))

    # Use numpy's random.uniform to generate random floating numbers from within the range [-100.0, 100.0)
    a_vector = numpy.random.uniform(low=-100.0, high=100.0, size=a_vector_len)

    print("\n=> The random vector generated with the requested length is: ", a_vector)

    b_vector = [1/5, 1/5, 1/5, 1/5, 1/5]

    print("\n=> The second vector used for the convolution is: ", b_vector)

    print("\n=> The result vector of the convolution is: ", my_convolve.MyConvolve(a_vector, b_vector))


