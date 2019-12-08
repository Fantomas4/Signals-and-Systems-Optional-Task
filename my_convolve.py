import threading
import time


def ConvolutionThread(a_vector, b_vector, index, y_vector, yLocker):
    number = 0
    if index < len(b_vector) - 1:  # b_vector is not in the frame yet
        for position, j in enumerate(a_vector[:index + 1]):
            number += j * b_vector[-1 - position]
    elif index < len(a_vector):  # b_vector is inside the frame
        for position, j in enumerate(a_vector[index - len(b_vector) + 1:index + 1]):
            number += j * b_vector[position]
    else:  # b_vector is leaving the frame
        for position, j in enumerate(a_vector[index - len(b_vector) + 1:]):
            number += j * b_vector[position]
    while yLocker.locked():
        continue
    yLocker.acquire()
    y_vector[index] = round(number, 4)
    yLocker.release()


def MyConvolve(a_vector, b_vector):
    """
    b_vector is smaller that the a_vector
    """
    y_vector = [0 for i in range(len(a_vector) + len(b_vector) - 1)]
    maximum = len(y_vector)
    print(maximum)
    yLocker = threading.Lock()
    threads = []
    for i in range(len(a_vector) + len(b_vector) - 1):
        print(i)
        t = threading.Thread(target=ConvolutionThread, args=(a_vector, b_vector, i, y_vector, yLocker))
        t.start()
        threads.append(t)

        # Up to 16 active threads can be executed concurrently at the same time.
        # If there are 16 threads already running, wait until one of them finishes
        # and spawn the new thread then.
        while True:
            active = 0
            for thread in threads:
                if thread.isAlive():
                    active += 1
            if active < 16:
                break
            else:
                # There are already 16 threads being executed,
                # so we wait for a second and repeat the loop
                # in order to check if one of them has finished
                time.sleep(1)
    [t.join() for t in threads]
    return y_vector
