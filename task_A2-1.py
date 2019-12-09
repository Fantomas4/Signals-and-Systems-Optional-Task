import librosa
from scipy.io import wavfile

import my_convolve

if __name__ == '__main__':

    # import the pink noise audio file
    fs1, dataPink = wavfile.read('pink_noise.wav')  # change sampling rate

    # import the sample audio file
    fs2, dataSample = wavfile.read('sample_audio.wav')

    # adjust the sampling rate of the audio signal with the highest sampling rate to match
    # the sampling rate of the audio signal with the lowest sampling rate.
    dataPink, y1 = librosa.load("pink_noise.wav", min(fs1, fs2))
    dataSample, y2 = librosa.load("sample_audio.wav", min(fs1, fs2))

    # call MyConvolve method to perform the convolution between the sample audio and the pink noise
    # and write the result to the output audio file
    wavfile.write("pinkNoise_sampleAudio.wav", y1, my_convolve.MyConvolve(dataSample, dataPink))
