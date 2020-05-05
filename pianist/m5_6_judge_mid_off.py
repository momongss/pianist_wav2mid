import numpy as np


def External_use(middle_mid, conceive_mid_data, divide_len, sampling_rate, len_wav):

    judge_mid_on = []

    middle_mid = middle_mid[0]  # single, mono case 를 다루기 때문에

    i = 0
    index = []
    for c in conceive_mid_data:
        if c == [0, 1]:
            index.append(i)
        i += 1

    print(len(index))

    divide_len_time = divide_len / sampling_rate

    def index_to_time(index, divide_len_time):
        judge_on_time = []
        for i in index:
            judge_on_time.append(i * divide_len_time)

        return judge_on_time

    judge_on_time = index_to_time(index, divide_len_time)

    def time_len_time(judge_on_time, divide_len_time):

        time_table_on = []

        for j in judge_on_time:
            temp = [j - divide_len_time, j + divide_len_time]
            time_table_on.append(temp)

        return time_table_on

    time_table_on = time_len_time(judge_on_time, divide_len_time)

    for t in time_table_on:
        for m in middle_mid:
            if (m[2][0] < t[1]) & (m[2][0] > t[0]):
                judge_mid_on.append(m[0])
                break

    return judge_mid_on


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
    import m4_1_middle_preprocessing as m4_1

    dir = 'C:\\Users\\TH\\Desktop\\music\\music composer\\01 Start\\'

    songname = 'to_1_8'

    mid_filename = dir + songname + '.mid'
    wav_filename = dir + songname + '.wav'

    import mido

    mid = mido.MidiFile(mid_filename)
    middle_mid = m4_1.External_use(mid, mid.ticks_per_beat)

    import mido
    import m3_1_conceive_mid_preprocessing
    from pydub import AudioSegment

    wav = AudioSegment.from_wav(wav_filename)
    wave = wave_opener(wav_filename)

    divide_len = 220
    sampling_rate = wav.frame_rate
    len_wav = len(wave[0])

    mid = mido.MidiFile(mid_filename)
    conceive_mid_data = m3_1_conceive_mid_preprocessing.External_use(mid, divide_len, sampling_rate, len_wav)

    judge_mid_on = External_use(middle_mid, conceive_mid_data, divide_len, sampling_rate, len_wav)

    print(judge_mid_on)