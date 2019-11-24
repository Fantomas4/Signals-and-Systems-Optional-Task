import wave
import numpy
import my_convolve

if __name__ == '__main__':
    sound_file_1 = wave.open("sample_audio.wav", "r")
    sound_file_2 = wave.open("pink_noise.wav", "r")

    print("Number of frames in sound_file_1 is: ", sound_file_1.getnframes())
    print("Number of frames in sound_file_2 is: ", sound_file_2.getnframes())

    # Extract Raw Audio from Wav File
    # -1 is used as an argument to get all the frames from sound_file
    # and is equivalent to readframes(sound_file.getnframes())
    signal_1 = sound_file_1.readframes(-1)
    signal_2 = sound_file_2.readframes(-1)

    # ONLY FOR TESTING!!!
    temp = numpy.fromstring(signal_1, dtype="int16")
    temp2 = numpy.fromstring(signal_2, dtype="int16")

    sample_audio_vector = numpy.fromstring(signal_1, dtype="int16").tolist()
    pink_noise_vector = numpy.fromstring(signal_2, dtype="int16").tolist()
    print(sample_audio_vector)
    print(pink_noise_vector)

    convolution_vector = my_convolve.MyConvolve(sample_audio_vector, pink_noise_vector)
    print(convolution_vector)

