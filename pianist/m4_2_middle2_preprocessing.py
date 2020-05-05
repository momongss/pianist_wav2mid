import numpy as np

def External_use(middle_mid, divide_len, sampling_rate, len_wav):

    import m5_3_middle_flat_processing
    import m5_4_to_conceive_data

    middle_flat = m5_3_middle_flat_processing.External_use(middle_mid, divide_len, sampling_rate, len_wav)
    conceive_mid_data = m5_4_to_conceive_data.External_use(middle_flat, divide_len, sampling_rate, len_wav)

    return conceive_mid_data

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

    dir = "C:\\Users\\rkrp1\\Desktop\\Music\\practice_file\\"
    mid_filename = dir + "Grand_1.0_0.5.mid"
    wav_filename = dir + "Grand_1.0_0.5.mid"

    import mido
    import wave
    import m4_1_middle_preprocessing

    from pydub import AudioSegment

    wav = AudioSegment.from_wav(wav_filename)
    wave = wave_opener(wav_filename)

    mid = mido.MidiFile(mid_filename)
    middle_mid = m4_1_middle_preprocessing.External_use(mid, mid.ticks_per_beat)

    divide_len = 220

    conceive_mid_data = External_use(middle_mid, divide_len, wav.frame_rate, len(wave[0]))
    print(conceive_mid_data)

    count = 0

    for c in conceive_mid_data:
        if c != [0, 0]:
            count += 1

    print(len(conceive_mid_data))
    print(count)