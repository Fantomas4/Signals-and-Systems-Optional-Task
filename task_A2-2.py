import numpy
from scipy.io import wavfile

import my_convolve


if __name__ == '__main__':

    # import the audio file
    fs2, audio_sample_data = wavfile.read('sample_audio.wav')

    # generate a random white noise
    mean = 0
    std = 1
    num_of_samples = 10
    white_noise_data = numpy.random.normal(mean, std, size=num_of_samples)

    # Convert the list returned by MyConvolve to the necessary numpy array format required by wavfile.write()
    convolution_array = numpy.array(my_convolve.MyConvolve(audio_sample_data, white_noise_data), dtype=numpy.float32)

    # call MyConvolve method to perform the convolution between the sample audio and the white noise
    # and write the result to the output audio file
    wavfile.write("whiteNoise_sampleAudio.wav", fs2, convolution_array)
