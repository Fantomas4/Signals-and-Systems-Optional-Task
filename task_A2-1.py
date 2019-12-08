import librosa
from scipy.io import wavfile

import my_convolve

if __name__ == '__main__':

    fs1, dataPink = wavfile.read('pink_noise.wav')  # change sampling rate
    fs2, dataSample = wavfile.read('sample_audio.wav')
    dataPink, y1 = librosa.load("pink_noise.wav", min(fs1, fs2))
    dataSample, y2 = librosa.load("sample_audio.wav", min(fs1, fs2))

    wavfile.write("output.wav", y1, my_convolve.MyConvolve(dataSample, dataPink))
