import tqdm

def MyConvolve(a_vector, b_vector):

    y_vector = [0] * (len(a_vector) + len(b_vector) - 1)

    for i in tqdm.trange(0, len(a_vector)):
        for k in range(0, len(b_vector)):
            y_vector[i + k - 1] += b_vector[k] * a_vector[i]
    print("finished!")
    return y_vector

