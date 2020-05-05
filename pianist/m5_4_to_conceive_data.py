import numpy as np

def External_use(middle_flat, divide_len, sampling_rate, len_wav):

    # ['on', 70, 0.375] --> [1,0]

    divide_len_time = divide_len / sampling_rate
    mid_train_len = int(len_wav / divide_len)

    conceive_mid_data = []
    for __ in range(mid_train_len):
        conceive_mid_data.append([0, 0])

    middle_flat_on = middle_flat[0]
    middle_flat_off = middle_flat[1]

    for m in middle_flat_on:
        index = int(m[2] / divide_len_time)
        conceive_mid_data[index][0] += 1

    for m in middle_flat_off:
        index = int(m[2] / divide_len_time)
        try:
            conceive_mid_data[index][1] += 1
        except:
            pass

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

    mid_filename = "C:\\Users\\TH\\Desktop\\music composer\\midi\\way back home.mid"
    wav_filename = "C:\\Users\\TH\\Desktop\\piano\\01 Start\\C3_damper_sound3.wav"

    import mido
    import m4_1_middle_preprocessing
    from pydub import AudioSegment

    # wav = AudioSegment.from_wav(wav_filename)
    wave = wave_opener(wav_filename)

    print(len(wave))
    print(len(wave[0]))
    print(len(wave[1]))

    f = open("C:\\Users\\TH\\Desktop\\piano\\01 Start\\c3_damper_sound_1_3.txt", 'w')
    for wav in wave[1
    ]:
        f.write(str(wav)+'\n');
    f.close()



    # mid = mido.MidiFile(mid_filename)
    # middle_mid = m4_1_middle_preprocessing.External_use(mid, mid.ticks_per_beat)
    #
    # divide_len = 220
    #
    # import m5_3_middle_flat_processing
    #
    # middle_flat = m5_3_middle_flat_processing.External_use(middle_mid, divide_len, wav.frame_rate, len(wave[0]))
    #
    # conceive_mid_data = External_use(middle_flat, divide_len, wav.frame_rate,len(wave[0]))
    #
    # print(conceive_mid_data)
    #
    # count = 0
    #
    # for c in conceive_mid_data:
    #     if c != [0, 0]:
    #         count+=1
    #
    # print(len(conceive_mid_data))
    # print(count)