def External_use(mid, divide_len, sampling_rate, len_wav):             # 외부에서는 이 함수를 통해 이 모듈에 접근해야한다.

    import m4_1_middle_preprocessing
    import m4_2_middle2_preprocessing

    ticks = mid.ticks_per_beat

    middle_mid = m4_1_middle_preprocessing.External_use(mid, ticks)
    conceive_mid_data = m4_2_middle2_preprocessing.External_use(middle_mid, divide_len, sampling_rate, len_wav)

    return conceive_mid_data

def wave_opener(file):

    import wave
    import numpy as np

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

    dir = "C:\\Users\\rkrp1\\Desktop\\Music\\practice_file\\"

    mid_filename = dir + "Grand_1.0_0.5.mid"
    wav_filename = dir + "Grand_1.0_0.5.wav"

    import mido
    import m4_1_middle_preprocessing
    from pydub import AudioSegment

    wav = AudioSegment.from_wav(wav_filename)
    wave = wave_opener(wav_filename)

    divide_len = 440
    sampling_rate = wav.frame_rate
    len_wav = len(wave[0])

    mid = mido.MidiFile(mid_filename)
    conceive_mid_data = External_use(mid, divide_len, sampling_rate, len_wav)

    print(conceive_mid_data)

    count = 0

    for c in conceive_mid_data:
        if c[0] == 1:
            count += 1

    print(len(conceive_mid_data))
    print(count)
    print(count / len(conceive_mid_data))