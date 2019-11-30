#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:32:48 2019

@author: mavroudo
"""

from scipy.io import wavfile

fs, dataPink = wavfile.read('pink_noise.wav') #change sampling rate 
fs, dataSample = wavfile.read('sample_audio.wav')

import threading
import time
def ConvolutionThread(a_vector,b_vector,index,y_vector,yLocker):
    number=0
    if index<len(b_vector): #b_vector is not in the frame yet
        for j in a_vector[:index+1]:
            number+=j*b_vector[len(b_vector)-1-index+j]
    elif index<len(a_vector): # vector is inside
        for position,j in enumerate(a_vector[index-len(b_vector):index+1]):
            number+=j*b_vector[position]
    else: #b vector is leaving
        for position,j in enumerate(a_vector[index-len(a_vector):]):
            number+=j*b_vector[position]
    while yLocker.locked():
       continue
    yLocker.acquire()
    yLocker[index]=number
    yLocker.release()
        

def Myconvolution(a_vector,b_vector):
    """
    b_vector is smaller that the a_vector
    """
    y_vector=[0 for i in range(len(a_vector)+len(b_vector)-1)]
    yLocker=threading.Lock()
    threads=[]
    for i in range(len(a_vector)+len(b_vector)-1):
        t=threading.Thread(target=ConvolutionThread,args=(a_vector,b_vector,i,y_vector,yLocker))
        t.start()
        threads.append(t)
        while True:
            active=0
            for thread in threads:
                if thread.isAlive() : 
                    active+=1
            if active<8:
                break
            else:
                time.sleep(2)
    return y_vector
    
a_vector = [1, 4, 5, 6, 7, 8, 9, 10, 22, 56, 2, 3, 11]
b_vector = [1/5, 1/5, 1/5, 1/5, 1/5]
print(Myconvolution(a_vector, b_vector))