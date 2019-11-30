#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:32:48 2019

@author: mavroudo
"""

from scipy.io import wavfile
import threading
import time
import librosa


def ConvolutionThread(a_vector, b_vector, index, y_vector, yLocker):
    number = 0
    if index < len(b_vector) - 1:  # b_vector is not in the frame yet
        for position, j in enumerate(a_vector[:index + 1]):
            number += j * b_vector[-1 - position]
    elif index < len(a_vector):  # vector is inside
        for position, j in enumerate(a_vector[index - len(b_vector) + 1:index + 1]):
            number += j * b_vector[position]
    else:  # b vector is leaving
        for position, j in enumerate(a_vector[index - len(b_vector) + 1:]):
            number += j * b_vector[position]
    while yLocker.locked():
        continue
    yLocker.acquire()
    y_vector[index] = round(number, 4)
    yLocker.release()


def Myconvolution(a_vector, b_vector):
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
        while True:
            active = 0
            for thread in threads:
                if thread.isAlive():
                    active += 1
            if active < 16:
                break
            else:
                time.sleep(1)
    [t.join() for t in threads]
    return y_vector


# 696473

fs1, dataPink = wavfile.read('pink_noise.wav')  # change sampling rate
fs2, dataSample = wavfile.read('sample_audio.wav')
dataPink, y1 = librosa.load("pink_noise.wav", min(fs1, fs2))
dataSample, y2 = librosa.load("sample_audio.wav", min(fs1, fs2))

wavfile.write("output.wav", y1, Myconvolution(dataSample, dataPink))
