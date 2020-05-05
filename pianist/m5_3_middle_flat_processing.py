import numpy as np


def External_use(middle_mid, divide_len, sampling_rate, len_wav):

    divide_len_time = divide_len / sampling_rate
    mid_train_len = int(len_wav / divide_len)

    middle_flat = []
    middle_flat_on = []
    middle_flat_off = []

    for middle in middle_mid:
        for m in middle:
            middle_flat_on.append(["on", m[0], m[2][0]])
            middle_flat_off.append(["off", m[0], m[2][1]])

    middle_flat.append(middle_flat_on)
    middle_flat.append(middle_flat_off)

    return middle_flat


def wave_opener(file):

    import wave

    with wave.open(file, 'r') as wav_file:
        # Extract Raw Audio from Wav File
        signal = wav_file.readframes(-1)
        signal = np.fromstring(signal, 'Int16')

        # Split the data into channels
        channels = [[] for channel in range(wav_file.getnchannels())]
        for index, datum in enumerate(signal):
            channels[index % len(channels)].append(datum)

        return channels

if __name__ == "__main__":

    mid_filename = "C:\\Users\\TH\\Desktop\\music composer\\midi\\way back home.mid"
    wav_filename = "C:\\Users\\TH\\Desktop\\music composer\\midi\\way back home.wav"

    import mido
    import m4_1_middle_preprocessing
    from pydub import AudioSegment
    import wave

    wav = AudioSegment.from_wav(wav_filename)
    wave = wave_opener(wav_filename)

    mid = mido.MidiFile(mid_filename)
    middle_mid = m4_1_middle_preprocessing.External_use(mid, mid.ticks_per_beat)

    divide_len = 220

    middle_flat = External_use(middle_mid, divide_len, wav.frame_rate, len(wave[0]))
    print(middle_flat)